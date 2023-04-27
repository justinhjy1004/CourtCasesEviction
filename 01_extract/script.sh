#!/bin/bash

ls ./CourtCases/*.json | xargs -P 8 -n 1 python3 extractionv2.py 