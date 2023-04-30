"""
Name: Justin Ho
Given court cases in JSON format, extract relevant information
and save it as a CSV file

Instructions on how to use this scraper in README.md
"""

from bs4 import BeautifulSoup
import json
import pandas as pd
import sys
import re
import extractors

if __name__ == '__main__':

    # Takes the first argument as a json file
    json_file = sys.argv[1]

    with open(json_file) as file:
        data = json.load(file)

    # Creates the list of Case IDs
    case_ids = list(data.keys())
    data_csv = []

    for c in case_ids:
        # Check panels to verify what information is present
        panel = []
        panel.append(c)
        soup = BeautifulSoup(data[c])
        results = soup.find_all("h3", {"class":"panel-title"})
        for result in results:
            panel.append(result.text)

        # Scrape Information
        case_information = []
        case_information.append(c)
        soup = BeautifulSoup(data[c])
        results = soup.find_all("pre", {"class":"notranslate"})
        for result in results:
            case_information.append(result.text)

        # Correction if Judgement Info is missing
        if 'Judgment Information' not in panel:
            case_information.insert(3, None)

        data_csv.append(case_information)
        
    # Covert data into a DataFrame
    df = pd.DataFrame(data_csv, columns=["CASE_ID", "CASE_SUMMARY", "PARTIES", "JUDGEMENT_INFO", "ACTIONS"])
    
    # Extract relevant information
    df["CASE_NAME"], df["PLAINTIFF"], df["DEFENDANT"] = zip(*df.CASE_SUMMARY.map(extractors.case_name))
    df["JUDGE"] = df.CASE_SUMMARY.apply(extractors.judge)
    df["CLASSIFICATION"] = df.CASE_SUMMARY.apply(extractors.classification)
    df["PLAINTIFF"], df["PLAINTIFF_ATTORNEY"] = zip(*df.apply(lambda x: extractors.plaintiff_information(x.PARTIES, x.PLAINTIFF), axis=1))
    df["DEFENDANT"], df["DEFENDANT_ATTORNEY"] = zip(*df.apply(lambda x: extractors.defendant_information(x.PARTIES, x.DEFENDANT), axis=1))
    df["NUM_DEFENDANTS"] = df.PARTIES.apply(extractors.num_defendants)
    df["DEFENDANTS_ADDRESS"] = df.apply(lambda x: extractors.defendant_address(x.PARTIES, x.DEFENDANT), axis=1)
    df["FILING_DATE"] = df.CASE_SUMMARY.apply(extractors.filing_date)
    df["CLOSING_DATE"] = df.CASE_SUMMARY.apply(extractors.closing_date)
    df["DECISION"] = df.CASE_SUMMARY.apply(extractors.decision)

    # Write to CSV
    csv_file = re.sub(".json", ".csv", json_file)
    df.to_csv(csv_file, index=False)