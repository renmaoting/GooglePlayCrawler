# GooglePlayCrawler
This is a simple App crawler, it will grabs all the App informations from Google Play, they include:
App name, company, rating, price, size, type, release time, download number and so on. THen it will store datas into mongodb

Use scrapy + mongodb.

usage: scrapy crawl App


necessary package installation:

1. install Python-pip: sudo apt-get install python-pip
2. install scrapy: sudo pip install scrapy
3. install mongodb: sudo apt-get install mongodb
4. install pymongo: sudo pip install pymongo

linux install mongochef which is a GUI tool: 

1. download http://3t.io/mongochef/download/core/platform/#tab-id-3
2. tar -xvzf mongochef-linux-x64-dist.tar.gz
3. ./mongochef-4.4.2-linux-x64-dist/bin/mongochef.sh
