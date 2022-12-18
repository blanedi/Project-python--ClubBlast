#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module contains a list of date-related words to extract from strings for processing and functions to identify dates

Module Exports:

find_dates()
date_id()

"""


from stringops import ascii_swap, word_finder
import datefinder

#Description: List of Time-related words to extract from TimeFinder function
time_keywords = [
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



def find_dates(df, column_names):
  """
  This function is used for returns dates in datetime format for each cell in specified column

  Parameters
  ----------
  df : dataframe
  column_names : name of the column that contains the information

  Returns
  -------
  dates : list of dates in datetime format for each cell in specified column

  """
  datewords = []
  x = 1
  while x < len(df. index) + 1: #for each cell in column
    Var1 = df.loc[x,column_names] #store values from cell in df in Var1
    Var2 = ascii_swap(Var1) #strip out excess ASCII characters
    Var3 = word_finder(Var2, time_keywords) #identify the time-related words in each string
    datewords.append(Var3) #store those words in list as a string
    x += 1
  dates = DateID(datewords) #run string through datefinder
  return dates


def date_id(strings):
  """
  This function is used to identify dates from each string in a list

  Parameters
  ----------
  strings : list of strings that contains dates

  Returns
  -------
  strings : list of dates identified by datefinder 

  """
  dates = []
  y = 0
  for i in strings: #for each string in list
    matches = datefinder.find_dates(i) #run date-finder
    for match in matches: #for each identified date
      match = match.date() #removes the time
      dates.append(match) #add to new list
    strings[y] = dates #update list with datefinder identified dates - note: moving values between lists to handle scenarios where multiple dates are identified
    dates = []
    y += 1
  return (strings)
