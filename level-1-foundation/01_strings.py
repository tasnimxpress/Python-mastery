# Access an index, Sting slicing
message = 'Good Morning'
position = message[1]  # 2nd string o
print(position)

print(message[0])  # first string G

print(message[-1])  # first string form last g

print(message[0:5])
print(message[5:])  # print only Monring

# reverse the string
print(message[::-1])
print(message[5:-3])

# extract word from end
print(message[-4:])  # start from end, -4 position: n, then up to 1 from end: g

# start from end, -4 position: n, then up to -2 from end: i
print(message[-4:-2])

# make it lowercase
lower_case = message.lower()
print(lower_case)

# make it uppercase
upper_case = message.upper()
print(upper_case)
