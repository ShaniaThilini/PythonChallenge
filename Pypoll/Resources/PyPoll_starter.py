# -*- coding: UTF-8 -*-
"""PyPoll Election Analysis."""

import csv
import os

# Files to load and output
file_to_load = os.path.join("C:\Users\Unagi\OneDrive\Documents\GitHub\PythonChallenge\Pypoll\Resources\election_data.csv")
file_to_output = os.path.join("C:\Users\Unagi\OneDrive\Documents\GitHub\PythonChallenge\Pypoll\Analysis")

# Initialize variables to track the election data
total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    # Print the final vote count
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate_name in candidate_votes:
        # Get the vote count and calculate the percentage
        votes = candidate_votes[candidate_name]
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        # Print and save each candidate's vote count and percentage
        candidate_results = (f"{candidate_name}: {vote_percentage:.3f}% ({votes})\n")
        print(candidate_results, end="")
        txt_file.write(candidate_results)

    # Generate and print the winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
