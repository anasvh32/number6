def parse_people(text):
    cleaned = text.strip()
    if cleaned.isdigit():
        result = int(cleaned)
        if result > 0:
            return result
    return None  # برای صفر، منفی، حروف و اعداد فارسی

def convert(kind, value):
    try:
        value = float(value)
    except ValueError:
        return "Error: Invalid number"
    
    if kind == "c2f":
        return round(value * 9 / 5 + 32, 2)
    else:
        return "Error: Unknown type"

while True:
    print("\n1. Convert\n2. Exit")
    choice = input("Enter choice: ")
    if choice == "2":
        break
    elif choice == "1":
        kind = input("Enter conversion type: ")
        value_str = input("Enter value: ")
        result = convert(kind, value_str)
        print(f"Result: {result}")
        
        people_str = input("Enter number of people (or press Enter to skip): ")
        if people_str.strip() != "":
            people = parse_people(people_str)
            if people is not None:
                print(f"Split per person: {result / people:.2f}")
            else:
                print("Error: Number of people must be a positive integer")