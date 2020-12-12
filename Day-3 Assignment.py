print("-------LetsUpgrade Day-3-------")
print("# Assignment - 1")
marks=int(input("Enter your marks percentage in the Exam : "))
print("Printing Grade in exam")
if marks>=85:
    print("you got A+ grade in the exam")
elif marks>=70:
    print("you got A grade in the exam")
elif marks>=60:
    print("you got B+ grade in the exam")
elif marks>=50:
    print("you got B grade in the exam")
elif marks>=45:
    print("you got C grade in the exam")
elif marks>=36:
    print("you got C+ grade in the exam")
else:
    print("you got Failed in the exam")

print("# Assignment - 2")
print("Printing prime numbers of range <1000") 
for i in range(1,1000):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=' ')

print("\n# Assignment - 3")
print("Printing Prime Numbers Using While With User Input")
n="Y"
while n=="Y":
    prime=int(input("enter ending range of the prime number to print : "))
    for i in range(1,prime+1):
        for j in range(2,i):
            if prime==i:
                break
            elif i%j==0:
                break
        else:
            print(i,end='  ')
    print("\nProcess is Completed")
    n=input("\nIf you want to enter range again Type 'y' else 'n': ").upper()
    if n!="Y":
        break









