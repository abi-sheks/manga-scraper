# Manga Scraper  
quick command line app that i'm using to track updates on my favourite manga, by scraping a [free online manga site](https://h.mangabat.com/).  
uses a simple requests + beautifulsoup setup considering the site only serves static HTML.  
uses a postgres database (peewee as ORM)  
## Setup  
Make sure you have a postgres instance up and running on your system. create a ```.env``` file like the one in ```.env.example```. (the scraping is obviously super website specific, so use the same website link).  
Usage instructions are within the command line app itself.  
You can subscribe for updates for a specific manga, and then query the command line tool for updates, which i find faster than navigating the actual website.  
## Future plans  
I just wanted a quick intro to web scraping and also a CLI based tool to check updates (my browser is slow lol).  
will perhaps implement periodic scraping while the app is running, or something along those lines (without overloading the website of course)