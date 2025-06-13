i = 1
while i <= 10:
    print(i)
    i += 1 
i = 10
while i >= 1:
    print(i)
    i -= 1 
# while ციკლი იმეორებს კოდს მანამ, სანამ პირობა მართალია (True)
# მაგ: სანამ i <= 10, მანამდე დაბეჭდავს i-ს
# თუ პირობა ცრუ გახდება, ციკლი შეწყდება

password = ""
while password != "python123":
    password = input("შეიყვანე პაროლი: ")
print("პაროლი სწორია!")

n = int(input("შეიყვანე რიცხვი: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print("რიცხვების ჯამი:", sum)