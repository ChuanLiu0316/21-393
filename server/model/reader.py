import csv
def read_csv(filename):
    data = [] # type: List[Dict]
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data        
