import platform    # For getting the operating system name
import subprocess

hostname ="10.73.107.200"
print(hostname)
output = subprocess.Popen(["ping",hostname],stdout = subprocess.PIPE).communicate()[0]

# print(output)
# def ping(host):
#     """
#     Returns True if host (str) responds to a ping request.
#     Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
#     """

#     # Option for the number of packets as a function of
#     param = '-n' if platform.system().lower()=='windows' else '-c'

#     # Building the command. Ex: "ping -c 1 google.com"
#     command = ['ping', param, '1', host]

#     return subprocess.call(command) == 0

# ping('10.73.107.200')

if ('timed out' in str(output) or 'unreachable' in str(output)):
    print("Offline")