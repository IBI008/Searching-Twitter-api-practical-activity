#!/usr/bin/env python
# coding: utf-8

# In[2]:


# To prepare the work station.
# Copy the YAML file and your Twitter keys over to this Jupyter Notebook before you start to work.
import yaml
from yaml.loader import SafeLoader
from twitter import *

# Import the YAML file - remember to specify the whole path.
twitter_creds = yaml.safe_load(open('twitter_tem.yaml', 'r').read())

# Pass your Twitter credentials.
twitter_api = Twitter(auth=OAuth(twitter_creds['access_token'],
                                 twitter_creds['access_token_secret'], 
                                 twitter_creds['api_key'],
                                 twitter_creds['api_secret_key'] ))


# In[3]:


# See if you are connected.
print(twitter_api)


# In[4]:


# Run a test with #python.
python_tweets = twitter_api.search.tweets(q="#python")

# View the output.
print(python_tweets)


# In[5]:


# Identify New York and London.
# Determine worldwide trends.
trends_worldwide = twitter_api.trends.available()

# How many trends are available?
print(len(trends_worldwide))

# Example of trends_worldwide.
trends_worldwide[0]


# In[6]:


# New York
# Find New York.
our_city = 'New York'

# Create a variable.
new_york = [_ for _ in trends_worldwide if _['name'] == our_city]

# View the output.
print(len(new_york))

# Use index to find New York.
new_york[0]

# List of where on earth identifier (woeid).
new_york[0]['woeid']


# In[7]:


# London
# Find London.
our_city_2 = 'London'

# Create a variable.
london = [_ for _ in trends_worldwide if _['name'] == our_city_2]

# View the output.
print(len(london))

# Use index to find London.
london[0]

# List of where on earth identifier (woeid).
london[0]['woeid']


# In[8]:


# Question three, Common trend.
# New York
# Look at trends in New York.
new_york_trends = twitter_api.trends.place(_id = new_york[0]['woeid'])

# View the output.
new_york_trends


# In[9]:


# Look at the output as a DataFrame.
# Import Pandas.
import pandas as pd

# Create a DataFrame.
new_york_trends_pd = pd.DataFrame(new_york_trends[0]['trends'])

# View a DataFrame.
new_york_trends_pd


# In[10]:


# Narrow list down to 50,000 tweets.
new_york_trends_over50k_pd = new_york_trends_pd[new_york_trends_pd['tweet_volume'] > 50000].sort_values('tweet_volume', ascending=False)

# View the output.
print(new_york_trends_over50k_pd.shape)
new_york_trends_over50k_pd


# In[11]:


# Save output as a CSV file.
new_york_trends_over50k_pd.to_csv('new_york_trends_over50k.csv', index=False)


# In[12]:


# London
# Look at trends in London.
london = twitter_api.trends.place(_id = london[0]['woeid'])

# View the output.
london


# In[13]:


# Look at the output as a DataFrame.

# Create a DataFrame.
london_trends_pd = pd.DataFrame(london[0]['trends'])

# View the DataFrame.
london_trends_pd


# In[14]:


# Narrow list down to 50,000 tweets.
london_trends_over50k_pd = london_trends_pd[london_trends_pd['tweet_volume'] > 50000].sort_values('tweet_volume', ascending=False)

# View the output.
print(london_trends_over50k_pd.shape)
london_trends_over50k_pd


# In[15]:


# Save output as a CSV file.
london_trends_over50k_pd.to_csv('london_trends_over50k.csv', index=False)


# In[16]:


# Common trends.
# Find New York.
our_city = 'New York'

# Create a variable.
new_york = [_ for _ in trends_worldwide if _['name'] == our_city]

# View the output.
new_york[0]['woeid']


# In[17]:


# Find London.
our_city_2 = 'London'

# Create a variable.
london = [_ for _ in trends_worldwide if _['name'] == our_city_2]

# View the output.
london[0]['woeid']


# In[18]:


# Search for each city.
# Import JSON.
import json

# Search for New York.
new_york_trends = twitter_api.trends.place(_id=2459115)

# View JSON output.
print (json.dumps(new_york_trends, indent=4))


# In[19]:


# Search for London.
london_trends = twitter_api.trends.place(_id=44418)

# View JSON output.
print (json.dumps(london_trends, indent=4))


# In[20]:


# Find common topics.
new_york_trends_list = [trend['name'] for trend in new_york_trends[0]['trends']]

# View output.
print(new_york_trends_list)


# In[21]:


# Find common topics.
london_trends_list = [trend['name'] for trend in london_trends[0]['trends']]

# View output.
print(london_trends_list)


# In[22]:


# Find trends between cities.
new_york_trends_set = set(new_york_trends_list)
london_trends_set = set(london_trends_list)

# Set variable.
common_trends = new_york_trends_set.intersection(london_trends_set)

# View output.
print(common_trends)


# In[23]:


# Search for #Bitcoin
# Run a test with #Bitcoin.
bitcoin_tweets = twitter_api.search.tweets(q="#Bitcoin")

# View JSON output.
print(json.dumps(bitcoin_tweets, indent=4))


# In[ ]:




