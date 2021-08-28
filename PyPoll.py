# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
candidate_options = []
candidate_votes = {}
# Open the election results and read the file.
with open(file_to_load) as election_data:
    print(election_data)
    
    # To do: read and analyze the data here.
 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    # Print each row in the CSV file.
    
    for row in file_reader:
        #print(row)
        candidate_name = row[2]
        if not candidate_name in candidate_options:
            candidate_options.append(candidate_name)
            #Creando el elemento Diccionario    
            candidate_votes[candidate_name] = 1
        #Contar los votos que ya estan en la lista
        else:
            candidate_votes[candidate_name] += 1

        # 2. Add to the total vote count.
        total_votes += 1

with open(file_to_save, "w") as txt_file:
    txt_file.write("\n")
    txt_file.write("Election Results\n")
    txt_file.write("------------------\n")
    txt_file.write("Total Votes: " +str(total_votes)+"\n")
    txt_file.write("------------------\n")

    # 3. Print the total votes.
    print(total_votes)
    print(candidate_options)
    print(candidate_votes)

    # Winning Candidate and Winning Count Tracker
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0

    for k,v in candidate_votes.items():
        #Percent of the votes
        vote_percentage = (v / total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({v:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
    
    #Who win?
        if v>winning_count:
            winning_candidate = k
            winning_count = v
            winning_percentage = vote_percentage
    txt_file.write("--------------------\n")

# Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)


# winning_candidate_summary = (
#     f"-------------------------\n"
#     f"Winner: {winning_candidate}\n"
#     f"Winning Vote Count: {winning_count:,}\n"
#     f"Winning Percentage: {winning_percentage:.1f}%\n"
#     f"-------------------------\n")
# print(winning_candidate_summary)


# # Using the with statement open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Counties in the election\n")
# outfile.write("--------------------------\n")
# outfile.write("Arapahoe\nDenver\nJefferson")
# # Close the file
# outfile.close()

