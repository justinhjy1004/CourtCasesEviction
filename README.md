# Eviction Court Cases in Nebraska

This is a documentation on how to use the code that is relevant to the scraping and extracting information from court cases related to evictions in Lancaster and Douglas Counties in Nebraska.

This is based on the list of the comprehensive list of court cases in **/00_scrapers/CourtCaseInfo.csv**

--------------

## Scraper

Refer to the folder **00_scrapers** for this section.

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