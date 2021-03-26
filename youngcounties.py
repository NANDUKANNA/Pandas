import pandas as pd
#reading a csv file
df = pd.read_csv("county_demographics (1).csv")
#extracting 10 youngest counties
young = df.nlargest(10, ['Age.Percent Under 18 Years'])
#printing youngest countries
print(young)

young.to_csv("YoungestCounties.csv")