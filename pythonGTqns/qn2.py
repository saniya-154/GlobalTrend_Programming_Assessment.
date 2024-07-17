#Write a Python function that takes a list of URLs, attempts to download their content, and retries up to 3 times if an error occurs. Use appropriate error handling to manage different types of exceptions.
import requests 
from time import sleep 
def download_url_content(urls):
    def fetch_url(urls,retries=3):
        for attempt in range(1,retries + 1):
            try :
                response = requests.get(urls,timeout = 10)
                response.raise_for_status()
                return response.content
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err} - URL: {url} (Attempt {attempt} of {retries})")
            except requests.exceptions.ConnectionError as conn_err:
                print(f"Connection error occurred: {conn_err} - URL: {url} (Attempt {attempt} of {retries})")
            except requests.exceptions.Timeout as timeout_err:
                print(f"Timeout error occurred: {timeout_err} - URL: {url} (Attempt {attempt} of {retries})")
            except requests.exceptions.RequestException as req_err:
                print(f"Request error occurred: {req_err} - URL: {url} (Attempt {attempt} of {retries})")
            sleep(1)  # Sleep for 1 second before retrying
        return None
    results = {}
    for url in urls:
        content = fetch_url(url)
        if content:
            results[url] = content
        else:
            results[url] = "Failed to download content after 3 attempts"

    return results
urls = [
    "https://www.example.com",
    "https://www.nonexistentwebsite.com",
    "https://httpstat.us/500"
]

downloaded_content = download_url_content(urls)
for url, content in downloaded_content.items():
    if isinstance(content, bytes):
        print(f"Successfully downloaded content from {url}")
    else:
        print(f"Error: {content}")