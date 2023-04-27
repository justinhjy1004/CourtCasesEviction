#!/bin/bash

mkdir -p bfscraped

python3 brute_force_scraper.py Lancaster 21 15000 4 300
python3 brute_force_scraper.py Lancaster 22 15000 4 300
python3 brute_force_scraper.py Lancaster 23 9000 4 300
python3 brute_force_scraper.py Douglas 21 30000 4 300
python3 brute_force_scraper.py Douglas 22 30000 4 300
python3 brute_force_scraper.py Douglas 23 15000 4 300
