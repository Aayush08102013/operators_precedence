# operators precedence PEMDAS (Parenthesis, exponential, multiplication, division, addition, subtraction.)
a = 12
b = 3
c = 4
d = 9
answer = b**c + d/ b*c + a
print(answer)

# challenges, if the number is divisible or not?
n1 = int(input("enter your numerator: "))
n2 = int(input("enter your denominator: "))
if n1%n2 == 0:
    print(str(n1),f"is divesible by",str(n2))
else:
    print(str(n1),f"is NOT divesible by",str(n2))

# Corrected mean
mean = 38
wrong_number = 36
correct_number = 56
total_number = 40

#wrong sum mean = sum/total
sum = mean*total_number
print(f"wrong mean = {sum}")
#corrected sum
sum2 = sum - wrong_number + correct_number
print(f"correct mean = {sum2}")
#mean2:
mean2 = sum2/total_number
print(f"the corrected mean is {mean2}")

# cyclist average speed
s1 = int(input("enter your value:"))
s2 = int(input("enter your value:"))
s3 = int(input("enter your value:"))
avg = (s1+s2+s3)/3
if s1 < avg:
    print("speed of the cyclist 1 is less average speed")
elif s1 > avg:
    print("speed of the cyclist 1 is above average speed")
if s2 < avg:
    print("speed of the cyclist 2 is less average speed")
elif s2 > avg:
    print("speed of the cyclist 2 is above average speed")
if s3 < avg:
    print("speed of the cyclist 3 is less average speed")
elif s3 > avg:
    print("speed of the cyclist 3 is above average speed")
