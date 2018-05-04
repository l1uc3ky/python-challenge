#import modules 
import os
import csv

election_datapath = os.path.join("election_data_1.csv") #,os.path.join("election_data_2.csv")

#open csv files reading data into dictionary
with open(election_datapath, newline="") as csvfile:
     election_data = csv.reader(csvfile, delimiter=',')
    

#make dictionary to store candidates
candidates = {}

# Skip the first line because it contains the headers.
next(csvfile)

# Loop through the rows of the csv
    for row in csvreader:
    
    # Pull the candidate name for the row
        candidate = row[2]

        # If there are no votes for the candidate, add to the dictionary with 1 vote
        if candidate not in candidates:
            candidates[candidate] = 1
        # Else increment the votes by 1    
        else:
            numvotes = 1 + candidates[candidate]
            candidates[candidate] = numvotes
        
    # Loop through dictionary to total votes 
    totalVotes = 0
    maxVotes = 0

    for person in candidates:
        totalVotes += candidates[person]
        if candidates[person] > maxVotes:
            winner = person
            maxVotes = candidates[person]

    # Print results
    print("Election Results")
    print("-" * 25)
    print(f'Total Votes: {totalVotes}')
    print("-" * 25)
    # Use a loop since we're printing data on each element in the candidate dictionary
    for candidate in candidates:
        print(f'{candidate}: {round(100*candidates[candidate]/totalVotes,1)}% ({candidates[candidate]})')
    print("-" * 25)
    print(f'Winner: {winner}')
    print("-" * 25)

# Define where to print the election results 
output_file = os.path.join('PyPoll','election_results.txt')

# Write into  output_file 
with open(output_file, "w", newline='') as datafile:

    # Write the results to the txt file
    print("Election Results", file = datafile)
    print("-" * 25, file = datafile)
    print(f'Total Votes: {totalVotes}', file = datafile)
    print("-" * 25, file = datafile)
    # Use a loop since we're writing data on each element in the candidate dictionary
    for candidate in candidates:
        print(f'{candidate}: {round(100*candidates[candidate]/totalVotes,1)}% ({candidates[candidate]})', file = datafile)
    print("-" * 25, file = datafile)
    print(f'Winner: {winner}', file = datafile)
    print("-" * 25, file = datafile)