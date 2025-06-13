
sistoluri = int(input("შეიყვანე სისტოლური წნევა: "))
diastoluri = int(input("შეიყვანე დიასტოლური წნევა: "))
if sistoluri > 140 or diastoluri > 90:
    print("მაღალი წნევა")
elif sistoluri < 90 or diastoluri < 60:
    print("დაბალი წნევა")
else:
    print("წნევა ნორმალურია")

age = int(input("შენი ასაკი: "))
weight = float(input("შენი წონა: "))

if age < 10:
    if weight < 20:
        print("წონა დაბალია")
    elif 20 <= weight <= 40:
        print("წონა ნორმალურია")
    else:
        print("წონა მაღალია")

elif 10 <= age <= 17:
    if weight < 40:
        print("წონა დაბალია")
    elif 40 <= weight <= 65:
        print("წონა ნორმალურია")
    else:
        print("წონა მაღალია")

else:  # age >= 18
    if weight < 50:
        print("წონა დაბალია")
    elif 50 <= weight <= 90:
        print("წონა ნორმალურია")
    else:
        print("წონა მაღალია")

age = int(input("ასაკი: "))
hour = int(input("საათი (0-23): "))

if age < 18 and hour >= 22:
    print("დროა დაძინების")
elif age >= 60 and hour >= 21:
    print("დასვენება რეკომენდებულია")
else:
    print("შეგიძლიათ გააგრძელოთ აქტივობა")


age = int(input("ასაკი: "))
heart_rate = int(input("გულის ცემა: "))

if age < 30 and heart_rate < 140:
    print("შეგიძლიათ მეტი ივარჯიშოთ")
elif age >= 30 and heart_rate > 170:
    print("დასვენება გჭირდებათ")
else:
    print("აქტივობის დონე ნორმალურია")

if 0 <= age <= 12:
    print("ბევრი ვიტამინიანი საკვები")
elif 13 <= age <= 25:
    print("ენერგიის მომცემი საკვები")
elif 26 <= age <= 59:
    print("ბალანსირებული რაციონი")
elif age >= 60:
    print("დაბალკალორიული და მსუბუქი საკვები")
else:
