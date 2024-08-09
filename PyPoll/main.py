# Import modules os and csv
import os
import csv

# Define variables
total_vote_count = 0
candidate_vote_count = 0
winner_vote_count = 0
winner = " "

# Define lists
total_candidate_list = []
unique_candidate_list =[]
count_list =[]
percentage_list =[]


#Path to file from resource folder
election_data_csv = os.path.join("Resources", "election_data.csv")


status = True

#Open and read csv file
with open(election_data_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    # First row
    csv_header = next(csv_reader)
    # print(f"Header: {csv_header}")

      
    #Read through rows
    for row in csv_reader:
        #List to store all entries for each candidate
        total_candidate_list.append(row[2])

        #Calculate number of votes
        total_vote_count += 1

        #Create list of candidate names (unique)
        candidate = row[2]
        if candidate not in unique_candidate_list:
            unique_candidate_list.append(candidate)

#Total number of votes and percentage for each candidate with winner
#loop through candidate list  then search for winner

    for candidate_name in unique_candidate_list:
        for value in total_candidate_list:
            #total votes and percentage by each candidate
            if value == candidate_name:
                candidate_vote_count += 1

        vote_percentage = round(((candidate_vote_count/total_vote_count)*100),3)
        #print(candidate_name, vote_percentage)

        #Make list to store collection for candidate
        count_list.append(candidate_vote_count)
        percentage_list.append(vote_percentage)

        #Who won?
        if candidate_vote_count > winner_vote_count:
                winner_vote_count = candidate_vote_count
                winner = candidate_name
        #Re-run 
        candidate_vote_count = 0

# Print Analysis
#Print 
print("Election Results")
print("--------------------")
print(f"Total Votes: {total_vote_count}")
print("--------------------")
#Print stats for each candidate
for (name, percentage, count) in zip(unique_candidate_list, percentage_list, count_list):
    print(f"{name}: {percentage}% ({count})")
print("--------------------")
print(f"Winner: {winner}")
print("--------------------")

# Write Analysis to text file
output_path = os.path.join("analysis", "financial_analysis.txt")
with open(output_path, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("--------------------\n")
    txtfile.write(f"Total Votes: {total_vote_count}\n")
    txtfile.write("--------------------\n")
    for (name, percentage, count) in zip(unique_candidate_list, percentage_list, count_list):
        txtfile.write(f"{name}: {percentage}% ({count})\n")
    txtfile.write("--------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("--------------------\n")
print(f"\nResults have been written to {output_path}")
