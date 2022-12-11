#!/usr/bin/env python
# coding: utf-8

# """Pandas is an open source library that was primarily developed for the purpose of dealing with relational or 
# labelled data in a straightforward and user-friendly manner."""

# In[ ]:


"""Pandas is an open source library that was primarily developed for the purpose of dealing with relational or labelled data in a straightforward and user-friendly manner."""
import pandas as pd


# In[ ]:


from matplotlib import pyplot as mtp_plot
"""Matplotlib is a library for the Python programming language that enables users to create visualisations that may be either static, animated, or
interactive. Matplotlib enables users to do tasks that range from simple to complex. Develop stories in a format that is appropriate for publishing.
Develop zoomable, pagable, and updatable graphs that may be interactively created."""


# In[ ]:


# create function 
def read_df(Data_filename):
    data=pd.read_csv(Data_filename) # read dataset 
    return data


# In[ ]:


Data_filename="/content/audi (1).csv" # dataset path 
audi_car_data=read_df(Data_filename)
audi_car_data.head(5) # showing data 


# #Comparison of audi car Price and tax 

# In[ ]:


df=audi_car_data.pivot_table(index=['year'], values=['price','tax'])  
mtp_plot.figure(figsize = (20,8)) # set figure size 
mtp_plot.plot(df.head(100)) # set datasaet  
mtp_plot.legend(['Price','Tax'])  # set lengend 
mtp_plot.xlabel('Year')
#  set  x axis  year 
mtp_plot.ylabel('Comparison ')
# set  y axis price 
mtp_plot.title('Comparison of Audi car Price and Tax ') 
# set  title name Comparison of Audi car Price and Tax
mtp_plot.show() # showing graph 


# #audi car price with model name

# In[ ]:


df1=audi_car_data.pivot_table(index=['model'], values=['price']) 
# set figure size
mtp_plot.rcParams['figure.figsize']=(20,7) 
df3= df1.head(20) # set datset 
df3.plot.bar(color=['cyan']) # set color name 
mtp_plot.xlabel('Car Model Name')
# set x axis  Car Model Name
mtp_plot.ylabel('Price')
# set y axis  price 
mtp_plot.title('Audi car Price with Model name ') 
# set title name Audi car Price with Model name
mtp_plot.show() ;


# #Comparison of mileage and price 

# In[ ]:


# plotting figure 
mtp_plot.rcParams['figure.figsize']=(15,7) 
# set font_size.
mtp_plot.rcParams.update({'font.size': 10})  
# set font size 
audi_car_data.plot(kind="scatter", x='mileage', y='price', alpha=0.5) 
mtp_plot.xlabel("Mileage") 
 # set x axis Mileage
mtp_plot.ylabel("Price") 
#  set y axis Price
mtp_plot.title("Comparison of Mileage and Price  ") 
# set title name Comparison of Mileage and Price 
plmtp_plotot_mat.show() 


# #Comparison of tax and price

# In[ ]:


# set figure size.
mtp_plot.rcParams['figure.figsize']=(14,7) 
# set font_size.
mtp_plot.rcParams.update({'font.size': 10}) 

audi_car_data.plot(kind="scatter", x='tax', y='price', alpha=0.5) 

mtp_plot.xlabel("Tax") 
# set x axis tax 
mtp_plot.ylabel("Price") 
#  set y axis price 
mtp_plot.title("Comparison of Tax and Price ") 
# set title name Comparison of Tax and Price
mtp_plot.show() 


# ##**we are firslty importing libraries pd and matp pd  for data manipulation and matp for data visualization then we are reading our dataset by pandas read csv method then we are plotting graph of audi car price and tax then we are plotting bar plot graph of model name and car price and scatter plot of tax and price we are plotting these graph with the help of  matplotlib .**

# In[ ]:




