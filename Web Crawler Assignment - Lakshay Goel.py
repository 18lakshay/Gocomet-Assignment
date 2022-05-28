#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importing 
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


# In[3]:


dd=pd.DataFrame()


# # Problem 1:

# In[32]:


#scraping product in flipkart 
search=input()
driver=webdriver.Chrome(r'C:\Users\Admin\Desktop\chromedriver.exe')
driver.get("https://flipkart.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div/div/button').click()
driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input').send_keys(search)
driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button').click()
time.sleep(5)

x=driver.find_element_by_class_name('_25b18c')    
price=x.get_attribute('innerHTML').split('>')[1][:7]

link=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a').get_attribute('href')
driver.get(link)
time.sleep(10)
yy=driver.find_elements_by_class_name('_21lJbe')
c=0
for i in yy:
    c+=1
    if(c==2):
            model=i.get_attribute('innerHTML')


# In[ ]:





# In[6]:


dictf={ 'productname':search,
'source':'flipkart',
'price':price,
'category':'smartphone',
'modelno':model,
'link':link}


dd=dd.append(dictf,ignore_index=True)


# In[12]:


#amazon scape
driver.get('https://www.amazon.in/')

driver.find_element_by_id('twotabsearchtextbox').send_keys(search)
driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]').click()

ele=driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[5]/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
linka=ele.get_attribute('href')
ele.click()

window1=driver.window_handles[1]
driver.switch_to.window(window1)
d=driver.find_element_by_class_name('a-price-whole')
price=d.get_attribute('innerHTML')
pricea=price.split('<')[0]


# In[14]:



dicta={ 'productname':search,
'source':'amazon',
'price':pricea,
'category':'smartphone',
'modelno':'nil',
'link':linka}


# In[15]:


dd=dd.append(dicta,ignore_index=True)


# In[18]:





# In[ ]:


dd = dd[['productname', "modelno",'source', 'category', 'link', 'price']]
dd.to_csv('cogomet.csv')


# # Problem 2:
# 

# problem 2.1
# 

# In[19]:


#sort by  in flipkart
int1=int(input("relavance:1, popularity:2, price low to high:3, price high to low :4, newest first :5"))
print(int1)


# In[22]:



driver.get("https://flipkart.com/")
time.sleep(3)
#driver.find_element_by_xpath('/html/body/div[2]/div/div/button').click()
driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input').send_keys(search)
driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button').click()
time.sleep(5)



if (int1==1):
    rel=driver.find_element_by_class_name('_10UF8M')
elif (int1==2):
    rel=driver.find_element_by_class_name('_10UF8M _3LsR0e')
elif (int1==3):
    rel=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[1]/div/div/div[2]/div[3]')
elif (int1==4):
    rel=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[1]/div/div/div[2]/div[4]')
elif (int1==5):
    rel=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[1]/div/div/div[2]/div[5]')
    
rel.click()


# In[24]:


#sort by  in amazon
inta=int(input("relavance:1, avg_customer:2, price low to high:3, price high to low :4, new arrival:5"))
print(inta)


# In[26]:


# amazon
driver.get('https://www.amazon.in/')

driver.find_element_by_id('twotabsearchtextbox').send_keys(search)
driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]').click()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="a-autoid-0-announce"]').click()


if(inta==2):
    linker='//*[@id="s-result-sort-select_3"]'

elif(inta==3):
    linker='//*[@id="s-result-sort-select"]/option[2]'

elif(inta==4):
    linker='//*[@id="s-result-sort-select"]/option[3]'

elif(inta==5):
    linker='//*[@id="s-result-sort-select_2"]'

driver.find_element_by_xpath(linker).click()


# #problem 2.2

# In[29]:


#delivery pincode in flipkart
driver.get("https://flipkart.com/")

driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input').send_keys(search)
driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button').click()
time.sleep(5)

link=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a').get_attribute('href')
driver.get(link)


wait = WebDriverWait(driver, 10)
user= wait.until(EC.presence_of_element_located((By.ID,"pincodeInputId"))) 
ele=driver.find_element_by_id("pincodeInputId")
ele.send_keys('134102')
ele.submit()
value=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[7]/div/div/div[2]/div[1]/ul/div/div[1]/span[1]').get_attribute('innerHTML')
print('in'+" "+value)


# In[34]:


#delivery pincode in amazon
driver.get('https://www.amazon.in/')

driver.find_element_by_id('twotabsearchtextbox').send_keys(search)
driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]').click()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="a-autoid-0-announce"]').click()
driver.find_element_by_xpath('//*[@id="nav-global-location-data-modal-action"]').click()
time.sleep(5)
driver.find_element_by_id('GLUXZipUpdateInput').send_keys('134102')
driver.find_element_by_xpath('//*[@id="GLUXZipUpdate"]/span/input').click()
time.sleep(5)
ele=driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[5]/div/div/div/div/div/div[1]/div/div[2]/div/span/a')
linka=ele.get_attribute('href')
ele.click()

window1=driver.window_handles[1]
driver.switch_to.window(window1)


# In[43]:


del1=driver.find_element_by_xpath('//*[@id="mir-layout-DELIVERY_BLOCK-slot-DELIVERY_MESSAGE"]/b').get_attribute('innerHTML')
del1[2:-2]


# # Problem 3:
# 

# All the given Problem Statements satisfies the Problem 3 conditions.
# All the code written for web crawling project fullfill the condition for the ease of human.It has the following advantages like:
#     1) The project Provides the benefit of easy to reach with no limitations.
#     2) It is also flexible for customers:Ecommerce is not limited to one product or one platform.It has multiple reach with multiple
#                                          Platforms.
#     3) Faster response to buyer/market demands:These days people are more inclining towards online shopping since it saves a huge 
#                                              time due to their hectic schedule and they get variety of products with multiple discount
#                                             offers which they dont get from local stores.
#     4) Easy Comparision of the product cost:The project helps in saving time and efforts by comparing prices on different
#                                             websites which creates a lot of chaos by opening different webapps.
#     5) It saves the cost,time and efforts.
# 

# # Problem 4:
# 

# In[48]:


dd


# In[53]:


#min from amazon and flipkart
min=dd['price'].min()
data=dd[dd['price']==min]
data


# In[ ]:


#add to excel
data.to_csv('minimum.csv')


# # Problem 5:

# In[ ]:


1 delay between requests:
    There are many options when it comes to putting your program to sleep 
    (or insert delays in the program). When performing Selenium, the Sleep function will 
    cause the execution of your code to halt for a specified number of seconds.
    
2 delay time between 2 requests:
    Scraping too fast and too many pages, faster than a human ever can
    
    
    
3 adding proxy to provide ips:
    A proxy is an intermediary between client requests and server responses. 
    Proxies are primarily used to ensure privacy and 
    encapsulation between numerous interactive systems
    
4 do not follow the crawling pattern:
    Following the same pattern while crawling. For example – go through all pages of search results, 
    and go to each result only after grabbing links to them. No human ever does that
    

