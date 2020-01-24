import platform    # For getting the operating system name
import subprocess  # For calling commands
import csv         # For reading CSV files

devices = []       # Array of dicts for holding info read from file

def ping(ip):
    print(ip)
    # Runs 1 ping and saves the commandline text to output
    output = subprocess.Popen(["ping",'-n','1',ip],stdout = subprocess.PIPE).communicate()[0]

    # Returns a fail (1) if unable to reach host or pass (0)
    if ('timed out' in str(output) or 'unreachable' in str(output)):
        return 0
    else:
        return 1

def readFile():
    with open('ips.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',') # Open csv file and set delimiter to a comma
        line_count = 0 # Tracks which line of the .csv it is on

        for row in reader:
            if line_count == 0:
                line_count += 1
            else:                 # Creates a dict with IP, Hostname, and location
                if len(row) == 2: # If the location is left empty in the csv, it will set it to unknown
                    dev = dict(ip=row[0], host=row[1], loc = "Unknown")
                else:
                    dev = dict(ip=row[0], host=row[1], loc = row[2]) 
                devices.append(dev) 
                line_count += 1
    csv_file.close()
    reader = None
    
readFile()

