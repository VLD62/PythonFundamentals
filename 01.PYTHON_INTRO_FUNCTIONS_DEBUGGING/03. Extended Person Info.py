name = input()
age = int(input())
town = input()
salary = float(input())
age_range = ""
salary_range = " "

if age < 18:
    age_range = 'teen'
elif age < 70:
	age_range = 'adult'
else:
    age_range = 'elder'

if salary < 500:
    salary_range = 'low'
elif salary < 2000:
	salary_range = 'medium'
else:
    salary_range = 'high'

print(f"Name: {name}\n"
      f"Age: {age}\n"
      f"Town: {town}\n"
      f"Salary: ${salary:.2f}\n"
      f"Age range: {age_range}\n"
      f"Salary range: {salary_range}\n")