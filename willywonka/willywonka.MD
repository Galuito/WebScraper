# Important Steps Documented for the willywonka project
## 1. Install Scrapy
Before you do anything you need to install Scrapy. 
## 2. Start your Project
In order to start the project I had to use scrapy startproject "projectName", in my case the name of my project was willywonka
## 3. Generate The Spider that Will Crawl the Website
There are many types of spiders, being the spider the most basic and common type, the other to are the CrawlSpider and the SitemapSpider. 
To generate a spider you'll type 'scrapy genspider willyspider website.com' on your terminal an example would be 'scrapy genspider willyspider chocolate.co.uk'
### 3.1 Spider Note
If you weren't in your project folder, you'll need to place the generated spider in the /spiders folder 
## 4. Repair the start_urls list, placing the correct link with all the necessary information
Initially, the start_urls contained a url that wasn't the correct one, you need to place the correct url in that list, not forgetting to put the https specification and the whole endpoint.
## 5. Open the Scrapy Shell and start testing your CSS Selectors
We will use the scrapy shell to generate the CSS Selectors that we will use to scrape the contents of the web page with our spider.
To open the scrapy shell we use "scrapy shell"
### 5.1 Scrapy Shell Note
If you're going to use ipython then you need to specify in the scrapy.cfg that the shell = ipython
Also, ipython won't be installed by default in your virtual environment, you need to install it.
## 6. Fetch the Page inside the Scrapy Shell
Fetch the page (This will automatically save it in the response variable) example: fetch('https://www.chocolate.co.uk/collections/all')
## 7. Inspect the Page in your Browser
Now we'll inspect the page manually (in our browser) and right click on an item, then, we will use the inspect element option, try to find if elements share a custom element or have a common denominator between the targets that you're interested in
### 7.1 Chocolate Example
We find that all the elements in the page have their own custom element (product-item) in the html, we can then use this to extract them into our spider, using the response variable which is housing the html of the studied page, we can now place all the elements in an object. 
#### response.css('product-item') for every item
#### response.css('product-item).get() for only the first item
## 8. Specify the data that you're interested in from those elements
Now we're going to get the information that we want out of these elements, specifically we want, names, prices and urls of each product
### 8.1 Getting the Names
To get the name all that you have to do is product.css('a.product-item-meta__title::text').get() 
### 8.2 Getting the Prices
To get the price is product.css('span.price').get().replace('<span class="price">\n              <span class="visually-hidden">Sale price</span>', '').replace('</span>', '')
### 8.3 Getting the URLs
To get the URL is product.css('a.product-item-meta__title::attr(href)').extract()
You can also do product.css('a.product-item-meta__title').attrib['href']
The latter seems more user friendly, needing to specify the SPECIFIC anchor selector and then asking for its href
## 9. Define the Parsing Function of your Spider
Once we have all of this then we need to go to our created spider and define the parsing function, once we do this we run the spider
## 10. Run your Spider
scrapy crawl "spiderName" in this case scrapy crawl willyspider 
## 11. Save The Scraped Data
In order to save this data we need to use de -O option, then we specify the file in which the data is going to be saved, this can be a json file or a CSV file
scrapy crawl willyspider -O chocolateData.json
scrapy crawl willyspider -O chocolateData.csv
The data will be saved in the main directory in which the project is located in