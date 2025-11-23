n=int(input("how many numbers you want to enter"))
result=[]
if n<0 and n>100:
    print("Enter correct value")
i=1
while i<=n:
    name=str(input("enter your name"))
    marks=float(input("enter your marks"))
    if marks>90 and marks<100:
        grade="O"
        comment="Congratulation you are exellent"
    elif marks>80 and marks<=90:
        grade = "A"
        comment ="Very good"
    elif marks>70 and marks<=80:
        grade = "B"
        comment ="Good score"
    elif marks>60 and marks<=70:
         grade="c"
         comment="need to improve yourself"
    elif marks>50 and marks<=60:
         grade="D"
         comment="need improvement "
    elif marks>0 and marks<50:
        grade="F"
        comment="fail"
    i=i+1
    results=result.append([name,marks,grade,comment])
for r in result:
    print("name:",r[0],"\n","marks:",r[1],"\n","Grade:",r[2],"\n","comment:",r[3])