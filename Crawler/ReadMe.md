# Police Report Crawler

## Getting started

Run in terminal:
```
pipenv install
```

## Run Crawler

To fetch policereport-urlids run:
```
cd polrepcrawl
scrapy crawl getreporturls
```

To scrape relevant policereport-data run 
(requires policereport-urlids.txt from previous crawl):
```
cd polrepcrawl
scrapy crawl getreportdata -a filename=policereport-urlids.txt
```

## Start scrapy shell

Run in terminal:
```
scrapy shell
```
