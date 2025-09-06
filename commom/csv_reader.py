import csv
import os

#读取CSV
def read_csv_test_date(file_name):
    test_data = []
    file_path = os.path.join(os.path.dirname(__file__),'..','data',file_name)

    with open(file_path,'r',encoding='utf-8') as  csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            test_data.append(row)

    return test_data