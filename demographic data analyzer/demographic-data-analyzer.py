import numpy as np
import pandas as pd

df = pd.read_csv('adult-data.csv')

#Count the people of each race
people_count_race = df['race'].value_counts()


#Average age of men
average_age_men = round(df[df['sex']=='Male']['age'].mean(),1)


#Percentage of people who have a Bachelor's degree
people_bachelor = round(df[df['education']=='Bachelors'].shape[0]/df.shape[0]*100,1)

#Percentage of people with Bachelors, Masters or Doc make than 50k
Advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
More_than_50k = df['salary']=='>50K' 
percentage_rich = round((Advanced_education & More_than_50k).sum()/Advanced_education.sum()*100,1)

#Percentage of people without Bachelors, Masters or Doc make than 50k
Advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
More_than_50k = df['salary']=='>50K' 
percentage_rich_no = round((~Advanced_education & More_than_50k).sum()/Advanced_education.sum()*100,1)


#Minimum number of hours a person works per week
min_hours_work = df['hours-per-week'].min()


#Percentage of people who work the minimum number of hours per week have a salary more than 50K
w1 = df['hours-per-week']==min_hours_work
percentage_less_work = round((w1 & More_than_50k).sum()/w1.sum()*100,1)


#Country with highest percentage of people that earn >50K
q = (df[More_than_50k]['native-country'].value_counts() \
                                / df['native-country'].value_counts() * 100).sort_values(ascending=False)
highest_earning_country = q.index[0]
highest_earning_country_percentage = round(q.iloc[0], 1)

#Identify the most popular occupation for those who earn >50K in India
Popular_occupation_India = df[(df['native-country'] == 'India') & More_than_50k] \
                          ['occupation'].value_counts().index[0]


print("Number of each race:\n", people_count_race) 
print("Average age of men:", average_age_men)
print(f"Percentage with Bachelors degrees: {people_bachelor}%")
print(f"Percentage with higher education that earn >50K: {percentage_rich}%")
print(f"Percentage without higher education that earn >50K: {percentage_rich_no}%")
print(f"Min work time: {min_hours_work} hours/week")
print(f"Percentage of rich among those who work fewest hours: {percentage_less_work}%")
print("Country with highest percentage of rich:", highest_earning_country)
print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
print("Top occupations in India:", Popular_occupation_India)
