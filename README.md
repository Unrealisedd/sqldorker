# sqldorker

Simple Google dorker that finds URLs with query parameters and tests them for SQL injection. Takes a dork like `inurl:"?id="`, grabs results, then throws basic SQLi payloads at each parameter and checks for SQL error strings in the response.

See [ImprovedSqlDorker](https://github.com/Unrealisedd/ImprovedSqlDorker) for the version with Tor rotation and Wappalyzer-based payload selection.

## Setup

```
pip install googlesearch-python requests colorama
```

## Usage

```
python sqldorker.py
```

Enter your dork and the number of URLs to test. Vulnerable URLs show up in green.

There's also a `sql injectable dorks` file with some example dorks to try.
