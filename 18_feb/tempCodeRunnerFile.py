def main():
    print("--- Simple Interest Calculator ---")
    
    try:
        # 1. Input Section
        # We use float to allow decimal values for money and rates
        principal = float(input("Enter the principal amount (P): "))
        rate = float(input("Enter the annual interest rate (R) in %: "))
        time = float(input("Enter the time period (T) in years: "))

        # 2. Calculation Section
        # Formula: SI = (P * R * T) / 100
        simple_interest = (principal * rate * time) / 100
        total_amount = principal + simple_interest

        # 3. Output Section
        # :.2f rounds the number to 2 decimal places
        # :, adds commas as thousands separators
        print("\n" + "="*30)
        print(f"Principal Amount:  ${principal:,.2f}")
        print(f"Interest Rate:     {rate}%")
        print(f"Time Period:       {time} years")
        print("-" * 30)
        print(f"Interest Earned:   ${simple_interest:,.2f}")
        print(f"Total Balance:     ${total_amount:,.2f}")
        print("="*30)

    except ValueError:
        print("Invalid input! Please enter numeric values only.")

if _name_ == "_main_":
    main()