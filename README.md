# Colorado Election Analysis
## Overview of Election Audit
An employee from the Colorado Board of Elections was interested in an automated way to analyze data from a congressional election.

The Colorado Board of Elections wanted the followng tasks completed:

1. Calculate total number of votes cast.
2. Determine all candidates votes were cast for.
3. Calculate total votes and percentage of total votes received by each candidate.
4. Calcuate the winning candidate based on the popular vote.
5. Determine all counties votes were cast in.
6. Determine vote count for each county.
7. Determine percentage of votes for each county.
8. Determine the county with the highest turnout.

## Election Audit Results
### Resources 
Python 3.6.7 was used to analyze the voting data. Visual Studio code 1.63.2 was used as a text editor. The data source used was [election-analysis.csv](election-analysis.csv). 

### Methods

The following is the code, written in python.
  # -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

  #Add our dependencies.
  import csv
  import os

  #Add a variable to load a file from a path.
  file_to_load = os.path.join("Resources", "election_results.csv")
  # Add a variable to save the file to a path.
  file_to_save = os.path.join("..", "election_results.txt")

  #Initialize a total vote counter.
  total_votes = 0

  #Candidate Options and candidate votes.
  candidate_options = []
  candidate_votes = {}

  #1: Create a county list and county votes dictionary.
  county_options = []
  county_votes = {}

  #Track the winning candidate, vote count and percentage
  winning_candidate = ""
  winning_count = 0
  winning_percentage = 0

  #2: Track the largest county and county voter turnout.

  largest_voting_county = []
  largest_county_count = 0
  largest_county_percentage = 0


  #Read the csv and convert it into a list of dictionaries
  with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

  #Save the results to our text file.
  with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        county_vote_count = county_votes.get(county_name)

        # 6c: Calculate the percentage of votes for the county.
        percentage_county_votes = float(county_vote_count)/float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (
            f"{county_name}: {percentage_county_votes:.1f}% ({county_vote_count:,})\n")

        print(county_results)

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_vote_count > largest_county_count) and (percentage_county_votes > largest_county_percentage):
            largest_county_count = county_vote_count
            largest_voting_county = [county_name]
            largest_county_percentage = percentage_county_votes
        
        # 6f1: In the case of a tie, add an elif statement.

        elif (county_vote_count == largest_county_count) and (percentage_county_votes == largest_county_percentage):
            largest_voting_county.append(county_name)


    # 7: Print the county with the largest turnout to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"County with Largest Vote Count: {' and '.join(largest_voting_county)}\n"
        f"County Vote Count: {largest_county_count:,}\n"
        f"County Percentage: {largest_county_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

### Results 
#### Voter Turnout by County 

The total number of votes cast in the election was 369,711. There were three voting counties in the precinct: Jeffereson, Denver, and Arapahoe. The couty results are below:

County Votes:<br>
Jefferson: 10.5% (38,855)<br>
Denver: 82.8% (306,055)<br>
Arapahoe: 6.7% (24,801)<br>

The county with the greatest voter turnout was Denver, with a county vote count of 306,055 (82.8%).

#### Popular Election Results
The candidates for the congressional election included Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. Vote percentage and vote count for each candidate can be found below:

Charles Casper Stockham: 23.0% (85,213)<br>
Diana DeGette: 73.8% (272,892)<br>
Raymon Anthony Doane: 3.1% (11,606)<br>

The winner of the election by popular vote was Diana DeGette with 272,892 votes (73.8%).

## Election Audit Summary

This script can be easily adapted for elections in all catergories city-wide, county-wide, and state-wide. To ensure accuracy, efficiency, and cost-avings, I suggest implementing this method for all elections going forward. To use for city-wide elections, for example, the county results could be taken out and instead only the results of the city-wide election could be shown. The code needs to be updated to take into consideration the unlikely event of a tie. You will see in the python code, I have done this for the county data. This could also be applied for the popular vote data in any type of election.



