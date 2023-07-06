def calculate_simple_interest(principle, rate, time):
    interest = (principle * rate * time) / 100
    return interest
def main():
    while True:
        print("Select the mode:")
        print("1. Calculate interest")
        print("2. Calculate principle")
        print("3. Calculate principle + interest")
        print("4. Calculate rate")
        print("5. Calculate time")
        print("6. Calculate total payable after interest")
        print("7. Quit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            principle = float(input("Enter the principle amount: "))
            rate = float(input("Enter the interest rate: "))
            time = float(input("Enter the time (in years): "))

            interest = calculate_simple_interest(principle, rate, time)
            print("The interest is:", interest)
        elif choice == "2":
            interest = float(input("Enter the interest: "))
            rate = float(input("Enter the interest rate: "))
            time = float(input("Enter the time (in years): "))

            principle = interest / (rate * time / 100)
            print("The principle amount is:", principle)
        elif choice == "3":
            interest = float(input("Enter the interest: "))
            rate = float(input("Enter the interest rate: "))
            time = float(input("Enter the time (in years): "))

            principle = interest / ((rate * time / 100) + 1)
            print("The principle + interest amount is:", principle + interest)
        elif choice == "4":
            principle = float(input("Enter the principle amount: "))
            interest = float(input("Enter the interest: "))
            time = float(input("Enter the time (in years): "))

            rate = (interest / (principle * time)) * 100
            print("The interest rate is:", rate)
        elif choice == "5":
            principle = float(input("Enter the principle amount: "))
            interest = float(input("Enter the interest: "))
            rate = float(input("Enter the interest rate: "))
            time = interest / (principle * rate / 100)
            print("The time (in years) is:", time)
        elif choice == "6":
            years = int(input('How many years of interest do you want to check (compound)'))
            interest = float(input('What is the interest? (In percentage)'))
            principle = float(input('What is the principle?'))
            years = years - 1
            deci_interest = (interest / 100) + 1
            payable = principle
            for i in range(years):
                payable = payable * deci_interest
            payable = payable - principle
            print("The total payable interest is $", round(payable,2))
        elif choice == "7":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 7.")
        print()  # Print a blank line for readability
if __name__ == "__main__":
    main()
