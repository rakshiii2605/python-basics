import pandas as pd

df = pd.read_csv("student_marks.csv")

print("📊 First 5 Rows of Data:")
print(df.head(), "\n")

print("📈 Summary Statistics:")
print(df.describe(), "\n")

print("ℹ️ Info About Dataset:")
print(df.info())
