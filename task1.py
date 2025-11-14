name=input("enter your name")
age=int(input("enter your age"))
city=input("enter your city")
hobbies=[]
while True:
    hobbie=input("your hobbie if completed enter done")
    if hobbie.lower() =='done':
        break
    hobbies.append(hobbie)
print("-"*40)
print("Personal Information")
print("-"*40)
print("1.Name:",name)
print("2.Age:",age)
print("3.city:",city)
print("4.hobbies:")
if hobbies:
    for i, h in enumerate(hobbies,start=1):
        print("\t",i,".",h  )
else:
    print("No hobbies")

print("-"*40)