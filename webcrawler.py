import requests
from bs4 import BeautifulSoup

# Add terms to this list that shouldn't appear in results
reject_list = ["careers", "policies", "source", "Source", "privacy", "accessibility", "audio", "about", "="]

def simple_web_crawler(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find and extract relevant information from the page
        # For example, let's extract all the links on the page
        links = soup.find_all('a')

        link_list = []
        # Print the extracted links
        for link in links:
            href = link.get('href')
            if href and "https://www." in href and not any(x in href for x in reject_list):
                link_list.append(href)
    else:
        # Print an error message if the request was not successful
        # print(f"Failed to fetch URL: {url}")
        pass
    
    return set(link_list)


def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file.readlines()]
    return urls


file_path = 'normalurls.txt'  # Replace the string with the path to your text file containing URLs
urls = read_urls_from_file(file_path)

for url in urls:
    for link in simple_web_crawler(url):
        print(link)
