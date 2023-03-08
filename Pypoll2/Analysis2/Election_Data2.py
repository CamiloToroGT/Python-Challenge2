import csv

# create a dictionary to store candidate names and their vote count
candidates = {}

# set the initial value for total votes to 0
total_votes = 0

# read the CSV file containing the election data
with open('Election_data.csv') as file:
    reader = csv.reader(file)
    next(reader)  # skip the header row

    # iterate over each row in the CSV file
    for row in reader:
        candidate = row[2]

        # if the candidate hasn't been added to the dictionary yet, add them
        if candidate not in candidates:
            candidates[candidate] = 0

        # increment the candidate's vote count by 1
        candidates[candidate] += 1

        # increment the total vote count by 1
        total_votes += 1

# create a list to store the results of each candidate
results = []

# iterate over each candidate in the dictionary
for candidate in candidates:
    # calculate the percentage of votes the candidate won
    percentage = round((candidates[candidate] / total_votes) * 100, 2)

    # create a tuple containing the candidate's name, percentage, and vote count
    result = (candidate, percentage, candidates[candidate])

    # add the tuple to the results list
    results.append(result)

# sort the results list in descending order based on vote count
results.sort(key=lambda x: x[2], reverse=True)

# print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for result in results:
    print(f"{result[0]}: {result[1]}% ({result[2]})")
print("-------------------------")
print(f"Winner: {results[0][0]}")
print("-------------------------")
