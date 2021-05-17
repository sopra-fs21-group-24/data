import pandas as pd

data = pd.read_csv("./data.csv")
# number_of_countries = data["Country"].nunique()
# print(number_of_countries)

values = data.iloc[:,:].values
# print(data.head())
# print(data.describe())
# print(data.shape)

currentCountry = ""
currentCountryCounter = 0
overallIndex = 0

for item in values:
    if (currentCountry == ""):
        currentCountry = item[1]
        currentCountryCounter = 0

    currentCountryCounter = currentCountryCounter + 1
    if (currentCountryCounter > 10):
        data.drop([overallIndex], inplace=True)
        if (currentCountry != item[1]):
            currentCountry = item[1]
            currentCountryCounter = 0
    overallIndex = overallIndex+1
    
data['Zoom'] = 8

data.to_csv("./results.csv", index=False, header=False)


    # print(itsem)