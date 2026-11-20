



def calculate_tip_share(bill: float, tip: float, people: int ) -> float | None:
    if bill <= 0 or tip < 0 or people <= 0:
        print("Error: bill and people must be greater than zero, and tip must be non-negative")
        return None

    tip_amount = bill * (tip / 100)

    total_bill = bill + tip_amount

    amount_per_person = total_bill / people  

    return amount_per_person  


bill = float(input("please enter your bill amount ($): "))
tip_percentage = float(input("please enter your tip percentage (%): "))
number_of_people = int(input("Please enter the number of people: "))

bill_per_person = calculate_tip_share(bill, tip_percentage, number_of_people)

if bill_per_person is not None:
    print(f"Each person's share: ${bill_per_person:.2f}")

