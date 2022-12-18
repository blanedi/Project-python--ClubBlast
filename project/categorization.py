#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module selects and cleans the relevant data to search for the dates, themes, event types or rooms

Module Exports:

process_dates()
process_themes()
process_event_types
process_rooms()

"""


import re
import numpy as np
from dateops import find_dates
from stringops import string_cleaning


def process_dates(df):
  """
  This function creates a new clean column that contains the dates based on analysis of words in specified column

  Parameters
  ----------
  df : Tdataframe

  Returns
  -------
  new column on the dataframe containing dates

  """
  df['Dates'] = find_dates(df,"Announcement") #Create new column "dates" based on analysis of words in specified column
  df["Dates"] = df["Dates"].astype(str)
  for i in range(1,len(df.index)+1):
    df.loc[i,'Dates'] = string_cleaning(df.loc[i,'Dates'])

def process_themes(df):
  """
  This function selects and cleans the data to search for themes within a column of strings

  Parameters
  ----------
  df : dataframe.

  Returns
  -------
  new column on the dataframe containing themes

  """
    
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
    
def process_event_types(df):
  """
  This function selects and cleans the data to search for events within a column of strings

  Parameters
  ----------
  df : dataframe

  Returns
  -------
  new column on the dataframe containing types of event (online, onsite and outside Hertie)

  """
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
    
def process_rooms(df):
  """
  This function selects and cleans the data to search for the number of room that the event is happening within a column of strings

  Parameters
  ----------
  df : dataframe

  Returns
  -------
  new column on the dataframe containing number of rooms on the dataframe

  """
  
  df["nro_room"]=df['Announcement'].str.extract(r"(room \d.\d\d)",re.IGNORECASE, expand=True)


  df["nro_room"]=np.where(df['type of event'].str.count("Forum") >=1,"Hertie Forum", df.nro_room)


  df["nro_room"].astype("string")
  df["nro_room"]=np.where((df["nro_room"].isnull()) & (df['type_event_clean']=="on campus"),"not specified" , df["nro_room"])
