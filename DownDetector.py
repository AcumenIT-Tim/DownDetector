import platform    # For getting the operating system name
import subprocess  # For calling commands
import csv         # For reading CSV files

def ping(ip):
    # Runs 1 ping and saves the commandline text to output
    output = subprocess.Popen(["ping",'-n','1',ip],stdout = subprocess.PIPE).communicate()[0]

    # Returns a fail if unable to reach host
    if ('timed out' in str(output) or 'unreachable' in str(output)):
        return 1
    else:
        return 0

def readFile():
    with open('test.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print

readFile()