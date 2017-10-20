# Korp API for Python
Library for Python to use Korp API. This library provides an easy way to query [Korp systems](https://spraakbanken.gu.se/swe/forskning/infrastruktur/korp/) for language corpora.

# Usage

You can initialise Korp with either service_name ([språkbanken](https://spraakbanken.gu.se/korp/#?lang=sv), [kielipankki](https://korp.csc.fi) or [GT](http://gtweb.uit.no/korp)) or url to your Korp’s API interface such as https://korp.csc.fi/cgi-bin/korp.cgi .

An example for getting all concordances for North Sami corpora in Giellatekno Korp for query _[pos=”A”] “go” [pos=”N”]_.

    from korp.korp import Korp
    korppi = Korp(service_name="GT") #uses Giellatekno
    corpora = korppi.list_corpora("SME") #lists corpora returns the ones starting with the North Sami language code
    number_of_results, concordances = korppi.all_concordances('[pos="A"] "go" [pos="N"]', corpora)
    
# More information

[See the Wiki](https://github.com/mikahama/python-korp/wiki)

# Licence
Apache License 2.0
(C) [Mika Hämäläinen](https://mikakalevi.com) 2017

