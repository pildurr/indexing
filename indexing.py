"""Given a string of any length named s.

Extract and then print the first and last characters of the string (with one space between them).

For example, given s = 'abcdef'

the output will be

a f"""

s = input("Input a string: ")
s_first = s[0]
s_last = s[-1]
s_modified = s_first + " " + s_last

print(s_modified)