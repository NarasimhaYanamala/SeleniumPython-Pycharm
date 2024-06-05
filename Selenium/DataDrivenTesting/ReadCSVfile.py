import csv
import os

# csv open method
# with keyword operation, it provides simplyed exception handling , No need to close as  it handles

with open(os.getcwd()+"\\test.csv") as file:
    csvfile = csv.reader(file)    #reading CSV file
    for line in csvfile:
        print(csvfile)











