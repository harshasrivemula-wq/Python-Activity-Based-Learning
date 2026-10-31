n = int(input("Enter number of candidates: "))
candidates = []

for i in range(n):
    print("\nCandidate", i + 1)
    name = input("Enter name: ")
    math = float(input("Enter Mathematics marks: "))
    physics = float(input("Enter Physics marks: "))
    chemistry = float(input("Enter Chemistry marks: "))
    aggregate = (math + physics + chemistry) / 3

    if math >= 50 and physics >= 50 and chemistry >= 50 and aggregate >= 60:
        candidates.append([name, aggregate])

candidates.sort(key=lambda x: x[1], reverse=True)

print("\n--- Eligible Candidates ---")
rank = 1
for candidate in candidates:
    print(rank, candidate[0], round(candidate[1], 2))
    rank += 1

if len(candidates) == 0:
    print("No eligible candidates.")
else:
    print("\nAdmission ranking generated successfully.")
