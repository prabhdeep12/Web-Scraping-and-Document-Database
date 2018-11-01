
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
import tweepy
import pandas as pd
from splinter import Browser
import time
import pymongo
import requests 


# In[2]:


url = "https://mars.nasa.gov/news/"
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')


# In[3]:


news_title = soup.find('div', 'content_title', 'a').text
news_p = soup.find('div', 'rollover_description_inner').text


# In[4]:


print(news_title)
print(news_p)


# In[5]:


executable_path = {'executable_path' : 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)


# In[6]:


browser.click_link_by_partial_text('FULL IMAGE')
#time.sleep(5)


# In[8]:


browser.click_link_by_partial_text('more info')


# In[9]:


new_html = browser.html
new_soup = BeautifulSoup(new_html, 'html.parser')
temp_img_url = new_soup.find('img', class_='main_image')
back_half_img_url = temp_img_url.get('src')

recent_mars_image_url = "https://www.jpl.nasa.gov" + back_half_img_url

print(recent_mars_image_url)


# In[10]:


url_weather = "https://twitter.com/marswxreport?lang=en"
browser.visit(url_weather)


# In[11]:


html_weather = browser.html
soup = BeautifulSoup(html_weather, "html.parser")

mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
print(mars_weather)


# In[12]:


url_facts = "https://space-facts.com/mars/"


# In[13]:


table = pd.read_html(url_facts)
table[0]


# In[14]:


df_mars_facts = table[0]
df_mars_facts.columns = ["Parameter", "Values"]
df_mars_facts.set_index(["Parameter"])


# In[15]:


mars_html_table = df_mars_facts.to_html()
mars_html_table = mars_html_table.replace("\n", "")
mars_html_table


# In[18]:


url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
hemisphere_image_urls = hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"},
]


# In[19]:


print(hemisphere_image_urls)

