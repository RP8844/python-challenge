    #Import the files
import csv
import os
    # Assign the variables
total_vote = 0
total = 0
candidate_votes = {}
voter_id = 0
candidate_list = []
    # Path to collect data from the resources file
data = os.path.join('Resources','election_data.csv')
    # Define the data
with open(data) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    # Determine the total number of votes cast
    # Determine the complete list of candidates who received votes
    for row in reader:
        total_vote += 1
        voter_id += 1
    # Determine the complete number of votes each candidate won
        candidates = (row[2])
        if candidates not in candidate_list:
            candidate_list.append(candidates)
            candidate_votes[candidates] = 0
        candidate_votes[candidates] += 1
    print("Election Results")
    print("---------------------")
    print(f"Total Votes: {voter_id}")
    print("---------------------")
    # Determine the percentage of votes each candidate won
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        votes_percentage = float(votes)/float(total_vote) * 100
        output = f"{candidate}: {votes_percentage:.3f}% ({votes})\n"
        print(output)
    print("---------------------")
    max_votes = max(candidate_votes,key=candidate_votes.get)
    # Determine the winner of the election based on the most popular votes  
    print(f"Winner: {max_votes}")   
    print("---------------------")
