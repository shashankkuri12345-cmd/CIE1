temp = int(input("Enter temperature: "))
fah = (temp * 1.8)+32

print("TEMPERATURE :",temp)
print("FAHRENIT :",fah)

if temp < 15:
    print("Cold")
elif temp > 25:
    print("Hot")
else:
    print("Normal")