# Import modules os and csv
import os
import csv

# Define variables
count = 0
candidate_list = []
unique_candidate = []
vote_count = []
vote_percent = []

#Path to file from resource folder
election_data_csv = os.path.join("Resources", "election_data.csv")

#Open and read csv file
with open(election_data_csv, newline=" ") as csvfile:

    csv_reader = csv_reader(csvfile, delimiter=",")