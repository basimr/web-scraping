# Web Scraping

## About

This is my web scraping repo.

I made my first web scraping script to pull the names and emails of all Canadian members of parliament. I wanted these emails so I could contact them about the causes I care about.

## Instructions

1. Install Python3
2. Install scrapy
3. Run `scrapy runspider scrape-mps.py -O out/mps.json`
4. Print list of all emails: `jq -r '.[].email' out/mps.json`
5. Print semi-colon delimited list of emails, ready to be pasted into an email: `jq -r '.[].email' out/mps.json | tr '\n' ';'`
