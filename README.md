# Web Scraping Project

This project demonstrates a web scraping application using Python, BeautifulSoup, and Selenium. The application extracts data from web pages and saves the scraped data into a CSV file.
I have used Daraz to scrape general information of the products such as its name , url to the product, its price as well as the image of the product. The structure of the product is described below.

## Project Structure

- **main.py**: Uses Selenium to open a web browser, search for content, and navigate web pages. It uses the Chrome WebDriver to automate interactions on the Python website.
- **collection.py**: Uses BeautifulSoup to parse local HTML files stored in the "data" directory. It extracts product details such as title, price, link, and image and stores them in a CSV file.
- **data.csv**: The CSV file where the scraped data is saved.

## Requirements

- Python 3.x
- BeautifulSoup4
- Pandas
- Selenium
- Chrome WebDriver

To install the required packages, you can use the following commands:
```bash
pip install bs4
pip install pandas
pip install selenium
