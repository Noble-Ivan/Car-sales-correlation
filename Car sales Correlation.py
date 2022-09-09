#!/usr/bin/env python
# coding: utf-8

# In[86]:


#import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
plt.style.use('ggplot')
from matplotlib.pyplot import figure
get_ipython().run_line_magic('matplotlib', 'inline')
pd.options.mode.chained_assignment = None
matplotlib.rcParams['figure.figsize'] = (12,8) # Adjustd the configuration of the plots we will create


# In[87]:


# Read in the data
df = pd.read_csv(r'C:\Users\NOBLE IVAN\Downloads\archive (10)\Car_sales.csv')


# In[88]:


#view the top head table
df.head()


# In[89]:


#view the tail table
df.tail()


# In[90]:


#checking for the shape of the data
df.shape


# In[91]:


#describing the data
df.describe()


# In[93]:


# Checking the data types for the data in the dataset

df.dtypes


# In[118]:


# Change data types of columns (Sales_in_thousands&__year_resale_value)
df = df.fillna(0)  #From Ln17, it is noticed that there are are missing fields in the budget and gross column
                   # so I filled the empty fields with 0 to avoid getting errors when changing data types


df['budget'] = df['Sales_in_thousands'].astype('int64')

df['gross'] = df['__year_resale_value'].astype('int64')


# In[119]:


df


# In[103]:


df.drop_duplicates


# In[39]:


#Displaying null in each row
df.isnull()


# In[44]:


df.isnull().sum()


# In[46]:


#Total number of null values
df.isnull().sum().sum()


# In[48]:


#filling the null values
df2 = df.fillna(value = 0)
df2


# In[49]:


#recount of null values
df2.isnull().sum().sum()


# In[54]:


#Scatter plot to show relationship between manufacturer and sales
plt.scatter(x=df['Sales_in_thousands'], y=df['Manufacturer']) 
plt.title('Manufacturer and Sales')
plt.xlabel('Sales_in_thousands')
plt.ylabel('Manufacturer')
plt.show()


# In[65]:


#Scatter plot to show relationship between manufacturer and sales
plt.scatter(x=df['Horsepower'], y=df['Manufacturer']) 
plt.title('MANUFACTURER WITH THE HIGHEST HORSEPOWER')
plt.xlabel('Horsepower')
plt.ylabel('Manufacturer')
plt.show()


# In[63]:


#lets start looking at correlation
df.corr()


# In[78]:


#High correlation between price in thousands and sales in thousands
correlation_matrix = df.corr(method='pearson')
sns.heatmap(correlation_matrix, annot=True)
plt.title('Price vs Sales')
plt.xlabel('Price_in_thousands')
plt.ylabel('__year_resale_value')
plt.show() 


# In[98]:



#Numerizing the dataset

df_numerized = df

for col_name in df_numerized.columns:
    if(df_numerized[col_name].dtype == 'object'):
        df_numerized[col_name] =  df_numerized[col_name].astype('category')
        df_numerized[col_name] =  df_numerized[col_name].cat.codes
        
df_numerized.head(10)


# In[99]:


df_numerized.corr()


# In[102]:


# Showing the correlation
sns.regplot(x="__year_resale_value", y="Sales_in_thousands", data=df, scatter_kws={"color":"red"}, line_kws={"color":"green"})


# In[104]:


# Looking at the Correlations


# In[105]:


df.corr(method = 'pearson')


# In[106]:


df.corr(method = 'kendall')


# In[110]:


# Comparing the budget and the gross sales using a scatter plot

plt.scatter(x=df['budget'], y=df['gross'])

plt.title('Budget v Gross')

plt.xlabel('Gross')

plt.ylabel('Car Budget')

plt.show


# In[111]:


# Showing the correlation
sns.regplot(x="gross", y="budget", data=df, scatter_kws={"color":"red"}, line_kws={"color":"green"}) 


# In[112]:


#Numerizing the dataset

df_numerized = df

for col_name in df_numerized.columns:
    if(df_numerized[col_name].dtype == 'object'):
        df_numerized[col_name] =  df_numerized[col_name].astype('category')
        df_numerized[col_name] =  df_numerized[col_name].cat.codes
        
df_numerized.head(10)


# In[113]:


# Visualizing the Correlation Matrix

correlation_matrix = df_numerized.corr(method = 'pearson')

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix for Numeric Features")

plt.xlabel("Engine_size")

plt.ylabel("Horsepower")

plt.show()


# In[115]:


df_numerized.corr()


# In[ ]:





# In[ ]:




