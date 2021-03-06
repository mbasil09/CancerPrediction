import pandas as pd


import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]

df  = pd.DataFrame()

count = 1

number = 17

for f in files:

	if f != 'data_continuation.py' and f != 'OvaryCancer.csv':
		data = pd.read_csv(f,delimiter = '\t')
		if count == 1:
			df['patients'] = data['Composite Element REF']
		df['patient_'+str(count+number)] = data['Beta_value']
		count = count + 1

df = df.set_index('patients').T

df['stage'] = [2]*(count-1)

#print(df.head())

df.to_csv('OvaryCancer_temp.csv')

#print(df.head())

#print(df.shape)

df_new = pd.read_csv('OvaryCancer_temp.csv')
df_new.rename(columns={'Unnamed: 0':'patients'}, inplace=True)
print(df_new.head())

#print(df.head())

data = pd.read_csv('OvaryCancer.csv')
data.rename(columns={'Unnamed: 0':'patients'}, inplace=True)
print(data.head())
bigdata = pd.concat([data,df_new], ignore_index = True)
# bigdata.rename( columns={'Unnamed: 0':'patients'}, inplace=True )
#bigdata = bigdata.reset_index(drop=True)
#print(bigdata.tail())


print(bigdata.tail(10))


bigdata.to_csv('OvaryCancer_2.csv')