import pandas as pd

df = pd.read_csv("student_marks.csv")

print("👩‍🎓 Average Marks by Subject:")
print(df.groupby("Subject")["Marks"].mean(), "\n")

print("🏆 Highest Marks by Subject:")
print(df.groupby("Subject")["Marks"].max())
