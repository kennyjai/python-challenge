import os
import csv

pypollCSV = os.path.join('Resources', 'election_data.csv')

with open(pypollCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip the header
    csv_header = next(csvfile)

    #create a dictionary to gather all the results
    voter_results = {}
    totalvotes = 0

    for row in csvreader:

        # to get total amount of votes from the data    
        totalvotes += 1

        # build a dictionary that includes candidate and adds a count for each vote
        # if the candidate is not in the key, add a new dict key and start a new counter
        if str(row[2]) in voter_results:
            voter_results[str(row[2])] += 1
        else:
            voter_results[str(row[2])] = 1

# create lists from dictionary of the list of candidates and votes per candidate
votes_per_candidate = list(voter_results.values())
candidates = list(voter_results.keys())

#using votes_per_candidates list, create a new list getting the percentage of number votes over total votes
percentage_count = ['{0:.3f}'.format((x / totalvotes)*  100) for x in votes_per_candidate]

'''# we can use zip for reference to check our data
cleandata = zip(candidates,votes_per_candidate,percentage_count)
#for x in cleandata:
#    print(x)'''

# determine the winner based on most amount of votes, select the max from dictionary values
winner = max(voter_results.keys(), key=(lambda k: voter_results[k]))

# print our analysis
print(f'Election Results')
print(f'----------------------------------------')
print(f'Total Votes: ' + str(totalvotes))
print(f'----------------------------------------')
print(candidates[0]+": ",str(percentage_count[0]) + "% (" + str(votes_per_candidate[0]) + ")")
print(candidates[1]+": ",str(percentage_count[1]) + "% (" + str(votes_per_candidate[1]) + ")")
print(candidates[2]+": ",str(percentage_count[2]) + "% (" + str(votes_per_candidate[2]) + ")")
print(candidates[3]+": ",str(percentage_count[3]) + "% (" + str(votes_per_candidate[3]) + ")")
print(f'----------------------------------------')
print(f'Winner: ',winner)
print(f'----------------------------------------')

output_file = os.path.join("output.txt")

with open(output_file, "w", newline = "") as datafile:

    datafile.write(f'Election Results\n')
    datafile.write(f'----------------------------------------\n')
    datafile.write(f'Total Votes: ' + str(totalvotes) + '\n')
    datafile.write(f'----------------------------------------\n')
    datafile.write(str(candidates[0]) + ": " + str(percentage_count[0]) + "% (" + str(votes_per_candidate[0]) + ")\n")
    datafile.write(str(candidates[1]) + ": " + str(percentage_count[1]) + "% (" + str(votes_per_candidate[1]) + ")\n")
    datafile.write(str(candidates[2]) + ": " + str(percentage_count[2]) + "% (" + str(votes_per_candidate[2]) + ")\n")
    datafile.write(str(candidates[3]) + ": " + str(percentage_count[3]) + "% (" + str(votes_per_candidate[3]) + ")\n")
    datafile.write(f'----------------------------------------\n')
    datafile.write(f'Winner: ' + winner + '\n')
    datafile.write(f'----------------------------------------\n')