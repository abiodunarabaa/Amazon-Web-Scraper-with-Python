import requests
from bs4 import BeautifulSoup

def scrape_amazon_product(url):
    # Send a GET request to the Amazon product page
    response = requests.get(url)
    
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract product details
    product_title = soup.find('span', {'id': 'productTitle'}).text.strip()
    product_price = soup.find('span', {'id': 'priceblock_ourprice'}).text.strip()
    product_rating = soup.find('span', {'class': 'a-icon-alt'}).text.strip()
    product_reviews_count = soup.find('span', {'id': 'acrCustomerReviewText'}).text.strip()
    
    # Print the extracted details
    print('Product Title:', product_title)
    print('Price:', product_price)
    print('Rating:', product_rating)
    print('Number of Reviews:', product_reviews_count)

# Example usage:
amazon_product_url = 'https://www.amazon.com/dp/B07VGRJDFY'
scrape_amazon_product(amazon_product_url)



#Before scraping an Amazon website, please study the terms of service and the robots.txt file.
#It is important to remember that this activity may violate the company's website scraping policy.
#Furthermore, to stay out of trouble with the law, always abide by the website's robots.txt file and scrape appropriately.