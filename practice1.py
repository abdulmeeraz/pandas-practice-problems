import pandas as pd

df = pd.read_csv("employees.csv")
# 👉 Tasks:

# Print the dataset

print(df)

# Show first 3 rows

print(df.head(3))

# Show last 2 rows

print(df.tail(2))

# Print column names

print(df.columns)


# 🧩 QUESTION 2: Salary Analysis

# 👉 Tasks:

# Find average salary

print("Average salary :",round(df["Salary"].mean(),2))

# Find maximum salary

print("Maximum salary :",df["Salary"].max())

# Find minimum salary

print("Minimum Salary :",df["Salary"].min())

# 🧩 QUESTION 3: Filter Data

# 👉 Tasks:

# Employees with salary greater than 40,000

print("Salary Grater than 40,000 :\n",df[df["Salary"]>40000])

# Employees in IT department

print("Employees in IT department :\n",df[df["Department"]=="IT"])

# Employees aged above 30

print("Employees aged above 30 :\n",df[df["Age"]>30])

# 🧩 QUESTION 4: Add New Columns

# 👉 Tasks:

# Add column Bonus → 10% of Salary

df["Bonus"] = df["Salary"] * 0.10
print(df)
# Add column Total_Pay → Salary + Bonus

df["Total_pay"] = df["Salary"]+df["Bonus"]
print(df)

# 🧩 QUESTION 5: Conditional Column

# 👉 Task:
# Create column Level

# Rules:

# Experience ≥ 10 → "Senior"

# Experience ≥ 5 → "Mid"

# Else → "Junior"

df["Level"] = "Junior"
df.loc[df["Experience"]>=5,"Level"] = "Mid"
df.loc[df["Experience"]>=10,"Level"] = "Senior"

print(df)

# 🧩 QUESTION 6: Group By (VERY IMPORTANT)

# 👉 Tasks:

# Average salary by department

print(df.groupby("Department")["Salary"].mean())


# Total salary by department

print(df.groupby("Department")["Salary"].sum())

# Count employees per department

print(df.groupby("Department")["Name"].count())

# 🧩 QUESTION 7: Sorting

# 👉 Tasks:

# Sort employees by salary (ascending)

print(df.sort_values("Salary",ascending=True))


# Sort employees by experience (descending)

print(df.sort_values("Salary",ascending=False))

# 🧩 QUESTION 8: Top & Bottom Records

# 👉 Tasks:

# Highest paid employee

print(df.loc[df["Salary"].idxmax()])

# Lowest paid employee

print(df.loc[df["Salary"].idxmin()])

# Top 2 salaries

print(df.nlargest(2,"Salary"))

# 🧩 QUESTION 9: Multiple Conditions

# 👉 Tasks:

# IT employees with salary > 40,000

IT_sal = (df["Department"]=="IT") & (df["Salary"] > 40000)

# HR employees with experience < 4

HR_exp = (df["Department"]=="HR") & (df["Experience"] < 4)

print(df[IT_sal | HR_exp])

# 🧩 QUESTION 10: Real Interview Question ⭐

# 👉 Task:
# Find department with highest average salary

print("Depatment with highest average salary :",df.groupby("Department")["Salary"].mean().idxmax())

# 🔥 Challenge 1

# Add column Tax:

df["Tax"] = df["Salary"]*0.10

# Salary > 50,000 → 20%
# Else → 10%

df.loc[df["Salary"]>50000,"Tax"] = df["Salary"]*0.20

print(df)

# 🔥 Challenge 2

# Find most experienced employee in each department

print(df.loc[df.groupby("Department")["Experience"].idxmax()])

# 🔥 Challenge 3

# Calculate salary-to-experience ratio

df["salary_to_exp_ratio"] = (df["Salary"] / df["Experience"]).replace(0,pd.NA).round(2)

print(df)
