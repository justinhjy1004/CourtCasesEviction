#!/bin/bash
mkdir -p geocoderesult

split -l 8000 ./geocode/geocode.csv ./geocode/chunk_ --additional-suffix=.csv

curl --form addressFile=@./geocode/chunk_ah.csv --form benchmark=2020 https://geocoding.geo.census.gov/geocoder/locations/addressbatch --output ./geocoderesult/chunk_ah.csv
curl --form addressFile=@./geocode/chunk_ab.csv --form benchmark=2020 https://geocoding.geo.census.gov/geocoder/locations/addressbatch --output ./geocoderesult/chunk_ab.csv
curl --form addressFile=@./geocode/chunk_ac.csv --form benchmark=2020 https://geocoding.geo.census.gov/geocoder/locations/addressbatch --output ./geocoderesult/chunk_ac.csv
curl --form addressFile=@./geocode/chunk_ad.csv --form benchmark=2020 https://geocoding.geo.census.gov/geocoder/locations/addressbatch --output ./geocoderesult/chunk_ad.csv
curl --form addressFile=@./geocode/chunk_ae.csv --form benchmark=2020 https://geocoding.geo.census.gov/geocoder/locations/addressbatch --output ./geocoderesult/chunk_ae.csv
curl --form addressFile=@./geocode/chunk_af.csv --form benchmark=2020 https://geocoding.geo.census.gov/geocoder/locations/addressbatch --output ./geocoderesult/chunk_af.csv
curl --form addressFile=@./geocode/chunk_ag.csv --form benchmark=2020 https://geocoding.geo.census.gov/geocoder/locations/addressbatch --output ./geocoderesult/chunk_ag.csv
curl --form addressFile=@./geocode/chunk_aa.csv --form benchmark=2020 https://geocoding.geo.census.gov/geocoder/locations/addressbatch --output ./geocoderesult/chunk_aa.csv