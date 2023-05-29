import pandas as pd

if __name__ == '__main__':

    print("Combining original and updated eviction cases...")

    # Load updated court cases
    updated = pd.read_csv("clean_UpdatedCourtCases.csv")

    # Load updated cleaned cases
    original = pd.read_csv("clean_all_cases.csv")

    # Remove repeated Case IDs
    updated = updated[~updated["CASE_ID"].isin(original["CASE_ID"])]

    # Concatenate both dataframes
    all = pd.concat([original, updated], axis=0)
    all = all.reset_index().drop("index", axis = 1)

    # Write All Eviction Cases
    all.to_csv("AllEvictionCases.csv", index=None)

    print("Written AllEvictionCases.csv!")

