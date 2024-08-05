# Google Dorking and SQL Injection Vulnerability Tester

This script performs Google dorking to find URLs based on a user-provided dorking parameter and tests those URLs for SQL injection vulnerabilities. It is intended for educational purposes only. Ensure you have explicit permission from the website owner before performing such tests.

## Requirements

- Python 3.12
- `googlesearch-python` library
- `requests` library

## Installation

1. Clone the repository or download the script.

2. Install the required libraries:
    ```sh
    pip install googlesearch-python requests
    ```

## Usage

1. Run the script:
    ```sh
    python dorking_sqli_tester.py
    ```

2. Enter the Google dorking parameter when prompted (e.g., `inurl:"?id="`).

3. Enter the number of requests (URLs) you want to test.

The script will fetch the specified number of URLs using the provided dorking parameter and test each URL for SQL injection vulnerabilities.

## Example

```sh
Enter the Google dorking parameter (e.g., inurl:"?id="): inurl:"?id="
Enter the number of requests to make: 10
Testing 10 URLs for SQL injection vulnerabilities...
Testing URL: http://example.com/page.php?id=1
Not vulnerable to SQL injection: http://example.com/page.php?id=1
Testing URL: http://example.org/item.php?id=5
Vulnerable to SQL injection: http://example.org/item.php?id=5
...
