def calculate_bmi(weight_kg, height_m):
    """Calculate BMI given weight in kg and height in meters"""
    return weight_kg / (height_m ** 2)

def get_bmi_category(bmi):
    """Return BMI category based on WHO standards"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def get_valid_input(prompt, input_type=float, min_val=0, max_val=300):
    """Get and validate user input"""
    while True:
        try:
            value = input_type(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Please enter a value between {min_val} and {max_val}")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("=== BMI Calculator ===")
    print("Please enter your details:\n")
    
    weight = get_valid_input("Weight in kilograms: ", min_val=30, max_val=300)
    height = get_valid_input("Height in meters (e.g., 1.75): ", min_val=1.0, max_val=2.5)
    
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)
    
    print(f"\nYour BMI is: {bmi:.1f}")
    print(f"Category: {category}")
    
    # Additional health information
    if category == "Underweight":
        print("\nNote: Being underweight may indicate nutritional deficiency.")
    elif category == "Normal weight":
        print("\nGreat! You're in the healthy weight range.")
    elif category == "Overweight":
        print("\nConsider consulting a healthcare provider about healthy weight management.")
    else:
        print("\nPlease consult a healthcare provider for weight management advice.")

if __name__ == "__main__":
    main()