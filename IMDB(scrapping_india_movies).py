# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 06:26:39 2018

@author: vishal
"""

url = 'https://www.imdb.com/india/top-rated-indian-movies/?sort=rk,asc&mode=simple&page=1'
from selenium import webdriver
driver =  webdriver.Chrome(r"C:\Users\visha\chromedriver")
driver.get(url)

#for storing all titles in a list
titles = driver.find_elements_by_class_name('titleColumn')
newtitles = []
for i in titles:
    j = i.text
    newtitles.append(j)

#looping for ratings
string_title = '//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[1]/td[3]/strong' 
ratings = []
for er in range(1,len(titles)+1):
    up_rate = string_title[0:-15] +str(er)+ string_title[-14:]
    k = driver.find_element_by_xpath(up_rate)
    ratings.append(k)
    
    
newratings = []
for k in ratings:
    q = k.text
    newratings.append(q)

#we made two updated list , newtitles and newratings

#updated = {}
#for i in range(0,249):
#    updated[newtitles[i]] = newratings[i]
#    print(updated)

'''we came to conclusion later that to access all films in rating wise
it would be great if we stick with list as dictionariesa re orderless '''    

list1 = []
for i in range(0,249):
    k = newtitles[i] + ' : ' + newratings[i]
    list1.append(k)


a = 1
while a != 0:
    test1 = int(input('Enter a number between 1-250 to check rating of a movie: '))
    if test1>=1 and test1<=250:
        print(list1[test1-1])
    else:
        print('wrong input')
    a = input("Enter 'done' to stop or press enter to continue: ")
    if a == 'done':
        break
