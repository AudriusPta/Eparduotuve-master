def sudetis(x, y):
    return x + y

def atimtis(x, y):
    return x - y

def daugyba(x, y):
    return x * y

def dalyba(x, y):
    if y != 0:
        return x / y
    else:
        return "Dalyba iš nulio negalima"

print("Pasirinkite veiksmą:")
print("1. Sudėtis")
print("2. Atimtis")
print("3. Daugyba")
print("4. Dalyba")

choice = input("Įveskite pasirinkimą (1/2/3/4): ")

num1 = float(input("Įveskite pirmą skaičių: "))
num2 = float(input("Įveskite antrą skaičių: "))

if choice == '1':
    print(num1, "+", num2, "=", sudetis(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", atimtis(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", daugyba(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", dalyba(num1, num2))
else:
    print("Neteisingas pasirinkimas")
