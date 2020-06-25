# =============================================================================
# Hypothesis Testing
# =============================================================================


# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}



def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"]  )
    
    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    1
    return "ANSWER"


import pandas as pd
import numpy as np 

ut = pd.read_csv('university_towns.txt', sep="/n", engine = 'python', header=None).rename(columns= {0:'location'})


# ut['state'] = ut['location'].apply(lambda x: x.replace('[edit]',''))

# region = ut['state'].apply(lambda x: x.replace(r'\[.*','', regex = True))

ut['State']= ut.loc[ut['location'].str.contains('[edit]',regex = False)]
ut['State'] = ut['State'].fillna(method = 'ffill')

ut['RegionName'] = ut['location'].apply(lambda x:  x if x[-6:] != '[edit]' else np.nan)

ut = ut.drop(ut[ut['RegionName'].isna()].index)

ut['State'] = ut['State'].apply(lambda x: x.split('[')[0])

ut['RegionName']= ut['RegionName'].str.replace(r'\(.*\)', '').str.replace(r'\[.*','')

ut_out = ut.iloc[:,1:3].reset_index(drop = True)






with open("university_towns.txt") as f:
    townslist = f.readlines()

townslist = [x.rstrip() for x in townslist]

townslist2 = list()

for i in townslist:
    if i[-6:] == '[edit]':
        temp_state = i[:-6]
        # totlist2 = townslist2.append(temp_state)
    elif '(' in i:
        
        town = i[:i.index('(') - 1]
        townslist2.append([temp_state,town])
    else:
        town = i
        townslist2.append([temp_state, town])

collegedf = pd.DataFrame(townslist2, columns=['State','RegionName'])


get_list_of_university_towns()






