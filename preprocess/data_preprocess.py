import csv
import pandas as pd


def preprocess():
    with open('data/oddetect.csv', 'r') as old_file:
        csv_reader = csv.reader(old_file, delimiter=',')
        invalid_lines = 0
        valid_lines = 0

        with open(r'data/fixed.csv', 'w', newline='') as new_file:
            write_file = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            write_file.writerow(
                ['frameNum', 'x', 'y', 'objectNum', 'size', 'sequenceNum', 'TBD', 'TBD', 'TBD', 'filename', 'start',
                 'path time', 'delta time'])
            for row in csv_reader:
                valid_lines += 1
                if len(row) == 14:
                    write_file.writerow(row)
                else:
                    invalid_lines += 1
    data = pd.read_csv("data/fixed.csv", usecols=[1, 2, 3, 5, 9, 10, 12])
    data['time'] = pd.to_datetime(data['start']) + pd.to_timedelta(data['delta time'])
    del data['start']
    del data['delta time']
    data.drop_duplicates(subset=None, keep='first', inplace=False)
    data.to_hdf("data/data.hdf5", "df")


