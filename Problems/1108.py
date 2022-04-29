address = "1.1.1.1"

a = address.split('.')

s = f'{a[0]}[.]{a[1]}[.]{a[2]}[.]{a[3]}'

print(s)