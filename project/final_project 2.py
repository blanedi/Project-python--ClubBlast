
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
