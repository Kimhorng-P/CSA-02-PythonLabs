
# Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter.
# Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes a hyphen will separate the two letters in the string.

alphabet = "abcdefghijklmnopqrstuvwxyz"

user_range = input("Enter a range of letters (e.g., a-z): ")
start_letter, end_letter = user_range.split('-')
start_character = ord(start_letter)
end_character = ord(end_letter)
result_string = ''.join(chr(i) for i in range(ord(start_letter), ord(end_letter) + 1))
print(result_string)
