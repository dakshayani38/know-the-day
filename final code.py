from tkinter import *
import tkinterweb
from datetime import datetime  # date and day module
from bs4 import BeautifulSoup
import requests
from googlesearch import search
from PIL import ImageTk, Image

##########################################################

today = datetime.now()  # getting today's date and day details
listofmonths = ["January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"]
# string of date in desired format
date_details = today.strftime(
    "%A")+", "+str(today.day)+" "+listofmonths[today.month-1]+" "+str(today.year)

##########################################################


def after_clicking_specialday_button(event):

    title_frame_listbox.delete(0, END)

    event_text = event.widget.cget("text")
    title_frame_listbox.insert(0, event_text)
    web_frame.load_website(list_of_links[list_of_days.index(event_text)])


##########################################################


list_of_days = []
list_of_links = []
text_in_wiki = []


def web_scraping():

    global list_of_days, text_in_wiki, list_of_links
    text_in_wiki = []
    list_of_days = []
    list_of_links = []

    ###### un######

    # date and month to search in un website
    date_for_un = str(datefromentry.get())+" " + \
        listofmonths[int(monthfromentry.get())-1][:3]
    # print(date_for_un)
    html_un = requests.get("https://www.un.org/en/observances/list-days-weeks",
                           headers={'User-Agent': 'Mozilla/5.0'}).text  # making html request
    parsed_un = BeautifulSoup(html_un, 'html.parser')  # parsing the html code
    # storing all the events as this div, class_ contains info of all events
    all_events = parsed_un.find('div', class_='view-content')

    for event in all_events:  # accessing each event in all_events
        if date_for_un in event.text:  # checking for the date in the text of that event
            # first field content is for title so just find but not find_all
            html_title = event.find('span', class_="field-content")
            # in that title we have both text of the event
            text_of_title_from_un = html_title.text
            list_of_days.append(text_of_title_from_un)
    # print(list_of_days)

    

    wikilink = "https://en.wikipedia.org/wiki/" + \
        listofmonths[int(monthfromentry.get())-1]+"_"+str(datefromentry.get())
    html_wiki = requests.get(
        wikilink, headers={'User-Agent': 'Mozilla/5.0'}).text  # making html request
    parsed_wiki = BeautifulSoup(
        html_wiki, 'html.parser')  # parsing the html code
    # all_ul_tags = parsed_wiki.find_all('ul')  # getting all the 'ul' tags
    parsed_div=parsed_wiki.find("div",class_="mw-content-ltr mw-parser-output")
    all_ul_tags = parsed_div.find_all('ul')  # getting all the 'ul' tags
    temp_text_in_wiki = []
    i = 1
    for events_yearwise in all_ul_tags:
        if i <= 3:
            temp_text_in_wiki.append(events_yearwise.text)
        if i > 3:
            break
        i += 1
    for i in temp_text_in_wiki:
        text_in_wiki.extend(i.split('\n'))

    

    html_festivals = requests.get(
        "https://traveltriangle.com/blog/famous-festivals-of-india/", headers={'User-Agent': 'Mozilla/5.0'}).text
    parsed_festivals = BeautifulSoup(html_festivals, 'html.parser')
    table = parsed_festivals.find('table')

    all_rows = table.find_all('tr')

    for each_row in all_rows[1:]:
        if str(datefromentry.get()) in each_row.text and listofmonths[int(monthfromentry.get())-1] in each_row.text:
            list_of_days.append((each_row.text.split('\n'))[2])
            break

    ####### byju's#########

    byjus_html = requests.get(
        "https://byjus.com/free-ias-prep/important-national-international-days-dates-for-upsc-prelims/").text
    parsed_byjus = BeautifulSoup(byjus_html, 'html.parser')
    table = parsed_byjus.find_all('table', class_='table table-bordered')
    all_rows = table[1].find_all('tr')

    for each_row in all_rows[2:]:
        if str(datefromentry.get()) in each_row.text and listofmonths[int(monthfromentry.get())-1][:3] in each_row.text:
            list_of_days.extend((each_row.text.split('\n'))[2:-1])
            break

    ####### gettings links of the list of days######

    for i in list_of_days:
        for j in search(i, tld="co.in", num=1, stop=1):
            list_of_links.append(j)

###########################################################


def after_enter(event):

    info_label = Label(top_window_input, text='', fg='white',
                       bg='skyblue', font="calibri 15 bold")
    info_label.place(x=50, y=200)
    if (check_entered_date(datefromentry.get(), monthfromentry.get())):
        info_label.config(text="Enter valid date!")
        return

    show_month_label.config(text=listofmonths[int(monthfromentry.get())-1][:3])
    show_date_label.config(text=datefromentry.get())
    wiki_text_listbox.delete(0, END)

    wiki_link_listbox.delete(0, END)

    for widget in space_for_list.winfo_children():
        widget.destroy()

    web_scraping()
    

    close_win()
    global dynamic_index
    dynamic_index = 0

    display_buttons()

    for i, year_wise_text in enumerate(reversed(text_in_wiki)):
        wiki_text_listbox.insert(i, year_wise_text)

    wikilink = "https://en.wikipedia.org/wiki/" + \
        listofmonths[int(monthfromentry.get())-1]+"_"+datefromentry.get()
    wiki_link_listbox.insert(0, wikilink)

###########################################################


def check_entered_date(date, month):

    # there's no need to check the year
    days_in_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (int(month) < 1 or int(month) > 12 or int(date) < 1 or int(date) > days_in_months[int(month)-1]):
        return 1

###########################################################


def display_wikipedia(event):

    special_days_indicator['background'] = 'white'
    wikipedia_indicator['background'] = 'skyblue'
    wiki_frame.pack(fill='both', expand=1)
    all_events_frame.pack_forget()

####################### 0####################################


def display_list_of_events(event):

    special_days_indicator['background'] = 'skyblue'
    wikipedia_indicator['background'] = 'white'
    all_events_frame.pack(fill='both', expand=1)
    wiki_frame.pack_forget()

###########################################################


def on_enter(e):
    e.widget['background'] = 'skyblue'


def on_leave(e):
    e.widget['background'] = 'white'

###########################################################
###########################################################


window = Tk()  # creating a object of type window
# setting the window size after getting the size of the display
window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")
window.config(bg="skyblue")
window.iconbitmap("project file\KD icon.ico")
window.title('KNOW THE DAY')


def popupwindow():

    global datefromentry
    datefromentry = StringVar()
    datefromentry.set(today.day)
    global monthfromentry
    monthfromentry = StringVar()
    monthfromentry.set(today.month)
    global top_window_input

    top_window_input = Toplevel(window, bg='skyblue')
    top_window_input.geometry("300x300")
    top_window_input.iconbitmap("project file\KD icon.ico")
    top_window_input.title('KNOW THE DAY')
    Label(top_window_input, text="Enter a Date : ",
          bg="skyblue", font="calibri 13 ").place(x=50, y=50)
    # packing the entry widgets in the frame f1
    date_entry = Entry(
        top_window_input, textvariable=datefromentry, justify="center", width=3)
    date_entry.place(x=175, y=55, width=25)

    Label(top_window_input, text="Enter a Month : ",
          bg="skyblue", font="calibri 13 ").place(x=50, y=100)
    month_entry = Entry(
        top_window_input, textvariable=monthfromentry, justify="center", width=3)
    month_entry.place(x=175, y=105, width=25)

    enter_button = Button(top_window_input, bg="white",
                          text="Get the info?", width=13, activebackground="skyblue")
    enter_button.place(x=110, y=150, width=75)
    enter_button.bind('<Button-1>', after_enter)
    enter_button.bind("<Enter>", on_enter)
    enter_button.bind("<Leave>", on_leave)


def close_win():
    top_window_input.destroy()


heading_frame = Frame(window, width=1000, height=224, bg="skyblue")
heading_frame.pack(side=TOP, fill="x", expand=True, anchor='n')

bottom_frame = Frame(window, width=1000, height=800, bg="white")
bottom_frame.pack(side=BOTTOM, fill="both", expand=True)

# heading frame

left_heading_frame = Frame(heading_frame, bg='skyblue')
left_heading_frame.pack(side=LEFT, fill='both', expand=1)
right_heading_frame = Frame(heading_frame, bg='skyblue')
right_heading_frame.pack(side=RIGHT, fill='both', expand=1)
Label(left_heading_frame, text="KNOW THE DAY", bg="skyblue",
      font="felixtitling 45 bold", anchor="w").pack(side=TOP, fill="both", pady=(1, 0))  # title of the project
Label(left_heading_frame, text=date_details, bg="skyblue",
      font="calibri 13 ", anchor='w').pack(side=TOP, pady=(0, 1), fill="both")

show_month_label = Label(right_heading_frame, height=1, width=15,
                         font="calibri 10 bold", justify='center', relief=GROOVE)
show_month_label.pack(side=TOP, expand=1, pady=3)
show_date_label = Label(right_heading_frame, height=4, width=15,
                        font="calibri 10 bold", anchor='center', relief=GROOVE)
show_date_label.pack(side=TOP, expand=1)
change_date_button = Button(
    right_heading_frame, text="change day?", width=14, command=lambda: popupwindow())
change_date_button.pack(side=TOP, expand=1, pady=3)
change_date_button.bind("<Enter>", on_enter)
change_date_button.bind("<Leave>", on_leave)

# bottom frame

left_frame_bottom = Frame(bottom_frame, width=1, height=800, bg='white')
left_frame_bottom.pack(side=LEFT, fill=BOTH, expand=1)

top_frame_left_bottom = Frame(left_frame_bottom, bg="white")
top_frame_left_bottom.pack(side=TOP, fill=BOTH, expand=1)

bottom_frame_left_bottom = Frame(left_frame_bottom, bg="white")
bottom_frame_left_bottom.pack(side=BOTTOM, fill=BOTH, expand=1)

special_days_indicator = Label(
    top_frame_left_bottom, width=2, text="", bg="white")
special_days_indicator.pack(side=LEFT, fill="y", expand=1, padx=9, pady=4)
special_days_button = Button(
    top_frame_left_bottom, text=" SPECIAL DAYS ", bg="white")
special_days_button.pack(side=RIGHT, fill=BOTH, expand=1, pady=7)
special_days_button.bind('<Button-1>', display_list_of_events)
special_days_button.bind("<Enter>", on_enter)
special_days_button.bind("<Leave>", on_leave)

wikipedia_indicator = Label(
    bottom_frame_left_bottom, width=2, text="", bg="white")
wikipedia_indicator.pack(side=LEFT, fill="y", expand=1, padx=0, pady=3)
wikipedia_button = Button(bottom_frame_left_bottom,
                          text="PAST EVENTS", bg="white")
wikipedia_button.pack(side=RIGHT, fill=BOTH, expand=1, pady=7)
wikipedia_button.bind('<Button-1>', display_wikipedia)
wikipedia_button.bind("<Enter>", on_enter)
wikipedia_button.bind("<Leave>", on_leave)

right_frame_bottom = Frame(bottom_frame, width=1420, height=800, bg='white')
right_frame_bottom.pack(side=RIGHT, fill=BOTH, expand=1)

# list of events frame

all_events_frame = Frame(right_frame_bottom, bg="white", height=800)

left_frame_body = Frame(all_events_frame, width=400,
                        height=800, bg="white")
left_frame_body.pack(fill="both", expand=True, side=LEFT, padx=4, pady=4)
right_frame_body = Frame(all_events_frame, width=400,
                         height=800, bg="white")
right_frame_body.pack(fill="both", expand=True, side=RIGHT, padx=4, pady=4)

######

dynamic_index = 0


def display_buttons():
    for day_in_the_list in list_of_days[dynamic_index:]:
        event_buttons = Button(space_for_list, bg="white", width=45, height=5,
                               text=f"{day_in_the_list}", font="calibri 12 ", anchor="w", activebackground="#00ABB3", activeforeground="black")
        event_buttons.pack(side=TOP, fill="x", padx=13, pady=2)
        event_buttons.bind('<Button-1>', after_clicking_specialday_button)


def up(event):
    global dynamic_index
    if (dynamic_index == 0):
        return
    dynamic_index -= 1
    for widget in space_for_list.winfo_children():
        widget.destroy()
    display_buttons()


def down(event):
    global dynamic_index
    if (dynamic_index == len(list_of_days)-1):
        return
    dynamic_index += 1
    for widget in space_for_list.winfo_children():
        widget.destroy()
    display_buttons()


#######
Label(left_frame_body, text="LIST OF SPECIAL DAYS",
      bg="skyblue", font="calibri 15 bold").pack(side=TOP, fill='x')
space_for_list = Frame(left_frame_body, width=450, height=350, bg="skyblue")
space_for_list.pack(side=LEFT, fill="both", expand=True, padx=5, pady=5)
space_for_up_down = Frame(left_frame_body, width=50, height=350, bg="white")
space_for_up_down.pack(side=RIGHT, fill="both", expand=True, padx=5, pady=5)
up_photo = Image.open("project file\\up-arrow.jpg")
new_upphoto = ImageTk.PhotoImage(up_photo.resize((20, 20)))
up_button = Button(space_for_up_down, bg='white',
                   activebackground='white', image=new_upphoto, height=300, width=20)
up_button.pack(side=TOP, fill='both', anchor='n', expand=1)
up_button.bind('<Button-1>', up)
down_photo = Image.open("project file\\down-arrow.jpg")
new_downphoto = ImageTk.PhotoImage(down_photo.resize((20, 20)))
down_button = Button(space_for_up_down, bg='white',
                     activebackground='white', image=new_downphoto, width=20, height=300)
down_button.pack(side=BOTTOM, fill='both', anchor='s', expand=1)
down_button.bind('<Button-1>', down)

######

title_frame = Frame(right_frame_body, bg="skyblue")
title_frame.pack(side=TOP, expand=True, fill="both", pady=5)
Label(title_frame, text="SPECIAL DAY", bg="skyblue",
      font="calibri 15 bold").pack(side=LEFT)
title_frame_listbox = Listbox(
    title_frame, width=500, height=2, font="calibri 13", justify="center")
title_frame_listbox.pack(fill="both", expand=True, padx=6, pady=6)

text_of_day_frame = Frame(right_frame_body, bg="skyblue",
                          width=500, height=2)
text_of_day_frame.pack(side=TOP, expand=True, fill="both")
Label(text_of_day_frame, text="WEB PAGE OF THE EVENT",
      bg="skyblue", font="calibri 15 bold").pack(side=TOP)

web_frame = tkinterweb.HtmlFrame(
    text_of_day_frame, height=2, messages_enabled=False)
web_frame.pack(fill="both", expand=True, padx=4, pady=4)


# wikipedia frame

wiki_frame = Frame(right_frame_bottom, bg="white", height=800)
Label(wiki_frame, text="DAY IN THE PAST", bg="skyblue",
      font="calibri 15 bold").pack(side=TOP, padx=6, pady=6, fill="x")

wiki_listbox_frame = Frame(wiki_frame, height=29, bg="skyblue")
wiki_listbox_frame.pack(side=TOP, padx=5, pady=2, fill="both", expand=True)
wiki_text_v_sb = Scrollbar(wiki_listbox_frame, orient=VERTICAL,
                           activebackground="black", elementborderwidth=1)
wiki_text_v_sb.pack(side=RIGHT, fill="y")
wiki_text_listbox = Listbox(wiki_listbox_frame, width=500,
                            height=24, bg="white", relief=FLAT, font="calibri 13")
wiki_text_listbox.pack(fill="both", expand=True, padx=5, pady=5)

wiki_text_h_sb = Scrollbar(wiki_listbox_frame, orient=HORIZONTAL,
                           activebackground="black", elementborderwidth=1)
wiki_text_h_sb.pack(side=BOTTOM, fill="x")
wiki_text_listbox.config(yscrollcommand=wiki_text_v_sb.set)
wiki_text_listbox.config(xscrollcommand=wiki_text_h_sb.set)

wiki_link_frame = Frame(wiki_frame, height=2, bg="skyblue")
wiki_link_frame.pack(side=BOTTOM, anchor="s", padx=5,
                     pady=5, fill="x", expand=True)
Label(wiki_link_frame, text="LINK", bg="skyblue", font="calibri 15 bold").pack(
    side=LEFT, anchor="w", padx=3, pady=3)
wiki_link_listbox = Listbox(wiki_link_frame, height=2, font="calibri 17")
wiki_link_listbox.pack(side=LEFT, padx=6, pady=4, fill="x", expand=True)

wiki_text_h_sb.config(command=wiki_text_listbox.xview)
wiki_text_v_sb.config(command=wiki_text_listbox.yview)

#######
popupwindow()
#######

window.mainloop()
