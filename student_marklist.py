#studentmarklist calculat
sub1=float(input("enter the tamil mark:"))
sub2=float(input("enter the english mark:"))
sub3=float(input("enter the math mark:"))
sub4=float(input("enter the science mark:"))
sub5=float(input("enter the social science mark:"))
total=sub1+sub2+sub3+sub4+sub5
average=total/5
print(f"total mark:{total}")
print(f"average mark:{average}")
def total_grade(mark):
  if total>=500:
    return("invalid mark")
  elif total>=450:
    return("A grade")
  elif total>=400:
    return("B grade")
  elif total>=350:
    return("c grade")
  elif total>=300:
    return("D grade")
  else:
    return("fail")
def grade(mark):
  if mark>=90:
    return("A grade")
  elif mark>=70:
    return("B grade")
  elif mark>=50:
    return("C grade")
  elif mark<=50:
    return("average")
  else:
    return("fail")
print(f"total grade:{total_grade(total)")
print(f"tamil grade:{grade(sub1)}")
print(f"english grade:{grade(sub2)}")
print(f"math grarde:{grade(sub3)}")
print(f"science garde:{grade(sub4)}")
print(f"social sciencegarde:{grade(sub5)}")
print("hello")
