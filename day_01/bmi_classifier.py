

def classify_bmi(weight_kg:float, height_m:float) -> tuple[float, str]:

    bmi = weight_kg / (height_m ** 2) 
    

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category

weight = float(input("please enter your weight (kg): "))
height = float(input("please enter your height (m): "))

if weight <= 0 or height <= 0:
    print("Error: Weight and height must be greater than zero")
else:
    bmi_value, label = classify_bmi(weight, height)
    print(f"BMI: {bmi_value:.1f} {label}")   