import csv

if __name__ == '__main__':
    # open the file
    with open('example.csv', 'r', encoding='utf-8') as data:
        # call csv reader
        csv_data = csv.reader(data)
        # reformat it into a python object list of lists
        data_lines = list(csv_data)
        for line in data_lines[:5]:
            print(line)
