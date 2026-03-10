# # Access an index, Sting slicing
# message = 'Good Morning'
# position = message[1] # 2nd string o
# print(position)

# print(message[0]) # first string G

# print(message[-1]) #first string form last g

# print(message[0:5])
# print(message[5:]) # print only Monring

# #reverse the string
# print(message[::-1])
# print(message[5:-3])

# #extract word from end
# print(message[-4:]) #start from end, -4 position: n, then up to 1 from end: g

# print(message[-4:-2]) #start from end, -4 position: n, then up to -2 from end: i

# # make it lowercase
# lower_case = message.lower()
# print(lower_case)
# # make it uppercase
# upper_case = message.upper()
# print(upper_case)

# # swap case
# print(message.swapcase())

# def swap_case(s):
#     swap = s.swapcase()
#     return swap

# print(swap_case(message))


# # String Split and Join
# text = 'part of a string'
# def split_and_join(text):
#     split = text.split()
#     join = '-'.join(split)
#     return join

# print(split_and_join(text))


# print_full_name function
def print_full_name(first, last):
    full_name = first + ' ' + last
    # full_name = f'{first} {last}'
    print(f'Hello {full_name}! You just start learning python.')

if __name__ == '__main__':
    print_full_name('Ross', 'Tailor')

# firstName = 'Tas'
# lastName = 'Nim'
# print(print_full_name(firstName, lastName))

