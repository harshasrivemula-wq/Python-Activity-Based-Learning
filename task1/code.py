# Campus Event Financial Planning

shortfall = total_cost - total_income
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

if shortfall > 0:
    print("Sponsorship shortfall:", shortfall)
else:
    print("No sponsorship shortfall.")

if fee > 0:
    fixed_cost = total_cost - (catering + certificate)
    minimum_count = int(fixed_cost / fee) + 1
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
