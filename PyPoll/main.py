# Import to enable interaction for operating system and file type
import os
import csv
from pathlib import Path

# Add csv path
csvpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Rescources', 'election_data.csv')

# Set starting variables
poll = {}
tot_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open csv
with open(csvpath, newline='', encoding="utf-8") as csvfile:

    # Read csv
    csvreader = csv.reader(csvfile, delimiter=',')

    # Don't include header in counts
    header = next(csvreader)

    # DETERMINE TOTAL NUMBER VOTES 
    for row in csvreader:
        tot_votes += 1

        # DETERMINE TOTAL NUMBER VOTES EACH CANDIDATE RECEIVED
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1

# Create lists to store values
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
can_votes = [khan, correy, li, otooley]

# Candidate vote percentages
khan_per = (khan_votes / tot_votes) * 100
correy_per = (correy_votes / tot_votes) * 100
li_per = (li_votes / tot_votes) * 100
otooley_per = (otooley_votes / tot_votes) * 100

# Calculate Winner 
winner_election = max(khan, correy, li, otooley)

    # Name Winner
    if winner_election == khan_votes:
        winner = "Khan"
    elif winner_election == correy_votes:
        winner = "Correy"
    elif winner_election == li_votes:
        winner = "Li"
    else:
        winner = "O'Tooley" 

# PRINT ANALYSIS
print(f"Election Results")
print(f"--------------------------------")
print(f"Total Votes: {total}")
print(f"--------------------------------")
print(f"Kahn: {khan_per:.3f}% ({khan})")
print(f"Correy: {correy_per:.3f}% ({correy})")
print(f"Li: {li_per:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_per:.3f}% ({otooley})")
print(f"--------------------------------")
print(f"Winner: {winner}")
print(f"--------------------------------")

# EXPORT TEXT 

# Create file path
output = os.path.join(".", 'output.txt')
with open(output,"w") as PyPoll:

    # Write txt
    PyPoll.write(f"Election Results\n")
    PyPoll.write(f"--------------------------------")
    PyPoll.write(f"Total Votes: {total}\n")
    PyPoll.write(f"--------------------------------\n")
    PyPoll.write(f"Kahn: {khan_per:.3f}% ({khan})\n")
    PyPoll.write(f"Correy: {correy_per:.3f}% ({correy})\n")
    PyPoll.write(f"Li: {li_per:.3f}% ({li_votes})\n")
    PyPoll.write(f"O'Tooley: {otooley_per:.3f}% ({otooley})\n")
    PyPoll.write(f"--------------------------------\n")
    PyPoll.write(f"Winner: {winner}\n")
    PyPoll.write(f"--------------------------------\n")
