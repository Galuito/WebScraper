# Web Scraper using Python by @Galuito
This will be my first web scraper using python to test the reach and uses of an aplication that has such capabilities in here, I'll try to document what I think about the project, save the important notes and specify which modules or libraries I am using.

I will be doing web scraping from Wikipedia.

# Used Library
For scraping the web, I'll be using Scrapy, it was recommended by many sources and it was referred as a library that holds your hand and can be very helpful for someone that doesn't have that much experience over python, so, I think it's a good starting point

# Important Steps Documented
## 1. Install Scrapy
Before you do anything you need to install Scrapy. 
## 2. Start your Project
In order to start the project I had to use scrapy startproject "projectName", in my case the name of my project was willywonka
## 3. Generate The Spider that Will Crawl the Website
There are many types of spiders, being the spider the most basic and common type, the other to are the CrawlSpider and the SitemapSpider. 
To generate a spider you'll type 'scrapy genspider willyspider website.com' on your terminal an example would be 'scrapy genspider willyspider chocolate.co.uk'
### 3.1 Spider Note
If you weren't in your project folder, you'll need to place the generated spider in the /spiders folder which will be found inside a __init__.py file
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



# Notes
Once we create the Scrapy project many folders and files are generated, some of those files have important functionalities, here are some of them.

settings.py
items.py
pipelines.py
middlewares.py
scrapy.cfg

# Using ipython as the interpreter for the scrapy shell
It is recommended to use the ipython shell in order to work with the code
ipython needs to be installed in every new virtual enviroment using pip install ipython
shell = ipython

# How to get the text out of an html element
In order to get the text out of something you need to use the ::text at the end of its css selector
Gets the text only
In [16]: product.css('a.product-item-meta__title::text').get()
Out[16]: '100% Dark Hot Chocolate Flakes'

Gets the html tag and all its data
In [17]: product.css('a.product-item-meta__title').get()
Out[17]: '<a href="/products/100-dark-hot-chocolate-flakes" class="product-item-meta__title">100% Dark Hot Chocolate Flakes</a>' 

# How to get the HREF out of an anchor element
This is the easy way to get the href out of an anchor tag
product.css('a.product-item-meta__title').attrib['href']

# How to get the CSS Selectors
Now, you may be wondering, how did I get to that css specification? 
It was very easy, all you need to do is stand over the top of the html that pops up while you're inspecting a page, while you're doing that the browser will be giving you the selector that you're looking for, but you have to be careful to select actually the one that you want.

# Small problem when working in VS Code
Once you create your Scrapy Project, you'll need to cd into the folder in which you're going to be working on, this can be easily done by typing cd 'projectFolder' in your terminal, this can solve many problems and will allow your terminal to have access to your spiders, if you try to crawl your spiders without being in said folder your code won't be able to run
