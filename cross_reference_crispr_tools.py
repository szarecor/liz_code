from collections import OrderedDict
import texttable
#This program compares the tools in the order that they are given to them

# Helper method to make an ordered list of the target sequences
def makeList(fileName):
    # Open the data file
    f = open(fileName, "r")
    # Read each line, and add the target sequence to a list
    listA = []
    for line in f:
        next = line[:20]
        listA.append(next)

    return listA

# Ask for the data files
"""
number = raw_input("How many tools do you want to compare? \n")
num = int(number)

fileN = raw_input("What is the file path of your first file? \n")

files = [fileN]
count = 1

while count < num:
    # get a new file name from user
    fileN = raw_input("What is the  file path of your next file? \n")
    files.append(fileN)
    count += 1
"""

# I've temporarily commented-out the above so that I didn't need to manually specify the files
# during development, instead I'll just define the list of files here for dev purposes:
files = ["targets1.txt", "targets2.txt", "targets3.txt", "targets4.txt"]



# all_targets is a dictionary, we are going to use input file names as dictionary keys and lists of the file contents
# as dictionary values, we are using an OrderedDict so that the first input file will be the first column, and so on.
# without the OrderedDict, we would fetch them from a regular dictionary in an order different from the order we
# inserted them...
all_guides = OrderedDict()

# Here we start the table we will output:
table = texttable.Texttable()
# Set the widths of the table columns:
table.set_cols_width([20 for i in range(0, len(files) + 1)])
table.header([""] + files)

# This will be a set of unique CRISPR guides from all of the input files:
guide_set = set()

# Loop through the files in the list
for file_name in files:
    guide_list = makeList(file_name)
    all_guides[file_name] = guide_list

    # Loop through each guide from the file and add each to the unique set of CRISPR guides:
    for guide_seq in guide_list:
        guide_set.add(guide_seq)


# Now, we loop through the set of unique guides
for guide_seq in guide_set:

    matches = []
    # And loop through the dictionary of filenames => lists of guides:
    for source_file in all_guides:
        try:
            # [].index() will through an error if the guide is not found:
            matches.append(
                all_guides[source_file].index(guide_seq) + 1
            )

        except ValueError:

            # if the value is not found (error thrown), append an "X":
            matches.append("X")

    # Add a row to the table that is the guide sequence and the position ordinal for that guide from the relevant
    # input file:
    table.add_row([guide_seq] + matches)


# Finally, we can print the table we've made:
print table.draw()



