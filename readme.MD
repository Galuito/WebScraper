# Web Scraper using Python by @Galuito
This will be my first web scraper using python to test the reach and uses of an aplication that has such capabilities in here, I'll try to document what I think about the project, save the important notes and specify which modules or libraries I am using.

I will be doing web scraping from Wikipedia.

# Used Library
For scraping the web, I'll be using Scrapy, it was recommended by many sources and it was referred as a library that holds your hand and can be very helpful for someone that doesn't have that much experience over python, so, I think it's a good starting point

# General Documentation
This is the summary of what you have to do in order to make this work, also, there are some things which I didn't explain when doing my first example so I'll add those in here.
1. Install scrapy in your virtual environment
2. Create your scrapy project with 'scrapy startproject "projectName"'
3. Change your directory into the folder that you just created and create your spider 'scrapy genspider "name" "website.com.xy"'
## Remember to put the https in the start_urls
4. Place all the urls that you plan to visit inside of the start_urls variable
5. Open the scrapy shell through your terminal and test your css selectors 'scrapy shell'
## First, fetch your url 'fetch("https://exampleurl.com.uk")'
## Then, use the response.css('css .class/element/#id') to apply and check values
### Remember to use the .get() function and the ::text option like the following .css(a::text)
## Inspect the page in your browser in order to get the classes, ids and html element types
6. After you have what you want create your item inside of your items.py file
## Create a variable for each of the fields in the item that you're going to create per yield
7. Create your item loader taking into consideration the fields of your item, in here you can define the variable_in MapCompose function in which you can create a small pipeline that allows you to process certain data types through the use of a lambda function, if you want to do big changes you should do them in the pipelines.
## You have to import your item loader from your project like from project.itemloaders import ClassLoader
### The itemloader.py file doesn't come by default you need to create it
8. Handle your parsing logic inside of the parse function and think if you're going to use many items inside of different links or many items inside of the same page, the first example can be found in saleChecker the former can be found in currencyChecker
9. Once you are done try crawling your spider with 'scrapy crawl "spider_name"'
## If you want to save the values that you receive which you'll probably want to then you have to place -O "fileName.xxx" at the end of your crawl command, xxx can be json, css, and other useful file types
### I recommend placing your results inside of a results folder like so -O project/results/result_X.json
10. Start debugging your values until you get the desired raw data, don't try to process it yet, check that everything works before that, you could also avoid doing processing in your item loader to check that everything works before causing an error too soon.
11. Once every value works if you need you can create a Pipeline inside of pipelines.py file, once you create it and integrate it throughout the use of the item that you created in your itemloader, this can be used to modify strings, numeric values that couldn't be done or would be too problematic in previous steps.
## Even if you create a pipeline you need to activate it in the settings.py file, pipelines are inside of the ITEM_PIPELINES dictionary, in which they have a numeric value, this value can go from 1 to 1000 and is the one that specifies which pipeline goes first and which pipeline goes last (from small numbers to big numbers)
12. If you need to change how the predefined functions work you can do it inside of the middleware.py file, in this you can modify the request method and manage cookies and so much more.


# Notes
Once we create the Scrapy project many folders and files are generated, some of those files have important functionalities, here are some of them.

itemloaders.py
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
