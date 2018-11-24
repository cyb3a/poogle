#!/bin/bash
cd polrepcrawl
printf "Clear old output\n"
rm loc-policereport-paths.txt
rm noloc-policereport-paths.txt
rm urls-not-ok.txt
rm policereports.json
printf "Crawl police report urls\n"
pipenv run scrapy crawl getreporturls
printf "Scrape police report data for each url\n"
pipenv run scrapy crawl getreportdata
printf "Finished\n"
