import csv

class FlightDB:

    def __init__(self, name):
        self.name = name

    def insert(self, callsign, flightdata):
        data = flightdata
        header = ['time', 'blackbox']
        with open(callsign+'.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            for key in data:
                writer.writerow({'time': key, 'blackbox':data[key]})

    def search(self, callsign):
        with open(callsign+'.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            try:
                for row in reader:
                    print(f'{row[0]} --> {row[1]}')
            except:
                print("No data")

        # new_data = {"name":callsign, "time":flightdata.keys()[check]}
        # try:
        #     with open(callsign+'.csv', 'r') as file:
        #         data = csv.DictReader(file)
        #         list(data)

        # except FileNotFoundError:
        #     with open(plane+'.csv', 'w') as file:
        #         data = csv.writer(file)
        #         data.writerow(["time", 'blackbox'])
        # else:
        #     with open(plane+'.csv', 'w') as file:
        #         data = csv.writer(file)
        # fieldname1 = ['Callsign', 'Blackbox']
        # # self.__flight_data_dt[dt] = plane
        # # self.__blackbox[plane.callsign] = self.__flight_data_dt
        # new_data = plane
        # print(new_data)
        #
        # try:
        #     with open("blackbox.csv", "w") as csv_file:
        #         writer = csv.DictWriter(csv_file, fieldnames=fieldname1)
        #         writer.writeheader()
        #         for data in new_data:
        #             writer.writerow(data)
        # except IOError:
        #     print("I/O error")
        # except FileNotFoundError:
        #     with open("blackbox.csv", "w") as read_data:
        #         csv.reader(read_data, fieldname=fieldname)
        # else:
        #     data.update(new_data)
        #     with open("blackbox.csv", "w") as read_data:
        #         json.dump(data, read_data, indent=4)

