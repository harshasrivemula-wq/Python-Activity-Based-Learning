1. Problem Statement :
Campus Event Financial Planning:
Develop a Python program to calculate the total cost of a campus event including venue, equipment, catering, transport, and certificate costs. The program should calculate participant contributions, identify the sponsorship shortfall, and determine the minimum number of registrations required to break even.

2. Algorithm :
1. Start the program.
2. Read venue, equipment, catering, transport, and certificate costs.
3. Read the number of participants.
4. Read registration fee and sponsorship amount.
5. Calculate the total event cost.
6. Calculate participant contribution.
7. Calculate total income.
8. Calculate sponsorship shortfall.
9. Calculate the minimum registration count required.
10. Display the financial report.
11. Check whether the event reaches break-even.
12. Stop the program.

3. Flowchart — Mermaid Code :




4. Python Source Code :
# Campus Event Financial Planning

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificate = float(input("Enter certificate cost: "))
participants = int(input("Enter expected participants: "))
fee = float(input("Enter registration fee per participant: "))
sponsorship = float(input("Enter sponsorship amount: "))

total_cost = venue + equipment + catering + transport + certificate
contribution = participants * fee
total_income = contribution + sponsorship
shortfall = total_cost - total_income

if shortfall > 0:
    print("Sponsorship shortfall:", shortfall)
else:
    print("No sponsorship shortfall.")

if fee > 0:
    minimum_count = int(total_cost / fee) + 1
else:
    minimum_count = 0

print("\n--- Event Financial Report ---")
print("Total Event Cost:", total_cost)
print("Participant Contribution:", contribution)
print("Sponsorship:", sponsorship)
print("Total Income:", total_income)
print("Minimum Registration Count:", minimum_count)

if total_income >= total_cost:
    print("Event is financially successful.")
else:
    print("More registrations are needed.")

5. Sample Input :
Enter venue cost: 10000
Enter equipment cost: 5000
Enter catering cost: 15000
Enter transport cost: 5000
Enter certificate cost: 2000
Enter expected participants: 50
Enter registration fee per participant: 500
Enter sponsorship amount: 10000

6. Sample Output :
No sponsorship shortfall.

--- Event Financial Report ---
Total Event Cost: 37000.0
Participant Contribution: 25000.0
Sponsorship: 10000.0
Total Income: 35000.0
Minimum Registration Count: 45
More registrations are needed.
