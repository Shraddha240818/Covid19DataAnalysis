#!/usr/bin/env python
# coding: utf-8

# # COVID-19 DATA ANALYSIS USING PYTHON

# In[ ]:


Problem Statement-:
Coronavirus disease 2019 (COVID-19) is a contagious disease caused by the coronavirus 2 severe acute respiratory syndrome (SARS-CoV-2). 


# In[ ]:


Aim -:
The main aim of this project is to do covid analysis such as infection rate per day, no. of cases within consecutive two days, happiness rate during the pandemic, GDP per capita relation wrt infection rate.


# In[101]:


#importing libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


# In[66]:


#importing csv file
df = pd.read_csv("/Users/shraddhapadalkar/Desktop/covid19_Confirmed_dataset.csv")
df.head()


# In[67]:


df.shape


# In[68]:


#Dropped unnecessary columns 
df.drop(["Lat","Long"], axis=1, inplace=True)


# In[69]:


df.head()


# In[70]:


#Aggregated data wrt one column 
cdf = df.groupby("Country/Region").sum()


# In[71]:


cdf.head()


# In[72]:


cdf.shape


# In[73]:


#Visualizing Data related to country 
cdf.loc["China"].plot()
cdf.loc["Italy"].plot()
cdf.loc["Spain"].plot()
plt.legend()


# In[ ]:


Above graph, displays no. of covid cases for three different countries namely China, Italy, Spain


# In[74]:


#Calculating a good measure 
cdf.loc["China"].plot()


# In[ ]:


A rapid increase in covid cases is observed in China 


# In[75]:


#First three days of pandemic in china 
cdf.loc["China"][:3].plot()


# From the above plot we can see that there has been rapid increase in the covid-19 cases within the three consecutive days.

# In[76]:


#First derivative - increase or decrease in the number of covid cases (Rate of infection)
cdf.loc["China"].diff().plot()


# In[ ]:


It can be observed from the plot that the no. of covid cases were at its peak on 2nd november, 2020 and then the gradually decreased.


# In[106]:


#Maximum infection rate for China, Italy and Spain - 15136 covid cases in one day (24 hours)
cdf.loc["China"].diff().max()


# In[104]:


cdf.loc["Italy"].diff().max()


# In[105]:


cdf.loc["Spain"].diff().max()


# In[ ]:


It is noted that China is the highest infection rate with Maximum number of covid cases within past 24 hours


# In[78]:


#Find Max Infection rate for all countries 
countries = list(cdf.index)
Max_infection_rates = []
for c in countries:
    Max_infection_rates.append(cdf.loc[c].diff().max())
cdf["Max_infection_rates"]  = Max_infection_rates


# In[79]:


cdf.head(5)


# In[80]:


#creating a dataframe with only one needed column 
ncdf = pd.DataFrame(cdf["Max_infection_rates"])


# In[81]:


ncdf.head()


# In[82]:


#importing new dataset - Happiness Report Dataset 
hreport = pd.read_csv("/Users/shraddhapadalkar/Desktop/worldwide_happiness_report.csv")


# In[83]:


hreport.head()


# In[84]:


#dropping unrequired columns 

hreport.drop(["Overall rank","Score", "Generosity", "Perceptions of corruption"], axis = 1, inplace = True)


# In[85]:


hreport.head()


# In[86]:


hreport.set_index("Country or region", inplace = True)


# In[89]:


hreport.head()


# In[62]:


hreport.shape


# In[ ]:


# Joining two datasets - Covid, Happiness Report


# In[92]:


data = ncdf.join(hreport, how = "inner")


# In[93]:


data.head()


# In[ ]:


# Correlation Matrix


# In[95]:


data.corr()


# In[ ]:


Correlation matrix gives a correlation between the different parameters of the happiness report. 


# In[ ]:


# Visualizing the Results


# In[102]:


x = data["GDP per capita"]
y = data["Max_infection_rates"]
sns.scatterplot(x,np.log(y))


# In[ ]:


The scatterplot gives how GDP per capita is positively correlated to max_infection_rates


# In[103]:


sns.regplot(x,np.log(y))


# In[ ]:


The Regression plot displays the correlation between GDP and Infection rate.

