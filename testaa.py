from korp import Korp
import pickle, json, codecs

korppi = Korp(service_name="kielipankki")
#corpora = korppi.list_corpora("SME")
corpora = ["S24"]
#print korppi.word_picture_hits('villiinty\xe4..vb.1', corpora, "ADV", ["S24:16174044", "S24:2343136"])
print korppi.list_additional_parameters(korppi.all_concordances)


#number, concordances = korppi.all_concordances('[pos="A"] "go" [pos="N"]', corpora)
#pickle.dump(concordances, open("test.bin", "wb"))

#print number
#print len(concordances)

#print korppi.concordance('[pos="A"] "go" [pos="N"]', corpora)

#print korppi.statistics('[pos="A"] "go" [pos="N"]', corpora, "pos")

#print korppi.log_likelihood('[pos="A"] "go" [pos="N"]','[pos="A"] "dago" [pos="N"]', corpora, corpora, "pos")
"""
desc = codecs.open("descriptions.txt", "r", encoding="utf-8")
desc_dict = {}
desc_dict_key = ""
for d in desc:
	if d.startswith("["):
		desc_dict[desc_dict_key].append(d.replace("\n",""))
	else:
		desc_dict_key = d.replace("\n","")
		desc_dict[desc_dict_key] = []
json.dump(desc_dict, codecs.open("api_help.json", "w", encoding="utf-8"))
"""

