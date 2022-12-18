
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
from dfcolumns import remove_columns
from categorization import process_dates, process_themes, process_event_types, process_rooms
from searchengine import start_search


club_file= "https://github.com/blanedi/Project-python--ClubBlast/blob/main/HertieClubBlast%20-%20Final.xlsx?raw=true"


###Data pre processing##

df = pd.read_excel(club_file)
df = df.dropna()
columns_to_remove = ['Timestamp', 'Email Address']
remove_columns(df, columns_to_remove)


###Data categorization###

process_dates(df)

process_themes(df)

process_event_types(df)

process_rooms(df)  
      
#Start the search 

start_search(df)