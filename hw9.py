x = 10      # int
y = 3.5     # float
z = x + y   # Python აქ x-ს გადააქცევს float-ად ავტომატურად(implicit)

print(z)    # იქნება float ტიპის: 13.5

a = "5"
b = int(a)   # აქ ჩვენ ვეუბნებით – გადააკეთე string-იდან int-ად (explicit)
print(b + 10)  # 15

n = int(input("შეიყვანე რიცხვი: "))

for i in range(n + 1): 
    print(i)
    

n = int(input("შეიყვანე რიცხვი: "))

i = 0
while i <= n:
    print(i)
    i += 1
