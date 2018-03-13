#pyboss
#Dependencies
import csv
import datetime

#Name csv and text files
emp_csv = "employee_data2.csv"
results = "pyboss.txt"

with open( 'employee_data2.csv', newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")


#Create list placeholders
emp_ID = []
first_name = []
last_name = []
date_of_birth = []
ssNumber = []
state_abbrev = []


#Start building the table
for row in csvreader:

    #Add employee ID
    emp_ID.append(row[0])
    print(emp_ID)    

    #Split first and last name.
    name = row[1].split()row[0] 
    first_name.append(name_list[0])
    last_name.append(name_list[1])
    print(first_name_str)

    #DOB
    date_of_birth.append(row[2])


    #SSN
    str(row[3])[-4:].rjust(len(str(row[3])), "*")
     try:
       List of States
       us_state_abbrev = {
       'Alabama': 'AL',
       'Alaska': 'AK',
       'Arizona': 'AZ',
       'Arkansas': 'AR',
       'California': 'CA',
       'Colorado': 'CO',
       'Connecticut': 'CT',
       'Delaware': 'DE',
       'Florida': 'FL',
       'Georgia': 'GA',
       'Hawaii': 'HI',
       'Idaho': 'ID',
       'Illinois': 'IL',
       'Indiana': 'IN',
       'Iowa': 'IA',
       'Kansas': 'KS',
       'Kentucky': 'KY',
       'Louisiana': 'LA',
       'Maine': 'ME',
       'Maryland': 'MD',
       'Massachusetts': 'MA',
       'Michigan': 'MI',
       'Minnesota': 'MN',
       'Mississippi': 'MS',
       'Missouri': 'MO',
       'Montana': 'MT',
       'Nebraska': 'NE',
       'Nevada': 'NV',
       'New Hampshire': 'NH',
       'New Jersey': 'NJ',
       'New Mexico': 'NM',
       'New York': 'NY',
       'North Carolina': 'NC',
       'North Dakota': 'ND',
       'Ohio': 'OH',
       'Oklahoma': 'OK',
       'Oregon': 'OR',
       'Pennsylvania': 'PA',
       'Rhode Island': 'RI',
       'South Carolina': 'SC',
       'South Dakota': 'SD',
       'Tennessee': 'TN',
       'Texas': 'TX',
       'Utah': 'UT',
       'Vermont': 'VT',
       'Virginia': 'VA',
       'Washington': 'WA',
       'West Virginia': 'WV',
       'Wisconsin': 'WI',
      'Wyoming': 'WY',

    #Loop through states
    for row in csvreader:
        if state in us_state_abbrev.value():
            state_abbrev.append(row[4])
        elif:
            next row
     except SyntaxError:
        pass
      else:

#Zip lists together.
pyBoss = zip(empID,first_name, last_name, date_of_birth, ssNumber, state_abbrev)


with open("pyboss.txt", "w") as text_file:
    print(pyBoss)
