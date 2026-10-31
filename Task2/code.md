1. Problem Statement :
University Admission Decision Engine:
Develop a Python program to evaluate candidates for university admission based on minimum subject marks and aggregate marks. The program should identify eligible candidates and arrange them in rank order based on their aggregate marks.

2. Algorithm :
1. Start the program.
2. Read the number of candidates.
3. For each candidate, read their name and marks in Mathematics, Physics, and Chemistry.
4. Calculate the aggregate marks.
5. Check whether each subject has at least 50 marks and aggregate is at least 60.
6. Add eligible candidates to the candidate list.
7. Sort eligible candidates in descending order of aggregate marks.
8. Display the rank, name, and aggregate of each eligible candidate.
9. If there are no eligible candidates, display a suitable message.
10. Stop the program.

3. Flowchart — Mermaid Code :




4. Python Source Code:
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

5. Sample Input :
Enter number of candidates: 3

Candidate 1
Enter name: Ravi
Enter Mathematics marks: 80
Enter Physics marks: 75
Enter Chemistry marks: 70

Candidate 2
Enter name: Priya
Enter Mathematics marks: 90
Enter Physics marks: 85
Enter Chemistry marks: 80

Candidate 3
Enter name: Anu
Enter Mathematics marks: 45
Enter Physics marks: 70
Enter Chemistry marks: 75

6. Sample Output :
--- Eligible Candidates ---
1 Priya 85.0
2 Ravi 75.0

Admission ranking generated successfully.
