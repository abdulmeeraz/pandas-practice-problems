import pandas as pd

df = pd.read_csv("students.csv")

print(df)


print("First 2 rows\n")

print(df.head(2))

df["Total"] = df["Maths"] + df["Science"] + df["English"]

df["Average"] = round(df["Total"]/3,2)

print(df)

topper = df.loc[df["Total"].idxmax()]

print(topper)

df["Pass/Fail"] = df["Average"]>=50

print(df)

failed = df[df["Pass/Fail"]==False]
print("Failed Students\n")
print(failed)

print("Subject wise Average\n")

print(df[["Maths","Science","English"]].mean())

print("Basic Statics\n")
print(df.describe())
