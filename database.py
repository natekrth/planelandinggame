import csv


class FlightDB:

    def __init__(self, name):
        self.name = name

    def insert(self, callsign, flightdata):
        """
        insert method will insert time and blackbox object to csv file of each plane sort by callsign
        :param callsign: callsign of the plane
        :param flightdata: flightdata dictionary
        """
        header = ['time', 'blackbox']                          # header of column
        with open(callsign+'.csv', 'w', newline='') as file:   # open file by given callsign for write
            writer = csv.DictWriter(file, fieldnames=header)   # writer is object operates to write on file with header
            writer.writeheader()                               # write header in csv file
            for time, blackbox in flightdata.items():
                writer.writerow({'time': time, 'blackbox': blackbox})      # write time and black box to each row

    def search(self, callsign):
        """
        search method use for read data from csv file of plane and print time and blackbox if it is exist
        :param callsign: callsign of the plane
        """
        with open(callsign+'.csv', 'r') as file:              # open file by given callsign for read
            reader = csv.reader(file)                         # reader is object that will iterate over lines
            next(reader)                                      # skip header row
            try:
                for row in reader:
                    print(f'{row[0]} --> {row[1]}')
            except ValueError:
                print("No data")
