# The data we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#import datetime as dt
#now = dt.datetime.now()
#print("The time right now is", now)

#Import appropriate dependencies
import csv
import os

#1 Assign a variable for the file to load and the path, 2 Assign variable to write txt file to directory
file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Open the election results and read the file, open analysis file and use "w" to write data to the file
with open(file_to_load) as election_data:

    #To do: Read and analyze data
    
    #1 Read file object with reader function (part of csv module)
    file_reader = csv.reader(election_data)
    
    #Print header row.
    headers = next(file_reader)
    print(headers)

    #2 How to print each row in the CSV file.
    #for row in file_reader:
        #print(row)

