# 1-misol
n = int(input("Sonni kiriting: "))
s = 1
for i in range(1,n+1):
    s *=i
print(s)

# 2-misol
s = "O'zbekiston"
t = s[::-1]
print(t)

# 3-misol
royxat = [13,5,3,7,15,25]
new_royxat = []
for i in royxat:
    new_royxat.append(i**2)    
print(new_royxat)

# 4-misol
royxat = [32, -12, 11, 42, -6, -65, 19]
musbat_royxat = []
manfiy_royxat = []
for i in royxat:
    if i > 0:
        musbat_royxat.append(i)
    else:
        manfiy_royxat.append(i)
print(f"musbat royxat = {musbat_royxat}, manfiy royxat = {manfiy_royxat}" )

# 5-misol
royxat = [32, 29, 11, 42, 66, 123, 87, 90, 45]
juft_royxat = []
toq_royxat = []

for i in royxat:
    if i % 2 == 0:
        juft_royxat.append(i)
    else:
        toq_royxat.append(i)
        
print(f"juft royxat = {juft_royxat}, toq royxat = {toq_royxat}")
    
# 6-misol
for i in range(1, 6):
	for j in range(1, 6-i):
		print(end=" ")
	for j in  range(1, i+1):
		print("*", end=" ")
	print()

