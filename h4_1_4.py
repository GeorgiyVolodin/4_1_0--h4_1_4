def palindrome(s):
   return s==s[::-1]

while True:
 s=input('Введите слово: ')

 if palindrome(s):
   print(True)
 else:
   print(False)



