import pandas as pd

df = pd.read_csv("student_marks.csv")

# Display top 3 students overall
print("🏆 Top 3 Students Overall:")
print(df.sort_values(by="Marks", ascending=False).head(3), "\n")

# Students scoring above 80
print("📌 Students scoring above 80:")
print(df[df["Marks"] > 80], "\n")

# Export filtered data
df[df["Marks"] > 80].to_csv("top_students.csv", index=False)
print("✅ Filtered results saved to top_students.csv")
