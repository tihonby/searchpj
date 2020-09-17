# Search Project 
## Search program 
Configured to search the site for books and return search results.

## Functions
By keywords of the book title, text, author name or part of the url finds a match and provides the result in the form of a list of title, author and URL.

## Components
Django 2.2, PostgreSQL, Scrapy.

## Implementation
The web crawler crawls the site, highlighting the following information: title of the book, author, url, and abstract to the book. Possible output in csv or json format.
The information is recorded in the database, from where the search on request takes place.

## Settings
the first page of the search is written to the parser file my scraper / scraper.py, the search queries by tags and the passage through the site are configured. The scraper is started by the command:
```bash
scrapy runspider scraper.py 
     this command creates the corresponding file:
scrapy runspider scraper.py -o output.csv -t csv
scrapy runspider scraper.py -o output.json
```
## Features
When extracting xpath by tags of the same type, iteration did not occur correctly (or did not happen at all), and information on one of the search fields was added equally to all results on the page. As a result, I had to limit myself to css, although this is less convenient.
