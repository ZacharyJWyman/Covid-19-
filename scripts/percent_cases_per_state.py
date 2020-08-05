import pandas as pd
import numpy as np



url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
data = pd.read_csv(url, error_bad_lines = False)

start_date = '2020-07-10'
end_date = '2020-07-12'

#tiemframe data by most(cases) i.e. will be most recent
mask = (data['date'] > start_date) & (data['date'] <= end_date)
new_data = data.loc[mask]

#pop data per state
population_data = pd.read_csv(r"C:\Users\19712\Documents\Python Scripts\population estimates.txt", sep = '\t', thousands = ',', header = int())
population_data.columns = ['rank', 'state', 'population', 'percent of Tot']

population_data = population_data.drop(columns=['rank', 'percent of Tot'])

#merge data
complete_data = pd.merge(data, population_data, how='inner', on='state')

percent_cases_per_state = complete_data['cases'] / complete_data['population'] * 100
complete_data['virus % per state'] = percent_cases_per_state

complete_data.to_excel('covid_19_percents_per_state.xlsx', index='False')
    
    
    
    
