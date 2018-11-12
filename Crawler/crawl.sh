#!/bin/bash
cd polrepcrawl
printf "Clear old output\n"
rm policereport-urlids.txt
rm urls-no-id.txt
rm urls-not-ok.txt
rm policereports.json
printf "Crawl police report urls\n"
pipenv run scrapy crawl getreporturls
print "Scrape police report data for each url\n"
pipenv run scrapy crawl getreportdata -a filename=policereport-urlids.txt
printf "Finished\n"
