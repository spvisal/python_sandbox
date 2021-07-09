#import required module
import pandas as pd
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
    start_date = date(2021, 7, 9)
    end_date = date(2021, 7, 12)
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'
    for single_date in daterange(start_date, end_date):
        fromatted_string=single_date.strftime("%m-%d-%Y")
        url='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'+fromatted_string+'.csv'
        response = requests.get(url)
        if response.status_code == 200:
            covid_data = response.content
            df = pd.read_csv(io.StringIO(covid_data.decode('utf-8')))
            df.to_csv('/Users/saurabhvisal/Desktop/python_sandbox/python_sandbox/covid-19-project/extracted_data/cases_'+str(fromatted_string)+'.csv')
            #print(df.head())
        else:
            with open("/Users/saurabhvisal/Desktop/python_sandbox/python_sandbox/covid-19-project/log/log_file.txt", "a") as file1:
                file1.write("Data is not available for " + fromatted_string + "\n")
        continue

#call to the function
extract_data()