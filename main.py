import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://news.ycombinator.com"

# Sending a GET request to the website
response = requests.get(url)

# Parsing the HTML content of the response with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Counter to keep track of the number of news items
count = 0

# Finding all <span> elements with the class "titleline"
spans = soup.find_all("span", class_="titleline")

# Iterating through each <span> element
for span in spans:
    # Finding the <a> tag (anchor) inside the <span>
    link_tag = span.find('a')  # <a> tag
    
    if link_tag:  # Checking if the <a> tag exists
        count += 1  # Incrementing the counter
        
        # Extracting the text (headline) and URL from the <a> tag
        link_text = link_tag.text  # Text inside the <a> tag
        link_href = link_tag['href']  # URL in the href attribute
        
        # Printing the news headline and URL
        print(f"{count}. News Title:", link_text)
        print(f"{count}. News URL:", link_href)
        
        # Breaking the loop after 10 news items
        if count == 10:
            break
