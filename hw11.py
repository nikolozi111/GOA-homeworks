n = int(input("შეიყვანე რიცხვი: "))
for i in range(0, n + 2): 
    print(i)

age = int(input("შეიყვანე ასაკი: "))
has_card = input("გაქვს სტუდენტური ბარათი? (დიახ/არა): ")

if age < 18 or has_card.lower() == "დიახ":
    print("დანაზოგი გაქვს!")
elif age >= 60 and has_card.lower() != "დიახ":
    print("პენსიონერის ფასდაკლება გაქვს!")
else:
    print("ფასდაკლება არ გეკუთვნის.")

a = int(input("შეიყვანე პირველი რიცხვი: "))
b = int(input("შეიყვანე მეორე რიცხვი: "))

if a > 0 and b > 0:
    print("ორივე დადებითია")
elif (a > 0 and b <= 0) or (a <= 0 and b > 0):
    print("მხოლოდ ერთი დადებითი რიცხვია")
else:
    print("არცერთი არ არის დადებითი")

x = float(input("შეიყვანე პირველი რიცხვი: "))
y = float(input("შეიყვანე მეორე რიცხვი: "))
op = input("შეიყვანე ოპერაცია (+, -, *, /): ")

if op == "+":
    print("შედეგი:", x + y)
elif op == "-":
    print("შედეგი:", x - y)
elif op == "*":
    print("შედეგი:", x * y)
elif op == "/":
    if y != 0:
        print("შედეგი:", x / y)
    else:
        print("არასწორი ოპერაცია!")
else:
    print("არასწორი ოპერაცია!")