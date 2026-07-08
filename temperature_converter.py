format_of_temperature = input("enter the degree tye (Fahrenheit,Celsius)").lower()
current_temperature = float(input("Enter today's temperature:\n"))
if format_of_temperature == 'fahrenheit' or format_of_temperature == 'f':
    def convert_to_celsius():
        celsius = round((current_temperature-32)*(5/9))
        return celsius
    print(f"{current_temperature}Fahrenheit converted to celsius is {convert_to_celsius()}")
elif format_of_temperature == 'celsius' or format_of_temperature == 'c':
    def convert_to_fahrenheit():
        fahrenheit = round((current_temperature*(9/5))+32)
        return fahrenheit
    print(f"{current_temperature}Celsius converted to Fahrenheit is {convert_to_fahrenheit()}")
else:
    print("Invalid temperature type")