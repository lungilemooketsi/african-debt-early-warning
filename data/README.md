# Data

This folder is tracked so the project has a place to put a fiscal panel. The dataset files themselves are not in the public tree.

## What was removed

`raw_fiscal_data.xlsx` was the 10alytics Data Science Hackathon workbook. One sheet is the hackathon problem statement. The `Data` sheet is a compiled country-year panel whose `Source` column names national publishers (central banks, finance ministries, revenue authorities, and statistics offices), including the Central Bank of Nigeria, the Bank of Ghana, the South African Reserve Bank, and peer institutions. `cleaned_fiscal_data.csv` was that panel after unit scaling and pivoting. Both files are omitted here. They remain in git history; this change does not rewrite history.

No World Bank or IMF extract is in the repository. Those sources were not the file that was committed.

## What to use instead

Build your own workbook and save it as `data/raw_fiscal_data.xlsx` (gitignored):

- [World Bank World Development Indicators](https://data.worldbank.org/). The World Bank's terms allow reuse under [Creative Commons Attribution 4.0 (CC BY 4.0)](https://datacatalog.worldbank.org/public-licenses). Cite the World Bank.
- [IMF World Economic Outlook](https://www.imf.org/en/publications/weo). The tables are public. Follow the [IMF copyright and usage terms](https://www.imf.org/en/about/copyright-and-usage) before you commit or republish a download.
- The national institution that publishes the series you need (central bank, statistics office, or finance ministry). Use that institution's own terms.

A World Bank or IMF file you download yourself may live in this folder locally. Commit it only when that licence allows redistribution.

## Layout the cleaner expects

- Sheet name: `Data`
- `Country`
- `Year`, or `Time` as a date that contains a year
- `Indicator`
- `Amount` or `Value`
- `Unit`: `Million`, `Billion`, or `Trillion` (scaled to billions)

Include a GDP level (`Nominal GDP`, `Real GDP`, or `GDP`), a debt stock (`Government Debt`, `Total_Debt`, or `Debt`), plus revenue or tax revenue and the budget deficit or surplus when you have them. Keep each level series in one currency, or convert it before you run the cleaner. The hackathon workbook mixed national currencies in a single amount column.

Then:

```bash
python src/data_cleaner.py
```

That writes `data/cleaned_fiscal_data.csv`, which is gitignored. No API key is required.
