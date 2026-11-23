# Input data

Nothing in this folder is committed except this file. The notebooks create the snapshots here on
first run.

| File | Source | Written by |
|---|---|---|
| `wiki_membership.json` | Raw HTML of Wikipedia's *List of S&P 500 companies* and *Historical components of the S&P 500* | Part 1, cell 2 |
| `prices_2015-01-01_2026-08-24.parquet` | Yahoo Finance adjusted closes (`yfinance`) for every historical member plus SPY and RSP | Part 1, cell 4 |
| `failed_2015-01-01_2026-08-24.json` | Tickers Yahoo returned nothing for | Part 1, cell 4 |
| `hedge_*.parquet` | State rebuilt by Part 2 from the two snapshots above | Part 2, cell 2 |

Prices are not redistributed here: they are Yahoo Finance data, subject to its terms.

## The snapshots behind the paper

The notebooks print these hashes when they load a snapshot. A matching hash means the run is using
the same inputs as the paper.

| Snapshot | Shape / captured | Content hash (printed by the notebook) |
|---|---|---|
| Membership (`wiki_membership.json`) | captured 2026-10-24 06:56 UTC | `2df28d3ebfae3e17` |
| Prices (`prices_2015-01-01_2026-08-24.parquet`) | 2,926 dates × 615 tickers, 0 failed | `255853e91a9228f5` |

A fresh download yields different hashes, because Yahoo's coverage of delisted tickers and the
Wikipedia pages both change over time. The results should be close, but not identical. The exact
snapshots are available from the authors on request.
