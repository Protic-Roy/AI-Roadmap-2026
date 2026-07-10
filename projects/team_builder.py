applicants = [
    {
        "name": "Roy",
        "skills": ["Python", "Machine Learning"],
        "experience": 2
    },
    {
        "name": "Alice",
        "skills": ["Python", "Data Analysis"],
        "experience": 5
    },
    {
        "name": "Bob",
        "skills": ["Java", "SQL"],
        "experience": 4
    },
    {
        "name": "David",
        "skills": ["Python", "Deep Learning"],
        "experience": 1
    },
    {
        "name": "Eva",
        "skills": ["Python", "AI"],
        "experience": 6
    }
]

print("APPLICANTS\n")

for applicant in applicants:
    print(f"{applicant["name"]} knows:")
    for skill in applicant["skills"]:
        print(f"   .{skill}")
    print ("-"*30)



#filter applicants

python_applicants = [
    applicant for applicant in applicants
    if ("Python" in applicant["skills"])

]
print("\n=== 🐍 PYTHON APPLICANTS ===")
for applicant in python_applicants:
    skills = ", ".join(applicant["skills"])
    print(f"- {applicant['name']:<8} | Exp: {applicant['experience']} yrs | Skills: {skills}")
    

experienced_applicants = [
 applicant for applicant in python_applicants 
 if(applicant["experience"] >3) 

]
beginner_applicants = [
 applicant for applicant in python_applicants
 if(applicant["experience"] <= 3) 

]

teams = list(zip(experienced_applicants,beginner_applicants))


total_applicants = len(applicants)
py_applicants_count = len(python_applicants)
experienced_applicant_count = len(experienced_applicants)
beginner_applicant_count = len(beginner_applicants)
team_count = len(teams)

print("\n")
print("="*30)
print(f"Total Applicants = {total_applicants}")
print(f"Python Applicants = {py_applicants_count}")
print(f"Experienced = {experienced_applicant_count}")
print(f"Beginner = {beginner_applicant_count}")
print(f"Teams Counted = {team_count}")

print("="*30)
print("\nHackathon Teams\n")

for number, team in enumerate(teams, start=1):

    senior = team[0]
    junior = team[1]

    print(f"""
========== Team {number} ==========
Senior : {senior["name"]} ({senior["experience"]} years)
Junior : {junior["name"]} ({junior["experience"]} years)
===================================
""")
