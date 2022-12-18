###Data Prep Functions###
"""
This module contains the dataprep functions for the Hertie ClubBlast Search Engine. 

Exports:
- 

"""



def DataFrameColumnRemover(ColumnTitle):
  """Removes specified columns from dataframe by title

    Args: 
        ColumnTitle (str): title of column to be removed from dataframe.
      
    Returns:
        NA
  
  """
  for i in ColumnTitle:
    df.drop(i,axis=1, inplace=True)

    
def FindDates(df,ColumnTitle):
  """Returns dates in datetime format for each cell in specified column

    Args: 
        df (dataframe): dataframe with column to be processed
        ColumnTitle (str): title of column to be processed
      
    Returns:
        dates (list): list of dates from each cell in column
  
  """
  datewords = []
  x = 1
  while x < len(df. index) + 1: #for each cell in column
    Var1 = df.loc[x,ColumnTitle] #store values from cell in df in Var1
    Var2 = ASCIISwap(Var1) #strip out excess ASCII characters
    Var3 = WordFinder(Var2, extractwords) #identify the time-related words in each string
    datewords.append(Var3) #store those words in list as a string
    x += 1
  dates = DateID(datewords) #run string through datefinder
  return dates


def ASCIISwap(prestrip):
  """Preps strings for datefinder by removing specified ASCII characters

    Args: 
        prestrip (str): string to be processed
      
    Returns:
        poststrip (str): string with specified characters removed
  
  """
  asciiDict = {
    33: 32,
    41: 32,
    44: 32,
    63: 32,
    }
  poststrip = prestrip.translate(asciiDict)
  return poststrip


def WordFinder(prestrip, words):
  """Return the specified date and time words from a string

    Args: 
        prestrip (str): string to be processed
        words (list): list of words to keep in the string
      
    Returns:
        poststrip (str): string with only the specified words included
  
  """
  list1 = []
  list2 = []
  list1 = prestrip.split()
  for i in list1:
    if i in words:
      list2.append(i)
  poststrip = " ".join(list2)
  return (poststrip)


'''List of Time-related words to extract from TimeFinder function'''
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


def DateID(prerun):
  """Runs datefinder to identify dates from each string in a list

    Args: 
        prerun (list): list of strings to search for dates
      
    Returns:
        postrun (list): list of dates identified by datefinder in datetime.date format
  
  """
  dates = []
  postrun = []
  y = 0
  for i in prerun: #for each string in list
    matches = datefinder.find_dates(i) #run date-finder
    for match in matches: #for each identified date
      match = match.date() #remove the time
      dates.append(match) #add to new list
    postrun.append(dates) #update list with datefinder identified dates - note: moving values between lists to handle scenarios where multiple dates are identified
    dates = []
    y += 1
  return (postrun)


def StringCleaning(prestrip):
  """Removes identified special characters using ASCII characters - run after using datefinder to prep "dates" column for search

    Args: 
        prestrip (list): string to be processed
      
    Returns:
        poststrip (list): spring with specified characters removed
  
  """
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

df = pd.read_excel("https://github.com/blanedi/Project-python--ClubBlast/blob/main/HertieClubBlast%20-%20Final.xlsx?raw=true")

df = df.dropna()

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

