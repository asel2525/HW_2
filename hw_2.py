# 1
hours = input("Enter hours: \n")
rate = input("Enter rate: \n")
salary = int(hours) * float(rate)
print("Salary: " + str(salary))

# 2
celcius = int(input("Enter Celcius Temperature: \n"))
fahrenheit = celcius * 9 / 5 + 32
fahrenheit = int(fahrenheit)
print("Fahrenheit temperature: " + str(fahrenheit))


# 3
seconds = int(input("Enter seconds: \n"))
hrs = seconds // 3600
min_ = seconds // 60 % 60
sec = seconds % 60
print(str(seconds) + " seconds is " + str(hrs) + " hours, " + str(min_) + " minutes, " + str(sec) + " seconds. ")