# Sequences (მიმდევრობები) — ეს არის მონაცემების თანმიმდევრობა
numbers = [1, 2, 3, 4]  # ეს არის სია — sequence
text = "Hello"          # ესეც sequence-ია, რადგან სიმბოლოების მიმდევრობაა

# Iteration არის პროცესის გამეორება. ჩვეულებრივ, ვხდებით sequence-ში ელემენტებზე.
for number in numbers:
    print(number)  # იტერაცია სიის ყველა ელემენტზე

# Selection პროგრამის ნაკადის მართვა პირობის საფუძველზე, მაგ: if
age = 18
if age >= 18:
    print("Adult")  # პირობაზე დაფუძნებული არჩევა

# ალგორითმი არის კონკრეტული ნაბიჯების თანმიმდევრობა, რომელიც მივყავართ გარკვეულ ამოცანის ამოხსნამდე.

number = 4
if number % 2 == 0:
    print("Even")  # ალგორითმის ნაწილი

print(True or False and False or True and False or False and False or False and True and False or True) 
# პასუხია True
print(5 > 10 or 7 * 7 / 7 == 7 and False or True and "1234" != "1234" and 7 + 3 * 3 + 1 == 15 and True and True or 100 > 100 or True)
# პასუხია True

num = int(input("Enter a number: "))
if (num % 2 == 0 and num > 10) or num == 7:
    print(True)


print(int("5"))        # 5
print(int(5.9))        # 5
print(int(True))       # 1


print(str(123))        # '123'
print(str(3.14))       # '3.14'
print(str(True))       # 'True'

print(float("3.5"))    # 3.5
print(float(10))       # 10.0
print(float(False))    # 0.0


print(bool(0))         # False
print(bool(5))         # True
print(bool(""))        # False

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("This is leap year")
if year % 4 != 0 and year % 100 != 0:
    print("This is not leap year")