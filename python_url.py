import requests
from requests.exceptions import RequestException, Timeout, HTTPError, ConnectionError

def download_urls(urls):
    max_retries = 3
    
    for url in urls:
        retry_count = 0
        while retry_count < max_retries:
            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()  # Raise HTTPError for bad responses
                content = response.content
                print(f"Downloaded content from {url}")
                break  # Break the retry loop if successful
            except (Timeout, ConnectionError) as e:
                print(f"Error downloading {url}: {type(e).__name__}. Retrying...")
                retry_count += 1
            except HTTPError as e:
                print(f"HTTP Error {e.response.status_code} downloading {url}. Retrying...")
                retry_count += 1
            except RequestException as e:
                print(f"RequestException downloading {url}: {e}. Retrying...")
                retry_count += 1
        else:
            print(f"Failed to download {url} after {max_retries} retries.")
urls = [
    "https://google.com/",
    "https://facebook.com/page2",
    "https://example.com/page3",
]

download_urls(urls)
