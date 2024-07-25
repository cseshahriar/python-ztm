#  := warlus operator
a = 'hellooooooooooooooooo'

if(n := len(a)) > 10:
    print(f" n: {n}")

print(n)


while(m := len(a) > 1):
    print(m)
    a = a[:-1]
