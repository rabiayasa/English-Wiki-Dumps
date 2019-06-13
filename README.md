# How to download ready wikidumps via Python requests
## Wikipedia
Wikipedia is a great source of online knowledge in many languages. If you need a huge corpus to work on it, the best is downloading a wikipedia articles. [In here](https://en.wikipedia.org/wiki/List_of_Wikipedias), you can see list of the different language editions of Wikipedia and check how many articles includes in selected languages or what the size of selected languages and so on. Also you can find IETF language tag (language code) for preferred language, it helps while finding related Wikidumps. 

## Wikidumps
Wikimedia offers ready database backup dumps and you can choose the latest completed version of wikidumps. Wikidumps are updated regularly. [In here](https://dumps.wikimedia.org/backup-index.html), you can select the language you want to work with. In this task, we will work on English Wikidumps.

First, it is needed to select the newest version of completed backup, [in here](https://dumps.wikimedia.org/enwiki/). (Sometimes latest version can incomplete.) Dump pages offers different types of alternative such as article pages only or including talk and  user pages. It is better to check [here](https://en.wikipedia.org/wiki/Wikipedia:Database_download#English-language_Wikipedia) to identify which option covers your work needs. Depending on the nature of your work, you can work with the partitioned files or a merged single file. In this work, we will download the partitioned files of only articles (no talk or user pages). Backups are bz2 compressed XML files.

## Prerequisites
BeautifulSoup and Keras is needed to download the pages.

```
pip install BeautifulSoup
pip install Keras
```
The default save location for Keras is
```
~/.keras/datasets/
``` 
In Windows, it is needed to run the code in keras location.
