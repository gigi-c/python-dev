import csv

with open("user_detail", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    # for row in csvreader:
    #     print(row)
    #
    for column in csvreader:
        print(column)

# print the last row and skipping every other line
    # iterable_csv = iter(csvreader)
    # next(iterable_csv) # to skip the next line
    # for row in csvreader:
    #     next(iterable_csv) # to skip the next line, so in the loop is every other line
    #     print(row[-1])

# copy data to a new csv file
def transform_user_details(user_detail):
    new_user_details = []
    with open("user_detail", newline="") as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=",")
        for user in user_details_csv:
            transformation = []
            transformation.append(user[0])
            transformation.append(user[1])
            transformation.append(user[-1])
            new_user_details.append(transformation)
        return new_user_details

def create_new_user_details_csv(old_file_name ="user_detail", new_file_name = "new_user_details"):
    new_user_details = transform_user_details(create_new_user_details_csv)
    new_file = open(new_file_name, "w")

    with new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_details)

create_new_user_details_csv()

