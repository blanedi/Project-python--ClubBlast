
"""
####** Project : ClubBlast Hertie engine** ####

Objective:

Hertie has an active social and academic community, with dozens of student clubs and regular compelling events. 
Currently, events are communicated to the student body through email. 
This requires students to read through long lists of information in multiple locations to identify events they would enjoy.
It can be difficult for busy students (and faculty) to keep track of! Our project will allow Hertie community members to identify upcoming club events of significance by entering their interests. 
It will return suggestions of forthcoming club events based on user input, with additional information about the event so the user can make an informed decision on how best to spend their time.

Team 
Christopher Borges
Cintya Huaire
Anusha Rajan
Frieder König

"""

#importing the libraries to be use#####
import pandas as pd
import io
import datefinder
import re
import numpy as np
from datetime import datetime
from IPython.display import display

######uploading the database########


###Data Prep Functions###
df = pd.read_excel("https://github.com/blanedi/Project-python--ClubBlast/blob/main/HertieClubBlast%20-%20Final.xlsx?raw=true")

df = df.dropna()
#DateFrameColumnRemover
#Author: Chris Borges
#Description: Removes excess columns from dataframe
#Inputs: Title of columns to remove from dataframe
#Output: None
def DataFrameColumnRemover(ColumnTitle):
  for i in ColumnTitle:
    df.drop(i,axis=1, inplace=True)

#FindDates
#Author: Chris Borges
#Description: Returns dates in datetime format for each cell in specified column
#Inputs: dataframe, Name of column
#Output: Dates in datetime format
def FindDates(df,ColumnTitle):
  datewords = []
  x = 1
  while x < len(df. index) + 1: #for each cell in column
    Var1 = df.loc[x,ColumnTitle] #store values from cell in df in Var1
    Var2 = ASCIISwap(Var1) #strip out excess ASCII characters
    Var3 = WordFinder(Var2, extractwords) #identify the time-related words in each string
    datewords.append(Var3) #store those words in list as a string
    x += 1
  return DateID(datewords) #run string through datefinder

#ASCIISwap
#Author: Chris Borges
#Description: Preps strings for datefinder by removing specified ASCII characters
#Inputs: String 
#Output: String with specified ASCII characters removed
def ASCIISwap(prestrip):
  asciiDict = {
    33: 32,
    41: 32,
    44: 32,
    63: 32,
    }
  poststrip = prestrip.translate(asciiDict)
  return poststrip


#WordFinder
#Author: Chris Borges
#Description: Function to return the specified date and time words from the string
#Inputs: String to be analyzed; List of words to keep in the string
#Output: String with only the specified words included
def WordFinder(prestrip, words):
  list1 = []
  list2 = []
  list1 = prestrip.split()
  for i in list1:
    if i in words:
      list2.append(i)
  poststrip = " ".join(list2)
  return (poststrip)


#Extractwords
#Author: Chris Borges
#Description: List of Time-related words to extract from TimeFinder function
extractwords = [
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December',
    'Jan', 'Feb', 'Mar', 'Apr', 'Aug', 'Sep', 'Oct', 'Nov',' Dec',
    'Monday', 'Tuesday', ' Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', 
    '20', '21,','22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '01', '02', '03', '04', '05', '06', '07', '08', '09',
    '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', 
    '17th', '18th', '19th', '20th', '21st','22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st',
    '1st.', '2nd.', '3rd.', '4th.', '5th.', '6th.', '7th.', '8th.', '9th.', '10th.', '11th.', '12th.', '13th.', '14th.', '15th.', '16th.', 
    '17th.', '18th.', '19th.', '20th.', '21st.','22nd.', '23rd.', '24th.', '25th.', '26th.', '27th.', '28th.', '29th.', '30th.', '31st.',
    'pm', 'am', "PM", "AM", "2022", "2023"
]

#DateID
#Author: Chris Borges
#Description: Runs datefinder to identify dates from each string in a list
#Inputs: List of strings to search for dates
#Output: List of dates identified by datefinder 
def DateID(list3):
  dates = []
  y = 0
  for i in list3: #for each string in list
    matches = datefinder.find_dates(i) #run date-finder
    for match in matches: #for each identified date
      match = match.date() #removes the time
      dates.append(match) #add to new list
    list3[y] = dates #update list with datefinder identified dates - note: moving values between lists to handle scenarios where multiple dates are identified
    dates = []
    y += 1
  return (list3)

#StringCleaning
#Author: Chris Borges
#Description: Removes identified special characters using ASCII keys - run after using datefinder to prep "dates" column for search
#Inputs: String
#Output: String with specified ASCII characters removed
def StringCleaning(prestrip):
  stringcleaner = {
    40: 32,
    41: 32,
    46: 32,
    91: 32,
    93: 32,
    97: 32,
    100: 32,
    101: 32,
    105: 32,
    109: 32,
    116: 32
    }
  poststrip = prestrip.translate(stringcleaner)
  poststrip = poststrip.strip()
  return poststrip


###Data Prep###
#Author: Chris Borges
#Description: Preps data for search - takes file, removes rows with null values, 
#creates new "dates" column based on datefinder analysis, cleans "dates" column for search
#Inputs: Name of file with data
#Output: None

ColumnRemoveList = ['Timestamp', 'Email Address']
DataFrameColumnRemover(ColumnRemoveList)
df['Dates'] = FindDates(df,"Announcement") #Create new column "dates" based on analysis of words in specified column
df["Dates"] = df["Dates"].astype(str)
for i in range(1,len(df.index)+1):
  df.loc[i,'Dates'] = StringCleaning(df.loc[i,'Dates'])



#####################################################
#########Generating variable "theme"#################
#############@author: CINTYAHUAIRE####################
#######################################################
df['theme'] = df['Announcement'].str.findall('finance|human right|digitalization|programm|cybersecurity|thesis|sustainable|film|movie|hike|boulder|wine', flags=re.IGNORECASE).str.join(",")

#####standarizing the themes #####
#academic events= human rights, thesis
#leisure activities= hike, wine, boulder
#other events= movie, film, etc
#tech events= cybersecurity, program

# create a list of our conditions
conditions = [
    (df['theme'].str.count("thesis") >=1)| (df['theme'].str.count(r"[hH]uman rights") >=1)| (df['theme'].str.count(r"[sS]ustainabl") >=1),
    (df['theme'].str.count(r"[hH]ik") >=1) | (df['theme'].str.count(r"[wW]ine") >=1)|(df['theme'].str.count(r"[bB]oulder") >=1),
    (df['theme'].str.count(r"[mM]ovie") >=1) | (df['theme'].str.count(r"[Ff]ilm") >=1),
    (df['theme'].str.count(r"[cC]ybersecurity") >=1) | (df['theme'].str.count(r"[pP]rogramm") >=1)| (df['theme'].str.count(r"[dD]igitalization") >=1)
    ]

# create a list of the values we want to assign for each condition
values = ['academics', 'leisure activities', 'other events', 'tech events']

# create a new column and use np.select to assign values to it using our lists as arguments
df['theme_clean'] = np.select(conditions, values)

#######################################################################
#########Generating  variable "type of event" ##########################
########to now whetever and event is onsite or online################
#######################################################################
df['type of event'] = df['Announcement'].str.findall('campus|online|room|forum', flags=re.IGNORECASE).str.join(",")
#standarizing it so room , forum, campus it should be an event on campus
#online an online event
#outside all the events of leisure activities

# create a list of our conditions
conditions = [
    (df['type of event'].str.count("campus") >=1)| (df['type of event'].str.count("forum") >=1) |(df['type of event'].str.count("room") >=1)
    |(df['type of event'].str.count("Room") >=1)  |(df['type of event'].str.count("Forum") >=1),
    (df['type of event'].str.count("online") >=1) ,
    (df['theme_clean']=="leisure activities")
    ]

# create a list of the values we want to assign for each condition
values = ['on campus', 'online', 'outside Hertie']

# create a new column and use np.select to assign values to it using our lists as arguments
df['type_event_clean'] = np.select(conditions, values)
   
#######################################################################
#########Generating  variable "nro_room" ##########################
########room number if an event is onsite################
#######################################################################


df["nro_room"]=df['Announcement'].str.extract(r"(room \d.\d\d)",re.IGNORECASE, expand=True)


df["nro_room"]=np.where(df['type of event'].str.count("Forum") >=1,"Hertie Forum", df.nro_room)


df["nro_room"].astype("string")
df["nro_room"]=np.where((df["nro_room"].isnull()) & (df['type_event_clean']=="on campus"),"not specified" , df["nro_room"])



###SEARCHING FUNCTIONS###

#SearchStart
#Author: Chris Borges
#Description: Prompts user to select their search criteria - options are club, date, theme, and location
#Selection determines which search function to call
#Inputs: None
#Outputs: None
def SearchStart():
  print ("Welcome to the Hertie School Club Event search tool!")
  path = input("What criteria would you like to search by? Option are club, date, theme, and location ")
  x = 0
  while x != 1:
    if path == "club":
      searchbyclub()
      x = 1
    elif path =="date":
      searchbydate()
      x = 1
    elif path == "theme":
      searchbytheme()
      x = 1
    elif path == "location":
      searchbylocation()
      x = 1
    else:
      print ("Invalid entry - please enter 'Club', 'Date', 'Theme', or 'Location'")
      path = input("What criteria would you like to search by? Option are club, date, theme, and location ")


#searchbydate - Runs search over event dates
def searchbydate():
  pd.set_option('display.max_colwidth', None)
  date = str(input ("What is the date you are looking for? Please enter in YYYY, MM, DD format: "))
  count=df['Dates'].str.contains(date).sum()
  if count<=0:
    print ("There are no events on this date")
  else: 
    datedf = df[df.Dates.str.contains(date)]
    display(datedf.iloc[:, 1:3])

#searchbyclub - Runs search over club names
def searchbyclub():
  pd.set_option('display.max_colwidth', None)
  title = """What is the name of the club you are looking for? Here is a list of clubs, please type in the names as they appear here: \n Work Economy and Social Policy \n Hertie School Hikers \n Hertie School Art Club \n Hertie School Hikers \n Hertie School Art Club \n Hertie Latinoamerica  \n Hertie Sustainability Club \n The Hertie Climbing Group \n Hertie School Security Club \n Hertie Wine Club  \n Hertie Coding Club  \n Kino Club  \n Cinema Politca  \n Centre for Fundamental Rights \n Hertie School City Lab  \n futurEU  \n Hertie Women in Public Policy \n SHIELD \n"""
  club = str(input(title))
#sorting names of clubs into dataframes because they are logged into the sheet differently by students 
#this will generate dataframes for each club, sorted chronologically, doing this will help display the newest event entered by the club most accurately
  WESP =  df[df["Club"].isin([ "WESP Club", "WESP club", "Work Economy and Social Policy", "WESP", "Work, Economy, & Social Policy Club (WESP)"])]
  Hertie_School_Hikers = df[df["Club"].isin(["Hertie School Hikers"])]
  Hertie_School_Art_Club = df[df["Club"].isin(["Hertie School Art Club"])]
  Hertie_Latinoamerica = df[df["Club"].isin(["Hertie Latinoamerica"])]
  Hertie_Sustainability_Club =  df[df["Club"].isin(["Hertie Sustainability Club", "Sustainability Club"])]
  Climbing_and_Bouldering_Club = df[df["Club"].isin([ "Hertie School Climbing and Bouldering Club", "The Hertie Climbing Group"])]
  HSSC = df[df["Club"].isin(["Hertie School Security Club (HSSC)"])]
  Hertie_Wine_Club = df[df["Club"].isin(["Hertie Wine Club", "Hertie wine club"])]
  Hertie_Coding_Club = df[df["Club"].isin(["Hertie Coding Club", "Hertie Coding Club "])]
  Kino_Club = df[df["Club"].isin(["Kino Club", " Kino Club", "Kino Club "])]
  Cinema_Politca = df[df["Club"].isin(["Cinema Politca"])]
  Fundamental_Rights= df[df["Club"].isin(["Student Advisory Board, Centre for Fundamental Rights"])]
  City_lab = df[df["Club"].isin(["Hertie School City Lab"])]
  futurEU = df[df["Club"].isin(["futurEU "])]
  WIPP=df[df["Club"].isin(["Hertie Women in Public Policy (WIPP)"])]
  SHIELD=df[df["Club"].isin(["SHIELD"])]
#elseif statements for generating relevant output to the input
  if club == "Work Economy and Social Policy":
    display(WESP.iloc[[-1],[1,2]])
  elif club == "SHIELD":
    display(SHIELD.iloc[[-1],[1,2]])
  elif club== "Hertie Women in Public Policy": 
    display(WIPP.iloc[[-1],[1,2]])
  elif club== "futurEU":
    display(futurEU.iloc[[-1],[1,2]])
  elif club=="Hertie School City Lab":
    display(City_lab.iloc[[-1],[1,2]])
  elif club=="Centre for Fundamental Rights":
    display(Fundamental_Rights.iloc[[-1],[1,2]])
  elif club=="Cinema Politca":
    display(Cinema_Politca.iloc[[-1],[1,2]]) 
  elif club=="Kino Club":
    display(Kino_Club.iloc[[-1], [1,2]])
  elif club=="Hertie Coding Club":
    display(Hertie_Coding_Club.iloc[[-1],[1,2]])
  elif club=="Hertie Wine Club": 
    display(Hertie_Wine_Club.iloc[[-1],[1,2]])
  elif club=="The Hertie Climbing Group":
    display(Climbing_and_Bouldering_Club.iloc[[-1],[1,2]])
  elif club=="Hertie School Security Club":
    display(HSSC.iloc[[-1],[1,2]])
  elif club=="Hertie Sustainability Club":
    display(Hertie_Sustainability_Club.iloc[[-1],[1,2]])
  elif club=="Hertie Latinoamerica":
    display(Hertie_Latinoamerica.iloc[[-1],[1,2]])
  elif club=="Hertie School Art Club":
    display(Hertie_School_Art_Club.iloc[[-1],[1,2]])
  elif club=="Hertie School Hikers":
    display(Hertie_School_Hikers.iloc[[-1],[1,2]])
  else:
    print("Invalid entry. Please try again.")

#searchbytheme - Runs search over event theme 
def searchbytheme():
  pd.set_option('display.max_colwidth', None)
  title = "What is the type of event you are looking for? You can choose of the following themes: \n Academic \n Leisure \n Tech \n Other \n"
  theme = str(input(title))
#sort events into their respective dataframes
  if theme == "Academic":
    academic=df[df["theme_clean"].isin(["academics"])]
    display(academic.iloc[:, 1:3])
  elif theme == "Leisure":
    academic=df[df["theme_clean"].isin(["leisure activities"])]
    display(academic.iloc[:, 1:3])
  elif theme == "Tech":
    academic=df[df["theme_clean"].isin(["tech events"])]
    display(academic.iloc[:, 1:3])
  elif theme == "Other":
    academic=df[df["theme_clean"].isin(["other events"])]
    display(academic.iloc[:, 1:3])
  else: 
    print("try again")

#searchbylocation - Runs search for events based on whether they are happening on-campus or outside Hertie 
def searchbylocation():
    pd.set_option('display.max_colwidth', None)
    title = "Are you looking for events onsite or outside Hertie? \n Type 'onsite' to search for events on campus \n Type 'outside' to search for events off campus \n"
    location = str(input(title))
    if location=="onsite":
      onsite = df[df.type_event_clean.str.contains("on campus")]
      display(onsite.iloc[:, 1:3])
      moreask = str(input("Are you looking for a specific room number? \n if yes, type the relevant room number. They are: Forum, 2.01, 2.34, 2.35, 3.30, 3.32, 3.47. If not, type 'bye'. \n"))
    if moreask=="Forum":
          forum=df[df.nro_room.str.contains("Hertie Forum", na=False)]
          display(forum.iloc[:, 1:3])
    elif moreask=="2.35": 
            room=df[df.nro_room.str.contains("room 2.35", na=False)]
            display(room.iloc[:, 1:3])
    elif moreask=="3.30": 
            room=df[df.nro_room.str.contains("Room 3.30", na=False)]
            display(room.iloc[:, 1:3])
    elif moreask=="3.32":
            room=df[df.nro_room.str.contains("Room 3.32", na=False)]
            display(room.iloc[:, 1:3])
    elif moreask=="2.01": 
            room=df[df.nro_room.str.contains("Room 2.01", na=False)]
            display(room.iloc[:, 1:3])
    elif moreask=="3.47":
            room=df[df.nro_room.str.contains("room 3.47", na=False)]
            display(room.iloc[:, 1:3])
    elif moreask=="2.34":
            room=df[df.nro_room.str.contains("room 2.34", na=False)]
            display(room.iloc[:, 1:3])
    elif moreask=="bye":
            print("Thank you.")
    elif location=="outside":
          outside = df[df.type_event_clean.str.contains("outside Hertie")]
          display(outside.iloc[:, 1:3])
    else:
          print("Try again")
          
      
  #Start the search 
SearchStart()