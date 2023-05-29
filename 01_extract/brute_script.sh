#!/bin/bash

ls ./UpdatedCourtCases/*.json | xargs -P 8 -n 1 python3 extractionv2.py 

Rscript brute_combiner.R UpdatedCourtCases

