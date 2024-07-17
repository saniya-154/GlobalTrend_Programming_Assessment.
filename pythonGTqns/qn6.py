def division(numerator,denominator):
    try:
        if denominator==0:
            return "Error: the denominator should be greater than 0"
        else:
            return numerator/denominator
    except TypeError:
        return "Error: Invalid inputs , inputs should be numbers."
numerator = int(input("Enter a number to be divided."))
denominator = int(input("Enter a number for divisor"))
result = int(division(numerator,denominator))
print(result)
     