#!/usr/bin/env python3

# Create a list containing three items:
my_list = [ "192.168.0.5", 5060, "UP" ]

# Display the first item in the list:
print("The first item in the list (IP): " + my_list[0] )

# Display the second item in the list:
print("The second item in the list (port): " + str(my_list[1]) )

# Display the third itemt in the list
print("The last item in the list (state): " + my_list[2] )

#Challenge 01: Display the IP address:
iplist = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

for item in iplist:
    if "." in str(item):
        print("IP Address: " + item)
