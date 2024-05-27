import csv #for reading csv files >>>REPLACE WITH PANDAS<<<
import os #for getting csv files from this script's directory

class IOHandler:
    '''
    IOHandler class
    Attributes: CSVFileName
    Functions: getUserInput, readPlanetData, writeResults
    '''
    def __init__(self):
        while True:
            print(f"CSV files from {os.path.basename(__file__)}'s directory")
            listOfCSV = []
            for fileName in os.listdir(os.path.dirname(os.path.realpath(__file__))):
                if fileName.endswith(".csv"):
                    listOfCSV.append(fileName)
                    print(f"{len(listOfCSV)}. {fileName}")
            try:
                self.CSVFile = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), listOfCSV[0]), 'r')
                self.CSVFile = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), listOfCSV[int(self.getUserInput("Enter CSV file number (enter anything if there is only one CSV file)", "Enter an int: ")) - 1]), 'r')
            except ValueError as e:
                pass
            except IndexError as e:
                pass
            except Exception as e:
                print(e)
                pass
            if hasattr(self, 'CSVFile'):
                break
        while True:#ask user to input row number of first and last planet
            #minus 1 so the first index is 0
            firstPlanet, lastPlanet = int(self.getUserInput("Enter the row of the first planet(starting from 1 for the first planet in the file)", "Enter an integer: ")), int(self.getUserInput("Enter the row of the last planet", "Enter an integer: "))
            if firstPlanet < lastPlanet and firstPlanet >= 0 and lastPlanet >= 0:
                self.firstPlanet, self.lastPlanet = firstPlanet, lastPlanet
                print(f"Planets in the simulation: {lastPlanet - firstPlanet}")
                break
    def getUserInput(self, message, message1):
        print(message)
        return input(message1)
        #userInput = input(message1) #restart script if input == "R"
        #return os.execv(sys.executable, [sys.executable, __file__] + sys.argv) if userInput == "R" else userInput
    def readPlanetData(self):
        csvReader = csv.reader(self.CSVFile)
        temp = []
        for index, row in enumerate(csvReader):#read the selected rows from the csv file
            if index+1 >= self.firstPlanet and index+1 <= self.lastPlanet:
                #content = list(row)
                content = [float(i) for i in list(row)]
                temp.append(content)
        return temp