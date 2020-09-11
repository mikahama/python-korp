# Korp API for Python
Library for Python to use Korp API. This library provides an easy way to query [Korp systems](https://spraakbanken.gu.se/swe/forskning/infrastruktur/korp/) for language corpora.

# Installation

    sudo pip install korp

# Usage

You can initialise Korp with either service_name ([språkbanken](https://spraakbanken.gu.se/korp/#?lang=sv), [kielipankki](https://korp.csc.fi) or [GT](http://gtweb.uit.no/korp)) or url to your Korp’s API interface such as https://korp.csc.fi/cgi-bin/korp.cgi .

An example for getting all concordances for North Sami corpora in Giellatekno Korp for query _[pos=”A”] “go” [pos=”N”]_.

    from korp.korp import Korp
    korppi = Korp(service_name="GT") #uses Giellatekno, "kielipankki" and "språkbanken" are other possible service_name values
    corpora = korppi.list_corpora("SME") #lists corpora returns the ones starting with the North Sami language code
    number_of_results, concordances = korppi.all_concordances('[pos="A"] "go" [pos="N"]', corpora)
    
# More information

See the Wiki for [a complete description](https://github.com/mikahama/python-korp/wiki) or my blog for [a real life Korp example](https://mikalikes.men/korp-and-python-access-corpora-from-your-python-code/).

## Need for NLP solutions for your business?


<img src="https://rootroo.com/cropped-logo-01-png/" alt="Rootroo logo" width="128px" height="128px">

My company, [Rootroo offers consulting related to multilingual NLP tasks](https://rootroo.com/). We have a strong academic background in the state-of-the-art AI solutions for every NLP need. Just contact us, we won't bite.

# Cite

If you use this in an academic publication, I would be ever so grateful if you cited it as follows:

Mika Hämäläinen. (2018, January 9). Python Korp Library (Version v1). Zenodo. http://doi.org/10.5281/zenodo.1143374

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1143374.svg)](https://doi.org/10.5281/zenodo.1143374)

# Licence
Apache License 2.0
(C) 2017-2019 [Mika Hämäläinen](https://mikakalevi.com)

