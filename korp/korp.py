#encoding: utf-8
import requests, json, codecs, os

services = {"GT":"http://gtweb.uit.no/cgi-bin/korp_2016/korp.cgi", "kielipankki":"https://korp.csc.fi/cgi-bin/korp.cgi", "språkbanken":"https://ws.spraakbanken.gu.se/ws/korp"}


class URLNotDefinedError(Exception):
    pass

class ServiceNameError(Exception):
    pass

class KorpQueryError(Exception):
    pass

class Korp(object):
	"""docstring for Korp"""

	def __init__(self, url=None, service_name=None):
		if url is None and service_name is None:
			raise URLNotDefinedError("Either url or service_name has to be specified")
		if url is None:
			if service_name not in services:
				raise ServiceNameError("Unsupported service " + service_name + " use one of " + str(services.keys()))
			else:
				self.url = services[service_name]
		else:
			self.url = url

	def list_corpora(self, limit_by_prefix=None):
		payload = {'command': 'info'}
		r = requests.get(self.url, params=payload)
		data = r.json()
		self.__check_error__(data)
		if limit_by_prefix is None:
			return data["corpora"]
		else:
			return_data = []
			for item in data["corpora"]:
				if item.startswith(limit_by_prefix):
					return_data.append(item)
			return return_data

	def concordance(self, query, corpora, start=0, end=999, additional_parameters={"show":["word", "lemma", "lemmacomp", "pos", "msd", "ref", "dephead", "deprel", "lex"]}):
		payload = {'command': 'query', "cqp": query, "start": start, "end": end, "corpus": self.__list_to_string_list__(corpora)}
		payload.update(additional_parameters)
		r = requests.post(self.url, data=self.__prepare_payload__(payload))
		data = r.json()
		self.__check_error__(data)
		return data["hits"], data["kwic"]

	def all_concordances(self, query, corpora, additional_parameters={"show":["word", "lemma", "lemmacomp", "pos", "msd", "ref", "dephead", "deprel", "lex"]}, use_function_on_iteration=None):
		total, kwic = self.concordance(query, corpora, additional_parameters=additional_parameters)
		iteration_count = 0
		if use_function_on_iteration is not None:
			use_function_on_iteration(kwic,iteration_count)
			kwic = []
		start = 1000
		while start < total:
			iteration_count = iteration_count + 1
			if total < start + 999:
				end = total
			else:
				end = start + 999
			n, more_kwic = self.concordance(query, corpora, start=start, end=end, additional_parameters=additional_parameters)
			start = start + 1000
			kwic.extend(more_kwic)
		if use_function_on_iteration is not None:
			use_function_on_iteration(kwic,iteration_count)
			kwic = []
		return total, kwic

	def corpus_information(self, corpora):
		payload = {'command': 'info', "corpus": self.__list_to_string_list__(corpora)}
		r = requests.post(self.url, data=self.__prepare_payload__(payload))
		data = r.json()
		self.__check_error__(data)
		return data["corpora"]

	def statistics(self, query, corpora, groupby, additional_parameters={}):
		payload = {'command': 'count', "groupby": groupby, "cqp": query, "corpus": self.__list_to_string_list__(corpora)}
		payload.update(additional_parameters)
		r = requests.post(self.url, data=self.__prepare_payload__(payload))
		data = r.json()
		self.__check_error__(data)
		return data["corpora"]

	def trend_diagram(self, query, corpora, additional_parameters={}):
		payload = {'command': 'count_time', "cqp": query, "corpus": self.__list_to_string_list__(corpora)}
		payload.update(additional_parameters)
		r = requests.post(self.url, data=self.__prepare_payload__(payload))
		data = r.json()
		self.__check_error__(data)
		return data["corpora"]

	def log_likelihood(self, query1, query2, corpora1, corpora2, groupby, additional_parameters={}):
		payload = {'command': 'loglike', "set1_cqp": query1, "set2_cqp": query2, "groupby": groupby, "set1_corpus": self.__list_to_string_list__(corpora1),"set2_corpus": self.__list_to_string_list__(corpora1)}
		payload.update(additional_parameters)
		r = requests.post(self.url, data=self.__prepare_payload__(payload))
		data = r.json()
		self.__check_error__(data)
		return data

	def word_picture(self, word, corpora, additional_parameters={}):
		payload = {'command': 'relations', "word": word, "corpus": self.__list_to_string_list__(corpora)}
		payload.update(additional_parameters)
		r = requests.post(self.url, data=self.__prepare_payload__(payload))
		data = r.json()
		self.__check_error__(data)
		return data["relations"]

	def word_picture_hits(self, head, corpora, relation, sources, additional_parameters={}):
		payload = {'command': 'relations_sentences', "head": head, "rel":relation, "source": sources, "corpus": self.__list_to_string_list__(corpora)}
		payload.update(additional_parameters)
		r = requests.post(self.url, data=self.__prepare_payload__(payload))
		data = r.json()
		self.__check_error__(data)
		return data["kwic"]

	def list_additional_parameters(self, funct):
		help_data = json.load(codecs.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "api_help.json"), "r", encoding="utf-8"))
		if callable(funct):
			funct = funct.__name__
		if funct in help_data.keys():
			return help_data[funct]
		else:
			return []

	def __list_to_string_list__(self, l):
		string_list = ""
		for item in l:
			string_list = string_list + item + ","
		return string_list[:-1]

	def __check_error__(self, j):
		if "ERROR" in j.keys():
			raise KorpQueryError(j["ERROR"]["value"])

	def __prepare_payload__(self, payload):
		for key in payload:
			if type(payload[key]) is list:
				payload[key] = self.__list_to_string_list__(payload[key])
		return payload


