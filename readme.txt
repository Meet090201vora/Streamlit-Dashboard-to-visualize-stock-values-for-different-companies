Nirma University
TEAM-8
Project : OHLC ENGINE

Contributors : 
Mansi Busa	  19BCE030
Meet Vora    	  19BCE299
Chaitanya Chhichhia 	  19BEC018 
Maarjani Sanghavi     	  19BEC117
 

Problem Statement
To Create a Dashboard based on which the user would be able to analyze the sentiment of the specific stock. You’re required to create an Analytical Server "OHLC '' (Open/High/Low/Close) time series based on the ‘Stock List’ dataset which will be provided to you in a separate JSON format and its output should be a timely report printed in Charts. (Note: You can use chart.js or any other free API for displaying Charts)
 
Solution
Language used: 
Python 

Design:
Using python as the core language, we created a dashboard in which the user can view the Stock details of the desired company. The whole process is divided into 3 sub-modules.

Sub Module 1: 
reading data from the .json file and creating a dataframe of required attributes, like high, low, date, open, close. This dataframe is then fed to the FSM which in turn creates different plots as per the user’s interest.

Sub Module 2: 
The finite state machine is an algorithm to compute OHLC performance and to give users options to view different data charts like bar graphs, candlesticks, etc. 
The user can search a particular company in the search bar by simply typing its  symbol in the search field and can select a particular data chart from a drop down menu to view the company’s stock performance. 
There is a Time slider provided beneath where the user can choose to view the stocks between a particular time interval.
Each module has its own functionality.

Sub Module 3: 
At the most basic level, Streamlit is served via Tornado.To pass information between Python and JavaScript, the protocol buffers serialization format is used.
 
Product:
Highly interactive Streamlit based web project that displays the Stock analysis of various companies where the user can choose the desired company and can view its OHLC performance. It is backed by different graphical charts in order to give better insights about the stock of a company.
 
 
