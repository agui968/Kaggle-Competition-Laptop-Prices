df['Ram']=df['Ram'].str.replace('GB','').astype(int)
df['Weight']=df['Weight'].str.replace('kg','').astype(float)
df['OpSys'][df['OpSys']=='Windows 10 S']='Windows 10'
df['OpSys'][df['OpSys']=='Mac OS X']='macOS'
df = pd.concat([df, pd.get_dummies(df['OpSys'], prefix='OpSys')], axis=1)

df = df.drop('OpSys', axis=1)
matches = df['Memory'].str.extractall(r'(\d+)\s?([GT]B)').reset_index()
matches.columns = ['level_0', 'match', 'Capacity', 'Unit']

# Calculate total memory in GB
matches['Total_GB'] = matches['Capacity'].astype(float) * matches['Unit'].replace({'GB': 1, 'TB': 1000}).fillna(1)
# Group by level_0 and sum to get the total memory for each row
df['Total_GB'] = matches.groupby('level_0')['Total_GB'].sum()
# Determine storage type
df['Storage_Type'] = df['Memory'].str.extract(r'(SSD|HDD)')

from sklearn.preprocessing import LabelEncoder
le= LabelEncoder()
le.fit(df['Storage_Type'])
df['Storage_type_Enc']= le.transform(df['Storage_Type'])
df.head()

df = pd.concat([df, pd.get_dummies(df['Company'], prefix='Company')], axis=1)
df = df.drop('Company', axis=1)

df = pd.concat([df, pd.get_dummies(df['TypeName'], prefix='TypeName')], axis=1)
df = df.drop('TypeName', axis=1)

df['ResolutionHeight'] = df['ScreenResolution'].str.extract(r'\d+x(\d+)')
# df.head()

df['CPU_Type'] = df['Cpu'].str.extract(r'(\bIntel\b|\bAMD\b|\bCore\s[^\d]+)')
df['Speed_GHz'] = df['Cpu'].str.extract(r'(\d+\.\d+)GHz')

df = pd.get_dummies(df, columns=['CPU_Type'], prefix='CPU_Type')

df['ResolutionHeight']=df['ResolutionHeight'].astype(int)
df['Speed_GHz']=df['Speed_GHz'].astype(float)

df.fillna(0, inplace=True)

df.drop(columns='Memory',inplace=True)
df.drop(columns='Storage_Type',inplace=True)
df.drop(columns='Product',inplace=True)
df = df.drop('ScreenResolution', axis=1)
df = df.drop('Cpu', axis=1)
df.drop(columns='laptop_ID',inplace=True)
df.drop(columns='Inches',inplace=True)

df.drop(columns='Gpu',inplace=True)

X=df.drop(columns=['Price_euros','id'])
y=df['Price_euros']


"""***********************************"""

#REPEATING FOR TEST.CSV
test=pd.read_csv('data/test.csv')
test['Ram']=test['Ram'].str.replace('GB','').astype(int)
test['Weight']=test['Weight'].str.replace('kg','').astype(float)
test['OpSys'][test['OpSys']=='Windows 10 S']='Windows 10'
test['OpSys'][test['OpSys']=='Mac OS X']='macOS'
test = pd.concat([test, pd.get_dummies(test['OpSys'], prefix='OpSys')], axis=1)

test = test.drop('OpSys', axis=1)
matches2 = test['Memory'].str.extractall(r'(\d+)\s?([GT]B)').reset_index()
matches2.columns = ['level_0', 'match', 'Capacity', 'Unit']

# Calculate total memory in GB
matches2['Total_GB'] = matches2['Capacity'].astype(float) * matches2['Unit'].replace({'GB': 1, 'TB': 1000}).fillna(1)
# Group by level_0 and sum to get the total memory for each row
test['Total_GB'] = matches2.groupby('level_0')['Total_GB'].sum()
# Determine storage type
test['Storage_Type'] = test['Memory'].str.extract(r'(SSD|HDD)')

le.fit(test['Storage_Type'])
test['Storage_type_Enc']= le.transform(test['Storage_Type'])

test = pd.concat([test, pd.get_dummies(test['Company'], prefix='Company')], axis=1)
test = test.drop('Company', axis=1)

test = pd.concat([test, pd.get_dummies(test['TypeName'], prefix='TypeName')], axis=1)
test = test.drop('TypeName', axis=1)

test['ResolutionHeight'] = test['ScreenResolution'].str.extract(r'\d+x(\d+)')
# test.head()

test['CPU_Type'] = test['Cpu'].str.extract(r'(\bIntel\b|\bAMD\b|\bCore\s[^\d]+)')
test['Speed_GHz'] = test['Cpu'].str.extract(r'(\d+\.\d+)GHz')

test = pd.get_dummies(test, columns=['CPU_Type'], prefix='CPU_Type')

test['ResolutionHeight']=test['ResolutionHeight'].astype(int)
test['Speed_GHz']=test['Speed_GHz'].astype(float)

test.fillna(0, inplace=True)

test.drop(columns=['Memory','Storage_Type','Product','ScreenResolution','Cpu','laptop_ID','Inches','Gpu'],inplace=True)