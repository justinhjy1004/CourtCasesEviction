# Eviction Court Cases in Nebraska

This is a documentation on how to use the code that is relevant to the scraping and extracting information from court cases related to evictions in Lancaster and Douglas Counties in Nebraska.

This is based on the list of the comprehensive list of court cases in **/00_scrapers/CourtCaseInfo.csv**

--------------

## Scraper

Refer to the folder **00_scrapers** for this section. The scraper is developed to allow the user, given the information on court cases *(refer to /00_scrapers/CourtCaseInfo.csv)*, to scrape the court cases in HTML format. Note that the output would be in a JSON format where it is in the form of 

```python
{
    CASE_ID : "HTML Text", ...
}
```

### Instructions

To use this scraper, you would have to add the following into the folder.

1. Create a **credentials.py** file and include the following code

```python
username = your_username
password = your_password
url = "https://"+ username + ":" + password + "@" +"www.nebraska.gov/justice/case.cgi"
```

2. Download ChromeDriver (I used version 112 specifically) 
3. To run the scraper, you need to provide the county (either **Douglas** or **Lancaster**) and the start year and end year. Note that this is only applicable for years 2000 and after and for 2011, the input would be 11. Run the following in the console (I am using *bash*)

```zsh
python3 scraper.py Douglas 11 15
```

which scrapes all eviction cases in **Douglas** County from years **2011 to 2015**.

4. This would take some time, so go take a nap.

-------------------

## Extract

Refer to the folder **01_extract** for this section.

**extraction.py** reads JSON files from generated from **00_scrapers**. This is written with multithreading in mind, and hence would work well if employed in that manner though it is not necessary.

### Instructions
Take the scraped JSON file with the relevant court cases, run the following  

```bash
python3 extraction.py file_name
```

and a corresponding **csv** file would be produced.

-------------------

## Cleaning

The sad part of the any data project. Here, I included a file *(not in GitHub)* called **all_cases.csv**, which is obtained from the previous *extract* section.

Then, run, which was done in a Bash Shell
```bash
chmod +x script.sh
./script.sh
```

-------------------

## Visualization and Summary Statistic

-------------------

## Geocoding

After Cleaning in Section 02, the geocoding is done using the https://geocoding.geo.census.gov/geocoder/locations/addressbatch which takes a maximum of 10,000 lines of address and geocode and matches to the 2020 Census Tract Information.

To run this section, 
1. From the cleaned data in Section 02 Cleaning, subset **CASE_ID, STREET, CITY, STATE, ZIP**
2. Place in a directory called *geocode*
3. Run the following commands *(done in Bash)*

```bash
chmod +x geocode.sh
./geocode.sh
```

The matched data is found in *matches.csv* and the other is under *no_match.csv*.

-------------------

## Actions of Court

-------------------

## Demographics

For demographics, using Tzioumis, Konstantinos (2018) using the **predictrace** package in *R*.

To run the following section 
1. Install packages **tidyverse** and **predictrace**
2. Run the following 

```bash
Rscript demographic.R
```
