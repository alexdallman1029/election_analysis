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

#Initialize variable for total votes
total_votes = 0

#Create list variable for candidates
candidate_options = []

#Create dictionary to pair candidate names with candidate vote counts
candidate_votes = {}

#Create variables for winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file, open analysis file and use "w" to write data to the file
with open(file_to_load) as election_data:

    #To do: Read and analyze data
    
    #1 Read file object with reader function (part of csv module)
    file_reader = csv.reader(election_data)
    
    #Print header row.
    headers = next(file_reader)

    #Count total votes using total_votes initalized before the open function and print
    for row in file_reader:
        #Add to total vote count
        total_votes += 1
    
        #Get names of each candidate
        #Declare new list
        candidate_name = row[2]
    
        #Add candidate_name list to candidate_options list
        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)
    
            #Pair candidate vote counts to candidates
            #Initalize candidate_votes
            candidate_votes[candidate_name] = 0

        #Tally candidate votes for each candidate
        candidate_votes[candidate_name] += 1

#Save the results to the text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n")
    
    print(election_results, end="")

    txt_file.write(election_results)

    #Find each candidate's percentage of votes using for loop
    for candidate_name in candidate_options:
        
        #Define variable for votes
        votes = candidate_votes[candidate_name]

        percentage_votes = float(votes)/float(total_votes)*100
        
        candidate_results = (
            f"{candidate_name}: {percentage_votes:.1f}% ({votes:,})\n")
        
        print(candidate_results)

        txt_file.write(candidate_results)

        #Determine winning vote count and candidate
        #Determine if votes are greater than winning count
        if (votes > winning_count) and (percentage_votes > winning_percentage):
        
            winning_count = votes
            winning_percentage = percentage_votes
            winning_candidate = candidate_name

    #Print winning outcomes using a variable
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n"
    )
    
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)
