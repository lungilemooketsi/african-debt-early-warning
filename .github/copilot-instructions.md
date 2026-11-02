# African Sovereign Debt Crisis — Early Warning System

## Project overview

Pipeline that cleans a country-year fiscal panel, flags next-year debt stress, and runs a revenue-shock and contagion view.

## Project structure

- `data/` — local workbook only. The hackathon extract is not in the repo. Read `data/README.md` before adding files. `data/*.xlsx` and `data/*.csv` are gitignored.
- `src/` — cleaning, the random-forest model, and the stress-test simulation.
- `outputs/` — charts. Generated CSV tables are gitignored.
- `notebooks/` — empty placeholder for exploration.

## Setup

1. `pip install -r requirements.txt`
2. Save your own panel as `data/raw_fiscal_data.xlsx` (see `data/README.md`). World Bank WDI is CC BY 4.0. IMF WEO is public under the IMF's own terms.
3. `python src/data_cleaner.py`
4. `python src/model_engine.py`
5. `python src/pioneer_simulation.py`

If the workbook is missing, the scripts should explain that and exit without writing tables.

## Behaviour to preserve

- Scale Million / Billion / Trillion amounts to billions.
- Engineer Debt_to_GDP, Deficit_to_GDP, and Tax_to_GDP.
- Label stress when next year's debt-to-GDP ratio is above 70 percent.
- Do not commit hackathon workbooks, Zindi exports, API keys, or generated score tables.
