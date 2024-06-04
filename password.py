import random
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters =uppercase_letters.lower()
digits = "0123456789"
symbols = " ~ ! @ # $ % ^ & * () _ + - = < > ? , . / ; : [ ] | \ { } "
upper,lower,numbers,symbol=True,True,True,True
all = " "

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if numbers:
    all += digits
if symbol:
    all += symbols

length = 10
amount = 10

for i in range(amount):
    password = "".join(random.sample(all,length))
    print(password)