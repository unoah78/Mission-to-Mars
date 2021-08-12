#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install splinter


# In[2]:


pip install webdriver_manager


# In[3]:


pip install bs4


# In[4]:


pip install pymongo


# In[5]:


pip install Flask-PyMongo


# In[6]:


pip install html5lib


# In[7]:


pip install lxml


# In[8]:


from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[9]:


# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[10]:


# Visit the Quotes to Scrape site
url = 'http://quotes.toscrape.com/'
browser.visit(url)


# In[11]:


# Parse the HTML
html = browser.html
html_soup = soup(html, 'html.parser')


# In[12]:


# Scrape the Title
title = html_soup.find('h2').text
title


# In[13]:


# Scrape the top ten tags
tag_box = html_soup.find('div', class_='tags-box')
# tag_box
tags = tag_box.find_all('a', class_='tag')

for tag in tags:
    word = tag.text
    print(word)


# In[14]:


url = 'http://quotes.toscrape.com/'
browser.visit(url)


# In[15]:


for x in range(1, 6):
   html = browser.html
   quote_soup = soup(html, 'html.parser')
   quotes = quote_soup.find_all('span', class_='text')
   for quote in quotes:
      print('page:', x, '----------')
      print(quote.text)
   browser.links.find_by_partial_text('Next').click()


# In[ ]:




