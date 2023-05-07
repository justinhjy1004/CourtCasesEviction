#!/bin/bash

# Making relevant directories
mkdir -p geocoderesult
mkdir -p geocode

# Take Relevant Columns
python3 relevant_columns.py clean_all_cases.csv

# Split files into 10,000 each, this is to not the make Census angry
split -dl 10000 --additional-suffix=.csv geocodable.csv part_  

# Move the split files into the input directory
mv part_* geocode

# python3 geocode.py [INPUT DIR] [OUTPUT DIR]
# To request geocoding service file by file
python3 geocode.py geocode geocoderesult

# Concatenate all files into one
cat ./geocoderesult/*.csv > geocoderesult.csv
# Get the Matches
grep -hr "Exact" geocoderesult.csv > matches.csv
# And the failures
grep -hr "No_Match" geocoderesult.csv > no_match.csv