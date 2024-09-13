<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>
    <h1>Web Scraping Project</h1>
    <p>This project demonstrates a web scraping application using Python, BeautifulSoup, and Selenium. The application extracts data from web pages and saves the scraped data into a CSV file.</p>

    <h2>Project Structure</h2>
    <ul>
        <li><strong>main.py:</strong> Uses Selenium to open a web browser, search for content, and navigate web pages. It uses the Chrome WebDriver to automate interactions on the Python website.</li>
        <li><strong>collection.py:</strong> Uses BeautifulSoup to parse local HTML files stored in the "data" directory. It extracts product details such as title, price, link, and image and stores them in a CSV file.</li>
        <li><strong>data.csv:</strong> The CSV file where the scraped data is saved.</li>
    </ul>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li>BeautifulSoup4</li>
        <li>Pandas</li>
        <li>Selenium</li>
        <li>Chrome WebDriver</li>
    </ul>
    <p>To install the required packages, you can use the following commands:</p>
    <pre><code>pip install bs4
pip install pandas
pip install selenium</code></pre>

    <h2>How to Run the Project</h2>
    <h3>Step 1: Setup Selenium</h3>
    <p>Download and install the Chrome WebDriver for your browser version from <a href="https://sites.google.com/a/chromium.org/chromedriver/downloads">here</a>. Ensure that the path to the Chrome WebDriver is added to your system's PATH environment variable.</p>

    <h3>Step 2: Run main.py</h3>
    <p>This script opens a browser and performs a search for the term "pycon" on the Python.org website. It uses Selenium to automate this task.</p>
    <pre><code>python main.py</code></pre>

    <h3>Step 3: Run collection.py</h3>
    <p>This script parses local HTML files located in the "data" directory. It extracts product information (title, price, link, and image) and saves it to <code>data.csv</code>.</p>
    <pre><code>python collection.py</code></pre>

    <h2>Data Collection Process</h2>
    <p>The project collects data from static HTML files. BeautifulSoup is used to parse each file and extract relevant product details such as:</p>
    <ul>
        <li><strong>Title:</strong> The product's title extracted from an anchor tag inside a div with class <code>'RfADt'</code>.</li>
        <li><strong>Price:</strong> The product's price extracted from a span tag with class <code>'ooOxS'</code>.</li>
        <li><strong>Link:</strong> The product's link, extracted from an anchor tag.</li>
        <li><strong>Image:</strong> The URL of the product image, extracted from an img tag inside a div with class <code>'picture-wrapper jBwCF'</code>.</li>
    </ul>

    <h2>Error Handling</h2>
    <p>The <code>collection.py</code> script contains basic error handling to catch and print any exceptions that occur during the parsing process.</p>

    <h2>Output</h2>
    <p>After successfully running the script, the extracted data is saved in <code>data.csv</code> in the following format:</p>
    <ul>
        <li><strong>Title</strong></li>
        <li><strong>Price</strong></li>
        <li><strong>Link</strong></li>
        <li><strong>Image</strong></li>
    </ul>
</body>
</html>
