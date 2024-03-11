
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import regex

driver = webdriver.Firefox(executable_path=r"/Users/naveenvarma/Documents/geckodriver")
# navigating through the pages until my reqired page for sraping the data is found.
ubereats_url = 'https://www.ubereats.com/feed?diningMode=DELIVERY&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMk5ldyUyMFlvcmslMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKT3dnXzA2VlB3b2tSWXY1MzRRYVBDOGclMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBNDAuNzEzMzE2NyUyQyUyMmxvbmdpdHVkZSUyMiUzQS03NC4wMDcwNCU3RA%3D%3D&sf=JTVCJTdCJTIydXVpZCUyMiUzQSUyMjFjN2NmN2VmLTczMGYtNDMxZi05MDcyLTI2YmMzOWY3YzAyMSUyMiUyQyUyMm9wdGlvbnMlMjIlM0ElNUIlN0IlMjJ1dWlkJTIyJTNBJTIyNGM3Y2Y3ZWYtNzMwZi00MzFmLTkwNzItMjZiYzM5ZjdjMDIzJTIyJTdEJTVEJTdEJTJDJTdCJTIydXVpZCUyMiUzQSUyMjJjN2NmN2VmLTczMGYtNDMxZi05MDcyLTQ2YmMzOWY3YzAyMSUyMiUyQyUyMm9wdGlvbnMlMjIlM0ElNUIlN0IlMjJ1dWlkJTIyJTNBJTIyMmM3Y2Y3ZWYtNzMwZi00MzFmLTkwNzItMjZiYzM5ZjdjMDMzJTIyJTdEJTVEJTdEJTVE'
driver.get(ubereats_url)
time.sleep(2)
# going to pickup mode.
driver.get('https://www.ubereats.com/feed?diningMode=PICKUP&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMk9rbGFob21hJTIwQ2l0eSUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUpnZEw0ZmxTS3JZY1JuVHBQMFhRU29qTSUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0EzNS40Njc1NjAyJTJDJTIybG9uZ2l0dWRlJTIyJTNBLTk3LjUxNjQyNzYlN0Q%3D&ps=1')
time.sleep(2)
driver.get('https://www.ubereats.com/feed?diningMode=PICKUP&mod=deliveryDetails&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMk9rbGFob21hJTIwQ2l0eSUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUpnZEw0ZmxTS3JZY1JuVHBQMFhRU29qTSUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0EzNS40Njc1NjAyJTJDJTIybG9uZ2l0dWRlJTIyJTNBLTk3LjUxNjQyNzYlN0Q%3D&ps=1')
time.sleep(2)
driver.get('https://www.ubereats.com/feed?diningMode=PICKUP&mod=locationManager&modctx=feed&next=%2Ffeed%3FdiningMode%3DPICKUP%26pl%3DJTdCJTIyYWRkcmVzcyUyMiUzQSUyMlN0aWxsd2F0ZXIlMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKSTYtWjZfa0pzWWNSbWRFUUlCYmFrWXclMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBMzYuMTE1NjA3MSUyQyUyMmxvbmdpdHVkZSUyMiUzQS05Ny4wNTgzNjgxJTdE%26ps%3D1%26sf%3DJTVCJTdCJTIydXVpZCUyMiUzQSUyMjFjN2NmN2VmLTczMGYtNDMxZi05MDcyLTI2YmMzOWY3YzAyMSUyMiUyQyUyMm9wdGlvbnMlMjIlM0ElNUIlN0IlMjJ1dWlkJTIyJTNBJTIyNGM3Y2Y3ZWYtNzMwZi00MzFmLTkwNzItMjZiYzM5ZjdjMDIzJTIyJTdEJTVEJTdEJTVE&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMlN0aWxsd2F0ZXIlMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKSTYtWjZfa0pzWWNSbWRFUUlCYmFrWXclMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBMzYuMTE1NjA3MSUyQyUyMmxvbmdpdHVkZSUyMiUzQS05Ny4wNTgzNjgxJTdE&ps=1&sf=JTVCJTdCJTIydXVpZCUyMiUzQSUyMjFjN2NmN2VmLTczMGYtNDMxZi05MDcyLTI2YmMzOWY3YzAyMSUyMiUyQyUyMm9wdGlvbnMlMjIlM0ElNUIlN0IlMjJ1dWlkJTIyJTNBJTIyNGM3Y2Y3ZWYtNzMwZi00MzFmLTkwNzItMjZiYzM5ZjdjMDIzJTIyJTdEJTVEJTdEJTVE')
time.sleep(2)
# finding the input text box to enter the location details.
uber_location = driver.find_element('xpath','//*[@id="location-typeahead-location-manager-input"]')
location="Stillwater OK,USA"
new = uber_location.find_element('xpath',('//*[@id="location-typeahead-location-manager-input"]')).send_keys(location+Keys.ENTER)
time.sleep(2)
driver.get('https://www.ubereats.com/feed?diningMode=PICKUP&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMlN0aWxsd2F0ZXIlMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKSTYtWjZfa0pzWWNSbWRFUUlCYmFrWXclMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBMzYuMTE1NjA3MSUyQyUyMmxvbmdpdHVkZSUyMiUzQS05Ny4wNTgzNjgxJTdE&ps=1&sf=JTVCJTdCJTIydXVpZCUyMiUzQSUyMjFjN2NmN2VmLTczMGYtNDMxZi05MDcyLTI2YmMzOWY3YzAyMSUyMiUyQyUyMm9wdGlvbnMlMjIlM0ElNUIlN0IlMjJ1dWlkJTIyJTNBJTIyNGM3Y2Y3ZWYtNzMwZi00MzFmLTkwNzItMjZiYzM5ZjdjMDIzJTIyJTdEJTVEJTdEJTVE')
time.sleep(2)
driver.maximize_window()
w=0
e=0
p=0

# intiating  multiple lists.
header_names=[]
type_cusine_name = []
type_cusine_rating = []
header = driver.find_elements('xpath','//div/li/a/span')
for y in header:
    header_names.append(y.text) 

# creating lists of lists.
for k in range(14):
    type_cusine_name.append([])
    type_cusine_rating.append([])


for l in range(1,27,2):

    if l > 15:
        # to scroll the element into the view, because i need to scroll the panel horizantally until my reqired element is visible.
        cusine2 = driver.find_element('xpath','//*[@id="main-content"]/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div[27]/li/a')
        driver.execute_script("arguments[0].scrollIntoView();",cusine2)
        time.sleep(3)
        # click the required element
        cusine1 = driver.find_element('xpath','//*[@id="main-content"]/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div[%d]/li/a' %l)
        cusine1.click()
        time.sleep(6)
    else:    
        cusine1 = driver.find_element('xpath','//*[@id="main-content"]/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div[%d]/li/a' %l)
        cusine1.click()
        time.sleep(6)

    name = driver.find_elements('css selector','a > h3')
    # storing names of the resturants acccording to their cusines.
    for i in name :
        type_cusine_name[w].append(i.text) 
    time.sleep(2)
    w=w+1

    # storing the ratings of the resturants according to the their cusines.
    rating = driver.find_elements('xpath',' //div[3]/span[2]')
    for j in rating :
        type_cusine_rating[e].append(j.text)
    time.sleep(2)
    e=e+1

    driver.get('https://www.ubereats.com/feed?diningMode=PICKUP&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMlN0aWxsd2F0ZXIlMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKSTYtWjZfa0pzWWNSbWRFUUlCYmFrWXclMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBMzYuMTE1NjA3MSUyQyUyMmxvbmdpdHVkZSUyMiUzQS05Ny4wNTgzNjgxJTdE&ps=1&sf=JTVCJTdCJTIydXVpZCUyMiUzQSUyMjFjN2NmN2VmLTczMGYtNDMxZi05MDcyLTI2YmMzOWY3YzAyMSUyMiUyQyUyMm9wdGlvbnMlMjIlM0ElNUIlN0IlMjJ1dWlkJTIyJTNBJTIyNGM3Y2Y3ZWYtNzMwZi00MzFmLTkwNzItMjZiYzM5ZjdjMDIzJTIyJTdEJTVEJTdEJTVE')
    # now i am moving back to main page as kept this in the loop first it goes into a single cusine and from there it stores there names and ratings of that particular cusines and comes back to our main page.
    # next it goes to the new cusine and stores the reqired data this process continues till the all the cusine data is stored.
    time.sleep(2)
    driver.maximize_window()   

print(type_cusine_name)
print(type_cusine_rating)    
df1 = pd.DataFrame(type_cusine_name)
df_n = df1.transpose()
df_n.columns = [header_names[0],header_names[1],header_names[2],header_names[3],header_names[4],header_names[5],header_names[6],header_names[7],header_names[8],header_names[9],header_names[10],header_names[11],header_names[12],header_names[13]]
df_n.to_csv(r'/Users/naveenvarma/Desktop/PDS/project/data/stillwater/stillwater_cusines.csv',sep='\t',encoding='utf-8')


df2 = pd.DataFrame(type_cusine_rating)
df_r = df2.transpose()
df_r.columns = [header_names[0],header_names[1],header_names[2],header_names[3],header_names[4],header_names[5],header_names[6],header_names[7],header_names[8],header_names[9],header_names[10],header_names[11],header_names[12],header_names[13]]
df_r.to_csv(r'/Users/naveenvarma/Desktop/PDS/project/data/stillwater/stillwater_ratings.csv',sep='\t',encoding='utf-8')

# data-reduction now dropping the unwanted columns for both names and ratings 
df_n1 = pd.read_csv (r'/Users/naveenvarma/Desktop/PDS/project/stillwater/stillwater_cusines.csv',sep='\t')
df_n2 = df_n1.drop(columns=[header_names[0],header_names[1],header_names[3],header_names[7],header_names[8],header_names[9],header_names[10],header_names[11],header_names[12],header_names[13]],axis=1)
df_n2.to_csv(r'/Users/naveenvarma/Desktop/PDS/project/data/stillwater/filtered_stillwater_cusines.csv',sep='\t',encoding='utf-8')

df_r1 = pd.read_csv (r'/Users/naveenvarma/Desktop/PDS/project/stillwater/stillwater_ratings.csv',sep='\t')
df_r2 = df_r1.drop(columns=[header_names[0],header_names[1],header_names[3],header_names[7],header_names[8],header_names[9],header_names[10],header_names[11],header_names[12],header_names[13]],axis=1)
df_r2.to_csv(r'/Users/naveenvarma/Desktop/PDS/project/data/stillwater/filtered_stillwater_ratings.csv',sep='\t',encoding='utf-8') 








