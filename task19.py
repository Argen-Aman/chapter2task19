str1 = input('What do you want to check, palindrome it, or not:\n')
str1 = str1.lower()
str1 = str1.replace(' ', '')

def palindrome (str1):
    if str1 == str1[::-1]:
        print('True')
    else:
        print('False')
palindrome (str1)
