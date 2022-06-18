# This script is to pipe data into our program, transform it, and save it.

import csv


def transformationFunc(dataset):
    # initialise header list
    header = []
    rows = []
    new_header = ["first_name", "last_name", "price", "above_100"]
    new_rows = []
    with open(dataset, 'r') as file:

        csvreader = csv.reader(file)

        
        # next() method returns current header column and moves on next column ['name', 'price']
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
    # print(header)
    # print(rows)

    # looping to remove 0 characters in price
    for list in rows:
        for i in list[1]:
            if i == "0":
                list[1] = list[1].replace(i,"")
            else:
                break
        
    # delete rows without names 
    for list in rows:    
        if list[0] == "":
            rows.remove(list)

    # splitting up the first and last name and adding new field to check on price above 100
    above_100 = False
    for list in rows:
        tmp = list[0].split(" ", 1)
        if float(list[1]) > 100:
            above_100 = True
        else:
            above_100 = False
        new_rows.append([tmp[0], tmp[1], list[1], above_100])


    with open("Output\processed" + dataset, 'w', newline="") as file:
        csvwriter = csv.writer(file) # create a csvwriter object
        csvwriter.writerow(new_header) # write the header
        csvwriter.writerows(new_rows) # write the rest of the data

transformationFunc("dataset1.csv")
transformationFunc("dataset2.csv")