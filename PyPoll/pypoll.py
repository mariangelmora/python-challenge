# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:01:41 2024

@author: maria
"""

import os
import csv

#path to find the file
csvpath = os.path.join(r"C:\Users\maria\Desktop\Bootcamp\python\Python challenge\Starter_Code\PyPoll\Resources1\election_data.csv")

#variable to keep track of the vote count
total_votes = 0
#empty list to add candidates
candidates_votes = {}

#open the file
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    #start from the second row
    csv_header = next(csvreader)
    print(f'csvheader: {csv_header}')
    
    # Iterate through each row in the CSV
    for i in csvreader:
        # get candidates
        candidate = i[2]

        # calculate the total votes 
        total_votes += 1

      
        if candidate in candidates_votes:
            candidates_votes[candidate] += 1
        else:
            candidates_votes[candidate] = 1
            
# find the winner among all the candidates            
winner = max(candidates_votes, key=candidates_votes.get)    

#results
print("Election Results")
print("-------------------------")
# print the total votes cast
print(f"Total Votes: {total_votes}")
print("-------------------------")

#candidates who received votes 
print("Candidates who received votes:")
for candidate, votes in candidates_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")