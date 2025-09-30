# 🐿️ Squirrel Census Analysis

This is a small pandas project that counts Central Park squirrels by their **Primary Fur Color**.

Dataset: [2018 Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw)

## Features
- Counts the number of squirrels with **Gray, Cinnamon, and Black** fur.
- Exports results to a CSV file (`squirrel_summary.csv`).
- Two different solutions:
  1. Direct counting with `len()`.
  2. Looping through colors and building a dictionary.

## How to run
```bash
python squirrel_count.py
```
The result is saved as `squirrel_summary.csv`.