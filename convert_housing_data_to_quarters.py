def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean 
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].
    
    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.
    
    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''
    
    return "ANSWER"


import pandas as pd 

mon_to_qua = {'01':'q1','02':'q1','03':'q1',
             '04':'q2','05':'q2','06':'q2', 
             '07':'q3','08':'q3','09':'q3',
             '10':'q4','11':'q4','12':'q4'}

states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

df = pd.read_csv('City_Zhvi_AllHomes.csv')

df['State'] = df['State'].map(states)

col_to_drop = ['RegionID','Metro','CountyName','SizeRank']

df = pd.DataFrame(df.drop(columns = col_to_drop))

df = df.set_index(['State', 'RegionName'])

dfloc = df.loc[:,'2000-01':]

dfloc =dfloc.stack()
dfloc = dfloc.reset_index().rename(columns = {'level_2': 'Year', 0:'MedianPrice'})

# convert year to quarter based

dfloc['Year1'] = dfloc['Year'].str[0:4]+ (dfloc['Year'].str[-2:].map(mon_to_qua))

# df1['MedianPrice'] = df1['MedianPrice'].mean()#

dfloc1 = (df.groupby(['State','RegionName'])
        .mean()
        .unstack())



import pandas as pd 
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}
month_to_qtr = {'01':'q1','02':'q1','03':'q1','04':'q2','05':'q2','06':'q2',
                '07':'q3','08':'q3','09':'q3','10':'q4','11':'q4','12':'q4'}


df = pd.read_csv('City_Zhvi_AllHomes.csv')
df['State'] = df['State'].map(states)
    
df = pd.DataFrame(df.drop(columns=['Metro','CountyName','SizeRank'])
                 .set_index(['RegionID','State','RegionName'])
                 .stack()
                 .reset_index()
                 .rename(columns={'level_3':'Year-Mo',
                                  0:'MedianPrice'}))
df['YearQtr'] = df['Year-Mo'].str[0:4] + (df['Year-Mo'].str[-2:]
                                        .map(month_to_qtr))
df = df[df['YearQtr']>='2000q1'].copy()
df = (df.drop(columns=['Year-Mo'])
     .groupby(['RegionID','State','RegionName','YearQtr'])
     .mean()
     .unstack())
df.index = df.index.droplevel()
df.columns = df.columns.droplevel()































# col_to_drop = ['RegionID','Metro','CountyName','SizeRank']

# df_con = df.drop(col_to_drop, axis =1)


# df_con_T = df_con.T.reset_index()

# # df_con_T = df_con_T.loc['2000-01','2016-08']

# df_con_T['index'] = df_con_T['index'].str[0:4]+ (df_con_T['index'].str[-2:].map(mon_to_qua))

# df_con_T = df_con_T.set_index('index')

# df_con_final = df_con_T.T

# df_con_final.rename(columns ={'0':'RegionName','1':'State'})

























