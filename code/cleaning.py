from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import regex

driver = webdriver.Firefox(executable_path=r"/Users/naveenvarma/Documents/geckodriver")


# Now as we obtained all the resturant names and ratings data.We now obtaining food item and price from the top picked menu for each resturant from the selected cuisines.
# Asian 
driver.get('https://www.ubereats.com/search?diningMode=PICKUP&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMlN0aWxsd2F0ZXIlMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKSTYtWjZfa0pzWWNSbWRFUUlCYmFrWXclMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBMzYuMTE1NjA3MSUyQyUyMmxvbmdpdHVkZSUyMiUzQS05Ny4wNTgzNjgxJTdE&q=Asian')
# finding the length for the loop.Basically finding number of restuarnts in a page.
q1 = driver.find_elements('xpath','//div/div[1]/div[2]/div[2]/div/div/div')
length_AS = len(q1)
menu_list_AS = []

# creating list of lists.
for i in range(length_AS):
    menu_list_AS.append([])
    
x_AS=0
for i in range(1,length_AS):
    new_AS = driver.find_element('xpath','//div[%d]/div/div/a/h3' % i)
    new_AS.click()
    time.sleep(2)
    menu_AS = driver.find_elements('css selector','div.bx > ul >li:nth-child(1)')
    for a in menu_AS: 
      menu_list_AS[x_AS].append(a.text)
    x_AS=x_AS+1    
    time.sleep(2)
    driver.back()
    time.sleep(2)

# data cleaning - this will repeat for all other choosen cusines
# we got restraunt menu data as single list so now we are spliting the data into single elements in the list for all the restraunts.
menu_list_AS1 = '\n'.join(menu_list_AS[0]).split('\n')
menu_list_AS2 = '\n'.join(menu_list_AS[1]).split('\n')
menu_list_AS3 = '\n'.join(menu_list_AS[2]).split('\n')

# removing unwanted rows - here in this case picked for you string.
menu_list_AS_1 = menu_list_AS1[1:]
menu_list_AS_2 = menu_list_AS2[1:]
menu_list_AS_3 = menu_list_AS3[1:]


length_AS1 = len(menu_list_AS_1)
length_AS2 = len(menu_list_AS_2)
length_AS3  =len(menu_list_AS_3)

newlistAS1=menu_list_AS_1.copy()
newlistAS2=menu_list_AS_2.copy()
newlistAS3=menu_list_AS_3.copy()

# data cleaning removing strings that end with dots in our case they are unwanted description.
for AS1 in range(length_AS1): 
    x_AS1 = menu_list_AS_1[AS1]
    if x_AS1.endswith("."):
        newlistAS1.remove(x_AS1) 

for AS2 in range(length_AS2): 
    x_AS2 = menu_list_AS_2[AS2]
    if x_AS2.endswith("."):
        newlistAS2.remove(x_AS2) 

for AS3 in range(length_AS3): 
    x_AS3 = menu_list_AS_3[AS3]
    if x_AS3.endswith("."):
        newlistAS3.remove(x_AS3) 

# data transformation _repeats same for other cusines as well.
itemlistAS1 = pd.DataFrame(newlistAS1[::2])
pricelistAS1= pd.DataFrame(newlistAS1[1::2])
itemlistAS2 = pd.DataFrame(newlistAS2[::2])
pricelistAS2= pd.DataFrame(newlistAS2[1::2])
itemlistAS3 = pd.DataFrame(newlistAS3[::2])
pricelistAS3= pd.DataFrame(newlistAS3[1::2])
dfAS1 = pd.concat([itemlistAS1,pricelistAS1], axis=1)
dfAS1.columns=['Item','Price']
dfAS2 = pd.concat([itemlistAS2,pricelistAS2], axis=1)
dfAS2.columns=['Item','Price']
dfAS3 = pd.concat([itemlistAS3,pricelistAS3], axis=1)
dfAS3.columns=['Item','Price']

dfAS1.to_csv(r'/Users/naveenvarma/Desktop/PDS/project/stillwater/Asian/1.csv',sep='\t',encoding='utf-8')
dfAS2.to_csv(r'/Users/naveenvarma/Desktop/PDS/project/stillwater/Asian/2.csv',sep='\t',encoding='utf-8')
dfAS3.to_csv(r'/Users/naveenvarma/Desktop/PDS/project/stillwater/Asian/3.csv',sep='\t',encoding='utf-8')


# Bakery 
driver.get('https://www.ubereats.com/search?diningMode=PICKUP&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMlN0aWxsd2F0ZXIlMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKSTYtWjZfa0pzWWNSbWRFUUlCYmFrWXclMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBMzYuMTE1NjA3MSUyQyUyMmxvbmdpdHVkZSUyMiUzQS05Ny4wNTgzNjgxJTdE&q=Bakery')
# finding the length for the loop.Basically finding number of restuarnts in a page.
q1 = driver.find_elements('xpath','//div/div[1]/div[2]/div[2]/div/div/div')
length_BK = len(q1)
menu_list_BK = []

# creating list of lists.
for i in range(length_BK):
    menu_list_BK.append([])
    
x_BK=0
for i in range(1,length_BK):
    new_BK = driver.find_element('xpath','//div[%d]/div/div/a/h3' % i)
    new_BK.click()
    time.sleep(2)
    menu_BK = driver.find_elements('css selector','div.bx > ul >li:nth-child(1)')
    for a in menu_BK: 
      menu_list_BK[x_BK].append(a.text)
    x_BK=x_BK+1    
    time.sleep(2)
    driver.back()
    time.sleep(2)

# we got restraunt menu data as single list so now we are spliting the data into single elements in the list for all the restraunts.
menu_list_BK1 = '\n'.join(menu_list_BK[0]).split('\n')
menu_list_BK2 = '\n'.join(menu_list_BK[1]).split('\n')
menu_list_BK3 = '\n'.join(menu_list_BK[2]).split('\n')

# removing unwanted rows - here in this case picked for you string.
menu_list_BK_1 = menu_list_BK1[1:]
menu_list_BK_2 = menu_list_BK2[1:]
menu_list_BK_3 = menu_list_BK3[1:]


length_BK1 = len(menu_list_BK_1)
length_BK2 = len(menu_list_BK_2)
length_BK3  =len(menu_list_BK_3)

newlistBK1=menu_list_BK_1.copy()
newlistBK2=menu_list_BK_2.copy()
newlistBK3=menu_list_BK_3.copy()

for BK1 in range(length_BK1): 
    x_BK1 = menu_list_BK_1[BK1]
    if x_BK1.endswith("."):
        newlistBK1.remove(x_BK1) 

for BK2 in range(length_BK2): 
    x_BK2 = menu_list_BK_2[BK2]
    if x_BK2.endswith("."):
        newlistBK2.remove(x_BK2) 

for BK3 in range(length_BK3): 
    x_BK3 = menu_list_BK_3[BK3]
    if x_BK3.endswith("."):
        newlistBK3.remove(x_BK3) 


itemlistBK1 = pd.DataFrame(newlistBK1[::2])
pricelistBK1= pd.DataFrame(newlistBK1[1::2])
itemlistBK2 = pd.DataFrame(newlistBK2[::2])
pricelistBK2= pd.DataFrame(newlistBK2[1::2])
itemlistBK3 = pd.DataFrame(newlistBK3[::2])
pricelistBK3= pd.DataFrame(newlistBK3[1::2])
dfBK1 = pd.concat([itemlistBK1,pricelistBK1], axis=1)
dfBK1.columns=['Item','Price']
dfBK2 = pd.concat([itemlistBK2,pricelistBK2], axis=1)
dfBK2.columns=['Item','Price']
dfBK3 = pd.concat([itemlistBK3,pricelistBK3], axis=1)
dfBK3.columns=['Item','Price']

dfBK1.to_csv(r'/Users/naveenvarma/Desktop/PDS/project/stillwater/Bakery/1.csv',sep='\t',encoding='utf-8')
dfBK2.to_csv(r'/Users/naveenvarma/Desktop/PDS/project/stillwater/Bakery/2.csv',sep='\t',encoding='utf-8')
dfBK3.to_csv(r'/Users/naveenvarma/Desktop/PDS/project/stillwater/Bakery/3.csv',sep='\t',encoding='utf-8')

# Chinese
driver.get('https://www.ubereats.com/search?diningMode=PICKUP&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMlN0aWxsd2F0ZXIlMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKSTYtWjZfa0pzWWNSbWRFUUlCYmFrWXclMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBMzYuMTE1NjA3MSUyQyUyMmxvbmdpdHVkZSUyMiUzQS05Ny4wNTgzNjgxJTdE&q=Chinese')
# finding the length for the loop.Basically finding number of restuarnts in a page.
q1 = driver.find_elements('xpath','//div/div[1]/div[2]/div[2]/div/div/div')
length_CH = len(q1)
menu_list_CH = []

# creating list of lists.
for i in range(length_CH):
    menu_list_CH.append([])
    
x_CH=0
for i in range(1,length_CH):
    new_CH = driver.find_element('xpath','//div[%d]/div/div/a/h3' % i)
    new_CH.click()
    time.sleep(2)
    menu_CH = driver.find_elements('css selector','div.bx > ul >li:nth-child(1)')
    for a in menu_CH: 
      menu_list_CH[x_CH].append(a.text)
    x_CH=x_CH+1    
    time.sleep(2)
    driver.back()
    time.sleep(2)

# we got restraunt menu data as single list so now we are spliting the data into single elements in the list for all the restraunts.
menu_list_CH1 = '\n'.join(menu_list_CH[0]).split('\n')
menu_list_CH2 = '\n'.join(menu_list_CH[1]).split('\n')


# removing unwanted rows - here in this case picked for you string.
menu_list_CH_1 = menu_list_CH1[1:]
menu_list_CH_2 = menu_list_CH2[1:]



length_CH1 = len(menu_list_CH_1)
length_CH2 = len(menu_list_CH_2)


newlistCH1=menu_list_CH_1.copy()
newlistCH2=menu_list_CH_2.copy()


for CH1 in range(length_CH1): 
    x_CH1 = menu_list_CH_1[CH1]
    if x_CH1.endswith("."):
        newlistCH1.remove(x_CH1) 

for CH2 in range(length_CH2): 
    x_CH2 = menu_list_CH_2[CH2]
    if x_CH2.endswith("."):
        newlistCH2.remove(x_CH2) 


itemlistCH1 = pd.DataFrame(newlistCH1[::2])
pricelistCH1= pd.DataFrame(newlistCH1[1::2])
itemlistCH2 = pd.DataFrame(newlistCH2[::2])
pricelistCH2= pd.DataFrame(newlistCH2[1::2])

dfCH1 = pd.concat([itemlistCH1,pricelistCH1], axis=1)
dfCH1.columns=['Item','Price']
dfCH2 = pd.concat([itemlistCH2,pricelistCH2], axis=1)
dfCH2.columns=['Item','Price']


dfCH1.to_csv(r'/Users/naveenvarma/Desktop/PDS/project/stillwater/Chinese/1.csv',sep='\t',encoding='utf-8')
dfCH2.to_csv(r'/Users/naveenvarma/Desktop/PDS/project/stillwater/Chinese/2.csv',sep='\t',encoding='utf-8')

# Mexican 
driver.get('https://www.ubereats.com/search?diningMode=PICKUP&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMlN0aWxsd2F0ZXIlMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKSTYtWjZfa0pzWWNSbWRFUUlCYmFrWXclMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBMzYuMTE1NjA3MSUyQyUyMmxvbmdpdHVkZSUyMiUzQS05Ny4wNTgzNjgxJTdE&q=Mexican')
# finding the length for the loop.Basically finding number of restuarnts in a page.
q1 = driver.find_elements('xpath','//div/div[1]/div[2]/div[2]/div/div/div')
length_MX = len(q1)
menu_list_MX = []

# creating list of lists.
for i in range(length_MX):
    menu_list_MX.append([])
    
x_MX=0
for i in range(1,length_MX):
    new_MX = driver.find_element('xpath','//div[%d]/div/div/a/h3' % i)
    new_MX.click()
    time.sleep(2)
    menu_MX = driver.find_elements('css selector','div.bx > ul >li:nth-child(1)')
    for a in menu_MX: 
      menu_list_MX[x_MX].append(a.text)
    x_MX=x_MX+1    
    time.sleep(2)
    driver.back()
    time.sleep(2)

# we got restraunt menu data as single list so now we are spliting the data into single elements in the list for all the restraunts.
menu_list_MX1 = '\n'.join(menu_list_MX[0]).split('\n')
menu_list_MX2 = '\n'.join(menu_list_MX[1]).split('\n')
menu_list_MX3 = '\n'.join(menu_list_MX[2]).split('\n')
menu_list_MX4 = '\n'.join(menu_list_MX[3]).split('\n')
menu_list_MX5 = '\n'.join(menu_list_MX[4]).split('\n')

# removing unwanted rows - here in this case picked for you string.
menu_list_MX_1 = menu_list_MX1[1:]
menu_list_MX_2 = menu_list_MX2[1:]
menu_list_MX_3 = menu_list_MX3[1:]
menu_list_MX_4 = menu_list_MX4[1:]
menu_list_MX_5 = menu_list_MX5[1:]


length_MX1 = len(menu_list_MX_1)
length_MX2 = len(menu_list_MX_2)
length_MX3  =len(menu_list_MX_3)
length_MX4 = len(menu_list_MX_4)
length_MX5  =len(menu_list_MX_5)

newlistMX1=menu_list_MX_1.copy()
newlistMX2=menu_list_MX_2.copy()
newlistMX3=menu_list_MX_3.copy()
newlistMX4=menu_list_MX_4.copy()
newlistMX5=menu_list_MX_5.copy()

for MX1 in range(length_MX1): 
    x_MX1 = menu_list_MX_1[MX1]
    if x_MX1.endswith("."):
        newlistMX1.remove(x_MX1) 

for MX2 in range(length_MX2): 
    x_MX2 = menu_list_MX_2[MX2]
    if x_MX2.endswith("."):
        newlistMX2.remove(x_MX2) 

for MX3 in range(length_MX3): 
    x_MX3 = menu_list_MX_3[MX3]
    if x_MX3.endswith("."):
        newlistMX3.remove(x_MX3)

for MX4 in range(length_MX4): 
    x_MX4 = menu_list_MX_4[MX4]
    if x_MX4.endswith("."):
        newlistMX4.remove(x_MX4) 

for MX5 in range(length_MX5): 
    x_MX5 = menu_list_MX_5[MX5]
    if x_MX5.endswith("."):
        newlistMX5.remove(x_MX5) 

itemlistMX1 = pd.DataFrame(newlistMX1[::2])
pricelistMX1= pd.DataFrame(newlistMX1[1::2])
itemlistMX2 = pd.DataFrame(newlistMX2[::2])
pricelistMX2= pd.DataFrame(newlistMX2[1::2])
itemlistMX3 = pd.DataFrame(newlistMX3[::2])
pricelistMX3= pd.DataFrame(newlistMX3[1::2])
itemlistMX4 = pd.DataFrame(newlistMX4[::2])
pricelistMX4= pd.DataFrame(newlistMX4[1::2])
itemlistMX5 = pd.DataFrame(newlistMX5[::2])
pricelistMX5= pd.DataFrame(newlistMX5[1::2])

dfMX1 = pd.concat([itemlistMX1,pricelistMX1], axis=1)
dfMX1.columns=['Item','Price']
dfMX2 = pd.concat([itemlistMX2,pricelistMX2], axis=1)
dfMX2.columns=['Item','Price']
dfMX3 = pd.concat([itemlistMX3,pricelistMX3], axis=1)
dfMX3.columns=['Item','Price']
dfMX4 = pd.concat([itemlistMX4,pricelistMX4], axis=1)
dfMX4.columns=['Item','Price']
dfMX5 = pd.concat([itemlistMX5,pricelistMX5], axis=1)
dfMX5.columns=['Item','Price']

dfMX1.to_csv(r'/Users/naveenvarma/Desktop/PDS/project/stillwater/Mexican/1.csv',sep='\t',encoding='utf-8')
dfMX2.to_csv(r'/Users/naveenvarma/Desktop/PDS/project/stillwater/Mexican/2.csv',sep='\t',encoding='utf-8')
dfMX3.to_csv(r'/Users/naveenvarma/Desktop/PDS/project/stillwater/Mexican/3.csv',sep='\t',encoding='utf-8')
dfMX4.to_csv(r'/Users/naveenvarma/Desktop/PDS/project/stillwater/Mexican/4.csv',sep='\t',encoding='utf-8')
dfMX5.to_csv(r'/Users/naveenvarma/Desktop/PDS/project/stillwater/Mexican/5.csv',sep='\t',encoding='utf-8')