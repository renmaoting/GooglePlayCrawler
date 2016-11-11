# GooglePlayCrawler
This is a distributed App crawler, and it will grabs all the App informations from Google Play, they include:
App name, company, rating, price, size, type, release time, download number and so on.

Use scrapy + redis + mongodb.

usage: scrapy crawl App

install mongodb on Ubuntu system:
  1. $ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
   //Create a /etc/apt/sources.list.d/10gen.list file and include the following line for the 10gen repository.
   deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen
   $ sudo apt-get update
   
  2. $ sudo apt-get install mongodb-10gen

config mongodb:
These packages configure MongoDB using the /etc/mongodb.conf file in conjunction with the control script. You will find the control script is at /etc/init.d/mongodb.
This MongoDB instance will store its data files in the /var/lib/mongodb and its log files in /var/log/mongodb, and run using the mongodb user account.

start mongodb:
  $ sudo service mongodb start
  You can verify that if it has started successfully by checking the contents of the log file /var/log/mongodb/mongodb.log.
  
stop mongodb:
  $ sudo service mongodb stop
  
restart mongodb:
  $ sudo service mongodb restart
  
usage of mongodb:
  Among the tools included with the MongoDB package, is the mongo shell. You can connect to your MongoDB instance by issuing the following command at the system prompt:
  $ mongo
  This will connect to the database running on the localhost interface by default. At the mongo prompt, issue the following two commands to insert a record in the “test” collection of the (default) “test” database.
  > db.test.save( { a: 1 } )
  > db.test.find()

