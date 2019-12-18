num = int(input("Please enter the current temperature:"))#Used int(input) to make the input an integer. Onnly integers are used in calculations. Python by default returns inputs as strings.
celciuscalc = (num - 32) * 5/9
print("It is currently ", round(celciuscalc, 1), "°C outside.")#Used round() to make it more readable.
#Try and make a distance converter when you're free