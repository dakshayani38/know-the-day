
# know-the-day-project
Python Projects

This project is built using python and webscraping techniques which utilizes a Graphical User Interface (GUI) that prompts the user to input a specific date. Once the user enters the desired date, the GUI displays important events and happenings from that day across the globe, making it easier for the user to access information about special events on a specific day. The GUI is built using Tkinter library.


Output:

![Screenshot_20221205_224942](https://github.com/durgavinay8/know-the-day-project/assets/113960662/a1361d1d-f585-4b74-98db-de3ad6e1f55b)
![Screenshot_20221205_225057](https://github.com/durgavinay8/know-the-day-project/assets/113960662/0fbe41eb-17df-4764-bd14-87ae4599fcaa)
![Screenshot_20221205_225206](https://github.com/durgavinay8/know-the-day-project/assets/113960662/431874f8-fff7-4a78-8dde-68edd6fac577)

 ------------------------------------------------
This project is primarily divided into two parts:
1.	Extract all the required data based on the entered date  
2.	Displaying the Extracted data making use of the Graphical User Interface (GUI)
 ------------------------------------------------
1. Extract the required data based on the entered date:
We gathered the required data from various websites. This data involves two things: 
a.  Information of the importance of the day (celebrated as):
We made use of various websites i.e., United Nations, 	National day calendar, Jagran-josh, Byju’s, Travel triangle to gather the information of all the celebrated days of that specific entered date.
Then to show the detailed information regarding the day we displayed the 1st website after searching it in google.
b. detailed information of its historical occurrences:
Here, we made use of Wikipedia 	 to get historical information.

Web-scraping technique has been deployed to extract all the necessary information from these websites and various tools from the bs4, BeautifulSoup, requests modules have been used to make this possible.
Tools in the google module have been used to search for the link of the first website after searching it in the google.

2. Displaying the extracted data making use of the Graphical User Interface (GUI):
Tkinter has been used for the design and implementation of the Graphical User Interface, it’s a standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications.
We made use of various tools, widgets provided by Tkinter and made them bind them to various functions to make the GUI possible.
