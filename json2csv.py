import pandas as pd
df = pd.read_json ('sample.json')
print (df)
import warnings
warnings.filterwarnings('ignore')

df=df.iloc[0:5]
df1=df.loc[:,'data']

#removing the new line
df1 = df1.replace(r"\n"," ",regex=True)

#converting the df into list
df2=pd.DataFrame([df1[0],df1[1]['lat'],df1[1]['lng'],df1[2],df1[3],df1[4]['type'],df1[4]['details']['owner'],df1[4]['details']['company_reg'],df1[4]['details']['owner_type'],df1[4]['details']['owner_address'],df1[4]['details']['date_added'],df1[4]['details']['country']]).transpose()


#saving to csv
df2.to_csv('C://Users//ashish//Desktop//UK PROPERTY//EN1 1AA//Address_detail//JSON//AGL119189.csv',index=False)
