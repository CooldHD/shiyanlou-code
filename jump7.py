num = range(100)
for a in num:
    b = a+1;
    if b%7 == 0:
        continue;
    if b%10 == 7:
        continue;
    if b//10 == 7:
        continue;
    print(b)
