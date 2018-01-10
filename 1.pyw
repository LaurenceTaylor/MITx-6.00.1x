# 1
# Write a program that counts up the number of vowels contained in the string s.

count = 0

for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1

print('Number of vowels: ' + str(count))

# 2
# Write a program that prints the number of times the string 'bob' occurs in s.

count = 0

for i in range(len(s) - 2):
    if s[i] + s[i + 1] + s[i + 2] == 'bob':
        count += 1

print(count)
