#import modules 
import os
import csv



#set path for file
election_datapath = os.path.join("election_data_1.csv") #,os.path.join("election_data_2.csv")

election_dict = []

#open csv files reading data into dictionary
with open(election_datapath, newline="") as csvfile:
     election_data = csv.DictReader(csvfile, delimiter=",")
    
     for row in election_data:
         voter_ID = row["Voter ID"]
         county = row["County"]
         candidate = row["Candidate"]
         election_dict.append(
             {
                 "Voter ID": row["Voter ID"],
                 "County": row["County"],
                 "Candidate": row["Candidate"]
             }
         )
    # for candidate in election_data:
    #     print(list.index(candidate))


   
from collections import Counter
candidatelist = []
for canditate in election_data:
    candidatelist.append(name)

    #print(Counter())

    #print("Total Votes: ", (str(total_votes))
    #print("--------------------------------")

# for key, value in election_dict : 
#     print (key,value)


# Get a count of votes by candidate 
#candidate_votes
# votePercent = round(int(candidate_votes/total_votes)*100),2)

# # Print out the candidate's name and their percentage of votes 
# print(candidate + votePercent + candidate_votes)

# #claim winner (conditionals)
