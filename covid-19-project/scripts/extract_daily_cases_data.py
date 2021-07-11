#import required module
import pandas as pd
import numpy as np
import glob
import requests
import io
from datetime import timedelta, date

#function to calculate the date range
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

#function to extract the data from repo. This will also download the data on local-machine, if data is
#missing for the date then it will log that into seperate file.
def extract_data():
    start_date = date(2021, 1, 1)
    end_date = date.today()
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'
    for single_date in daterange(start_date, end_date):
        fromatted_string=single_date.strftime("%m-%d-%Y")
        url='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'+fromatted_string+'.csv'
        response = requests.get(url)
        if response.status_code == 200:
            covid_data = response.content
            df = pd.read_csv(io.StringIO(covid_data.decode('utf-8')))
            df.to_csv('/Users/saurabhvisal/Desktop/python_sandbox/python_sandbox/covid-19-project/extracted_data/cases_'+str(fromatted_string)+'.csv')
            #df.to_csv('/Users/saurabhvisal/Desktop/python_sandbox/python_sandbox/covid-19-project/extracted_data/cases_data.csv')
            #print(df.head())
        else:
            with open("/Users/saurabhvisal/Desktop/python_sandbox/python_sandbox/covid-19-project/log/log_file.txt", "a") as file1:
                file1.write("Data is not available for " + fromatted_string + "\n")
        continue

def transform_and_load():
    path = '/Users/saurabhvisal/Desktop/python_sandbox/python_sandbox/covid-19-project/extracted_data'
    all_files = glob.glob(path + "/*.csv")
    df_files = (pd.read_csv(f) for f in all_files)

    df = pd.concat(df_files, ignore_index=True)

    #basic transformation
    df['Province_State'] = df['Province_State'].str.strip()
    df['Country_Region'] = df['Country_Region'].str.strip()
    df['Last_Update'] = pd.to_datetime(df['Last_Update'])

    #load the data for required countries only
    required_data = df[(df['Country_Region']=='India') | (df['Country_Region']=='Australia') | (df['Country_Region']=='United Kingdom') | (df['Country_Region']=='US') | (df['Country_Region']=='Germany')]

    # select required columns
    cases_death = required_data[['Province_State', 'Country_Region', 'Last_Update', 'Confirmed', 'Deaths','Recovered','Active','Incident_Rate','Case_Fatality_Ratio']]
    cases_death.to_csv('/Users/saurabhvisal/Desktop/python_sandbox/python_sandbox/covid-19-project/cases_data/cases_death.csv')

#call to the function
extract_data()
transform_and_load()