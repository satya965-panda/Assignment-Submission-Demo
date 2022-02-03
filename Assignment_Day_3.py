s = input("Enter a string: ").lower()
d = {}
for i in s:
  d[i] = d.get(i, 0) + 1

print(d)
max_key = max(d, key = d.get)
print(max_key)