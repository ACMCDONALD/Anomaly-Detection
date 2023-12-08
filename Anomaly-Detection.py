#Assignment 7 - Anomaly Detection
#Description: Read key card log file and look for anomalies in the data
#Created By: Andrew McDonald
#Date Created: December 1, 2023
#Date Modified: December 5, 2023

#import the csv module to read csv files
import csv

#define Variables
inNotOut = "Employee carded IN but did not card OUT"
outNotIn = "Employee carded OUT but did not card IN"
separator = "======================================="

#open the csv file cardKeyLog.txt
with open('cardKeyLog.csv') as csv_file:
    #set the scv_reader variable and look for the delimiter ',' when parsing the csv file
    csv_reader = csv.reader(csv_file, delimiter=',')

    #initialize line_count
    line_count = 0

    #begin to parse the csv_file for anomalies
    for row in csv_reader:
            try:
                #ignore the first row of data (headers)
                if line_count == 0:
                    line_count += 1
                #start parsing the data
                else:
                    #look for a 0 in row 3 (no punch in). If present output anomaly data to text file
                    if int(row[3]) == 0:
                        output = outNotIn
                        employeeID = row[0]
                        month = row[2]
                        day = row[1]
                        #output to ANOMALIES.txt per the ### OUTPUT FORMAT ### below
                        outputFile = open ('ANOMALIES.txt', 'a') #open text file
                        outputFile.write(f'Employee ID: {employeeID} Month: {month} Day: {day}\n{output}\n{separator}\n') #write data
                        outputFile.close() #close text file
                        line_count += 1 #increment line_count by 1
                    #look for a 0 in row 7 (no punch out). If present output anomaly data to text file   
                    elif int(row[7]) == 0:
                        output = inNotOut
                        employeeID = row[0]
                        month = row[2]
                        day = row[1]
                        #output to ANOMALIES.txt per the ### OUTPUT FORMAT ### below
                        outputFile = open ('ANOMALIES.txt', 'a') #open text file
                        outputFile.write(f'Employee ID: {employeeID} Month: {month} Day: {day}\n{output}\n{separator}\n') #write data
                        outputFile.close() #close text file
                        line_count += 1 #increment line_count by 1
                    else:
                        #if none of the above conditions are met, increment line_count by 1
                        line_count += 1
            except:
                    #output error to user if present
                    print("An error has occured")
                    
### OUTPUT FORMAT ###
# employeeID month day
# description (inNotOut -or- outNotIn)
# separator
