from tkinter import *
import tkinterweb
from datetime import datetime  # date and day module
from bs4 import BeautifulSoup
import requests
try:
    from googlesearch import search
except:
    print("error occured while import")
from PIL import ImageTk, Image
# from urllib.request import Request, urlopen


today = datetime.now()  # getting today's date and day details
listofmonths = ["January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"]
# string of date in desired format
date_details = today.strftime(
    "%A")+", "+str(today.day)+" "+listofmonths[today.month-1]+" "+str(today.year)


list_of_days = []
list_of_links = []
text_in_wiki = []


def web_scraping():

    global list_of_days, text_in_wiki, list_of_links
    text_in_wiki = []
    list_of_days = []
    list_of_links = []

    ###### un######

    # # date and month to search in un website
    # date_for_un = str(26)+" " +listofmonths[0][:3]
    # print(date_for_un)
    # html_un = requests.get("https://www.un.org/en/observances/list-days-weeks",
    #                        headers={'User-Agent': 'Mozilla/5.0'}).text  # making html request
    # parsed_un = BeautifulSoup(html_un, 'html.parser')  # parsing the html code
    # # storing all the events as this div, class_ contains info of all events
    # all_events = parsed_un.find('div', class_='view-content')
    # # for i in all_events:
    # #     print(i)  
    # # print(all_events)

    # for event in all_events:  # accessing each event in all_events
    #     if date_for_un in event.text:  # checking for the date in the text of that event
    #         print(event)
    #         # first field content is for title so just find but not find_all
    #         html_title = event.find('span', class_="field-content")
    #         # in that title we have both text of the event
    #         text_of_title_from_un = html_title.text
    #         print(text_of_title_from_un)
    #         list_of_days.append(text_of_title_from_un)
   

    # ####### byju's#########

    # byjus_html = requests.get(
    #     "https://byjus.com/free-ias-prep/important-national-international-days-dates-for-upsc-prelims/").text
    # parsed_byjus = BeautifulSoup(byjus_html, 'html.parser')
    # table = parsed_byjus.find_all('table', class_='table table-bordered')
    # all_rows = table[1].find_all('tr')
    # # print(all_rows)
    # for each_row in all_rows[2:]:
    #     if str(21) in each_row.text and listofmonths[3-1][:3] in each_row.text:
    #         print(each_row.text)
    #         list_of_days.extend((each_row.text.split('\n'))[2:-1])
    #         break


    # for i in list_of_days:
    #     for j in search(i, tld="co.in", num=1, stop=1):
    #         list_of_links.append(j)
    # print(list_of_links)
    ####### jagranjosh#######

    # jj_yearwise_html = requests.get(
    #     "https://www.jagranjosh.com/general-knowledge/national-and-international-important-days-1561379458-1").text
    # parsed_yearwise_jj = BeautifulSoup(jj_yearwise_html, 'html.parser')
    # all_a_tags_jj = parsed_yearwise_jj.find_all("a")

    # for each_a_tag in all_a_tags_jj:
    #     if 'gk' not in each_a_tag['href'] and 'important-days' in each_a_tag['href'] and listofmonths[int(monthfromentry.get())-1].lower() in each_a_tag['href']:
    #         link_of_required_month = each_a_tag['href']

    # jj_monthwise_html = requests.get(link_of_required_month).text
    # parsed_monthwise_jj = BeautifulSoup(jj_monthwise_html, "html.parser")

    # table = parsed_monthwise_jj.find('table')
    # all_rows = table.find_all('tr')

    # for each_row in all_rows[3:]:
    # #     if listofmonths[int(monthfromentry.get())-1] in each_row.text and datefromentry.get() in each_row.text:
    # #         list_of_days.append((each_row.text.split('\n'))[2][1:])
            
    # # ######### festivals##########

    # html_festivals = requests.get(
    #     "https://traveltriangle.com/blog/famous-festivals-of-india/", headers={'User-Agent': 'Mozilla/5.0'}).text
    # parsed_festivals = BeautifulSoup(html_festivals, 'html.parser')
    # table = parsed_festivals.find('table')

    # all_rows = table.find_all('tr')

    # for each_row in all_rows[1:]:
    #     if str(20) in each_row.text and listofmonths[8-1] in each_row.text:
    #         list_of_days.append((each_row.text.split('\n'))[2])
    #         break

    # print(list_of_days) 

    ####### jagranjosh#######

    # jj_yearwise_html = requests.get(
    #     "https://www.jagranjosh.com/general-knowledge/national-and-international-important-days-1561379458-1").text
    # parsed_yearwise_jj = BeautifulSoup(jj_yearwise_html, 'html.parser')
    # all_a_tags_jj = parsed_yearwise_jj.find_all("a")

    # for each_a_tag in all_a_tags_jj:
    #     if 'gk' not in each_a_tag['href'] and 'important-days' in each_a_tag['href'] and listofmonths[int(monthfromentry.get())-1].lower() in each_a_tag['href']:
    #         link_of_required_month = each_a_tag['href']

    # jj_monthwise_html = requests.get(link_of_required_month).text
    # parsed_monthwise_jj = BeautifulSoup(jj_monthwise_html, "html.parser")

    # table = parsed_monthwise_jj.find('table')
    # all_rows = table.find_all('tr')

    for each_row in all_rows[3:]:
        if listofmonths[int(monthfromentry.get())-1] in each_row.text and datefromentry.get() in each_row.text:
            list_of_days.append((each_row.text.split('\n'))[2][1:])

web_scraping()  

###########################################################