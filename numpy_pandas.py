# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13AS_Tt7o0uGzSwLNUYRL7H_uRvbj47HW
"""

import urllib

urllib.request.urlretrieve('https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv','italy-covid-daywise.csv')

import pandas as pd

covid=pd.read_csv('italy-covid-daywise.csv')

covid

type(covid)

covid_df=covid.copy()

covid_df

total_cases=covid_df.new_cases.sum()
total_tests=covid_df.new_tests.sum()

positive_rate=total_cases/total_tests

print(total_cases,total_tests)

positive_rate

high_ratio=covid_df[covid_df.new_cases/covid_df.new_tests > positive_rate]

high_ratio

covid_df['positive_rate']=covid_df.new_cases/covid_df.new_tests

covid_df

covid_df.drop(columns=['positive_rate'],inplace=True)

covid_df

covid_df.sort_values('new_cases',ascending=False).tailm(10)

covid_df.loc[165:176]

covid_df.at[172,'new_cases']=((covid_df.at[171,'new_cases'] + covid_df.at[173,'new_cases'])/2)

covid_df.at[172,'new_cases']

covid_df['year']=pd.DatetimeIndex(covid_df.date).year

covid_df['month']=pd.DatetimeIndex(covid_df.date).month

covid_df['day']=pd.DatetimeIndex(covid_df.date).day

covid_df['week']=pd.DatetimeIndex(covid_df.date).weekday

covid_df

covid_df_april=covid_df[covid_df.month== 4]

covid_df_metr=covid_df_april[['new_cases','new_tests','new_deaths']]

covid_april=covid_df_metr.sum()

covid_april

covid_df[covid_df.month==4][['new_cases','new_tests','new_deaths']].sum()

covid_df[covid_df.month== 4][['new_cases','new_tests','new_deaths']].mean()

covid_month_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].sum()

covid_month_df

covid_df['total_cases'] = covid_df.new_cases.cumsum()

covid_df

urllib.request.urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv',
            'locations.csv')

location=pd.read_csv('locations.csv')

location

covid_df['location']='Italy'

covid_df

merge_result=covid_df.merge(location,on="location")

merge_result

merge_result['cases_per_million']=merge_result.new_cases * 1e6/merge_result.population
merge_result['tests_per_million']=merge_result.new_tests * 1e6/merge_result.population
merge_result['deaths_per_million']=merge_result.new_deaths * 1e6/merge_result.population

merge_result

result=merge_result[['date','new_cases','new_deaths','new_tests','cases_per_million','tests_per_million','deaths_per_million','month']]

result

result.to_csv('result.csv',index=None)

result.set_index('month',inplace=True)

result

result.new_deaths.plot()
result.new_cases.plot();

result['month']=pd.DatetimeIndex(result.date).month