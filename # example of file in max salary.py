# # salary
# Read salaries and names from the file
file_s = open("salary.txt", "r")

# Initialize variables to store the maximum salary and corresponding name
max_salary = 0
highest_salary_person = ""

# Iterate through the data and find the person with the highest salary
for line in file_s:
    salary, name = line.strip().split()
    salary = float(salary)
    
    if salary > max_salary:
        max_salary = salary
        highest_salary_person = name

file_s.close()

print("The person with the highest salary is:" , highest_salary_person)
