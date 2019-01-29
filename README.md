# Mobile-phones-Search-Engine
A database of all the mobile phones and their specifications is created using a web-scrapping script which retrieve the data from the flipkart.com website. This database is used for searching a phone by applying filters on different specifications.

#### Initialization

The code is in python3. Thus, python3 must be installed in the system to run the script.
* Install urllib Library (if not installed)
* Install BeautifulSoup Library using [pip install beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

#### Technology Used

The database is created using sqlite and the data is scrapped from the flipkart.com website using BeautifulSoup library. The specifications of each mobile is extracted from its page and updated to the database.

#### To be included...

* The prices of the mobile phones will be scraped from various online markets and the search engine will allow to compare the prices of a product on different markets.
* Machine Learning will be applied to the dataset to predict the price for the new mobile phones to be launched by a company. And thereafter, giving recommendations of the phones with best specifications at lower price.
