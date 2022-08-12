# The BMI is Calculated by dividing a person's weight(in Kg) by the square of thier height (in M)
# BMI = weight(kg)/ square of height(m^2)


def main():
    height = float(input("Height: "))
    weight = float(input("Weight: "))
    print(f"BMI: {round(calculate_bmi(height, weight))}Kg/m2")
    print(f"Interpretation: {checker(calculate_bmi(height, weight))}")
    # print(f"BMI: {calculate_bmi(height, weight)}Kg/m2")

def checker(check):
    if check < 18.5:
      return "Underweight"
    elif 18.5 < check < 25:
      return "Normal weight"
    elif 25 < check < 30:
      return "Overweight"
    elif 30 < check < 35:
      return "Overweight"
    else:
      return "Clinically obese"
  

# def get_height():
#     return float(input("Height: "))


# def get_weight():
#     return int(input("Weight: "))


def calculate_bmi(h, w):
    return w / pow(h, 2)


if __name__ == "__main__":
    main()
 