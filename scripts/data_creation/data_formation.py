import pandas as pd


import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]

df  = pd.DataFrame()

count = 1

for f in files:

	if f != 'data_formation.py':

		data = pd.read_csv(f,delimiter = '\t')

		if count == 1:
			df['patients'] = data['Composite Element REF']
		df['patient_'+str(count)] = data['Beta_value']
		count = count + 1


df = df.set_index('patients').T

df['stage'] = [1]*(count-1)

df.to_csv('OvaryCancer.csv')