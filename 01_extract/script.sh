#!/bin/bash

ls ./CourtCases/*.json | xargs -P 8 -n 1 python3 extractionv2.py 

Rscript file_combiner.R

cp all_cases.csv ../02_cleaning