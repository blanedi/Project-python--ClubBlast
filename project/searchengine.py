#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module contains the search functions that searches through user input by date, club, theme or location

Module Exports:

start_search()
date_id()
search_by_date()
search_by_club()
search_by_theme()
search_by_location()

"""

import pandas as pd
from IPython.display import display



def start_search(df):
  """
  This function prompts user to select their search criteria - options are club, date, theme, and location considering the dataframe

  Parameters
  ----------
  df : dataframe

  Returns
  -------
  None.

  """
  print ("Welcome to the Hertie School Club Event search tool!")
  path = input("What criteria would you like to search by? Option are club, date, theme, and location ")
  x = 0
  while x != 1:
    if path == "club":
      search_by_club(df)
      x = 1
    elif path =="date":
      search_by_date(df)
      x = 1
    elif path == "theme":
      search_by_theme(df)
      x = 1
    elif path == "location":
      search_by_location(df)
      x = 1
    else:
      print ("Invalid entry - please enter 'Club', 'Date', 'Theme', or 'Location'")
      path = input("What criteria would you like to search by? Option are club, date, theme, and location ")

#search_by_date - Runs search over event dates

def search_by_date(df):
  """
  This function runs search over event dates within a dataframe

  Parameters
  ----------
  df : dataframe

  Returns
  -------
  None.

  """
  pd.set_option('display.max_colwidth', None)
  date = str(input ("What is the date you are looking for? Please enter in YYYY, MM, DD format: "))
  count=df['Dates'].str.contains(date).sum()
  if count<=0:
    print ("There are no events on this date")
  else: 
    datedf = df[df.Dates.str.contains(date)]
    display(datedf.iloc[:, 1:3])

#search_by_club - Runs search over club names
def search_by_club(df):
  """
  This function allows the user to search the events by the name of an specific club 

  Parameters
  ----------
  df : dataframe

  Returns
  -------
  None.

  """
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

#search_by_theme - Runs search over event theme 
def search_by_theme(df):
  """  
  This function allows the user to search the events by theme

  Parameters
  ----------
  df : dataframe

  Returns
  -------
  None.

  """
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

#search_by_location - Runs search for events based on whether they are happening on-campus or outside Hertie 
def search_by_location(df):
  """
  This function allows the user to search for events based on whether they are happening on-campus or outside Hertie 

  Parameters
  ----------
  df : dataframe

  Returns
  -------
  None.

  """
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
        
