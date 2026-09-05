# Q5 - pandas and csv analysis
# run this from the task-0 folder

import pandas as pd

df = pd.read_csv("data/student_performance.csv")

print("First 5 rows:")
print(df.head())

print()
print("Rows:", df.shape[0], " Columns:", df.shape[1])
print("Columns:", list(df.columns))

print()
print("Missing values:")
print(df.isnull().sum())

print()
print("Average final score:", round(df["Final_Score"].mean(), 2))

top = df.loc[df["Final_Score"].idxmax()]
print("Highest scorer:", top["Student"], "with", top["Final_Score"])

# new column
df["Improvement"] = df["Final_Score"] - df["Previous_Score"]

print()
print("Students with attendance >= 80:")
good_attendance = df[df["Attendance"] >= 80]
print(good_attendance.head(10))
print("total such students:", len(good_attendance))

df = df.sort_values("Final_Score", ascending=False)
print()
print("Sorted by final score:")
print(df.head())

df.to_csv("data/processed_student_performance.csv", index=False)
print()
print("saved processed_student_performance.csv")
