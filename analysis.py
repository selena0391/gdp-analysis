import csv
import math

def get_highest_gdp(data, year):
    highest = float(data[0][year])
    stateName = ""
    for state in data:
        if float(state[year]) > highest:
            highest = float(state[year])
            stateName = state['GeoName']
    return stateName


def get_lowest_gdp(data, year):
    lowest = float(data[0][year])
    for state in data:
        if float(state[year]) < lowest:
            lowest = float(state[year])
            stateName =  state['GeoName']
    return stateName

def get_state_gdp(data, state, year):
    for d in data:
        if d['GeoName'] == state:
            return float(d[year])
   
        

# save each row into a list (TODO: change to your path!)
list_data = []
with open("state_gdp_analysis.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)

# get highest gdp for 2020 using "get_highest_gdp(list_data, '2020')"
print("The state with highest gdp is ", get_highest_gdp(list_data, '2020'))

# get lowest gdp for 2020 using "get_lowest_gdp(list_data, '2020')"
print("The state with lowest gdp is ", get_lowest_gdp(list_data, '2020'))

prev = get_state_gdp(list_data, "New York", "2019")
new = get_state_gdp(list_data, "New York", "2020")

print("The change in New York GDP is ", new - prev )


#Challenge 1

years = [str(year) for year in range(1997, 2021)]
highStates = {}
lowStates ={}

for year in years:
    highStates[year] = get_highest_gdp(list_data,year)
    lowStates[year] = get_lowest_gdp(list_data, year)

print(highStates)
print(lowStates)

field_names = ["Year", "State with highest GDP"]

with open('highest_gdp.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(field_names)
    for key, value in highStates.items():
        writer.writerow([key,value])

field_namesLow = ["Yesr", "State with lowest GDP"]

with open('lowest_gdp.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(field_namesLow)
    for key, value in lowStates.items():
        writer.writerow([key,value])


#Challenge 2

def get_percent_change(data, state, year1, year2):
    first_year = get_state_gdp(data, state, year1)
    second_year = get_state_gdp(data, state, year2)

    return (second_year-first_year)/first_year * 100


print("The percentage change for New York between years 2019 and 2020 is ", math.ceil(get_percent_change(list_data, "New York", '2019', '2020')), "%")



