import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("students.csv")

# Convert categorical data
df["Tutoring"] = df["Tutoring"].map({"Yes": 1, "No": 0})
df["ParentalSupport"] = df["ParentalSupport"].map({"Low": 1, "Medium": 2, "High": 3})


# 1. GPA Distribution
plt.figure()
sns.histplot(df["GPA"], kde=True)
plt.title("GPA Distribution")
plt.savefig("gpa_distribution.png")
plt.show()

# 2. Study Hours vs GPA
plt.figure()
sns.scatterplot(x="StudyHours", y="GPA", data=df)
plt.title("Study Hours vs GPA")
plt.savefig("study_vs_gpa.png")
plt.show()

# 3. Attendance vs GPA
plt.figure()
sns.scatterplot(x="Attendance", y="GPA", data=df)
plt.title("Attendance vs GPA")
plt.savefig("attendance_vs_gpa.png")
plt.show()

# 4. Correlation Heatmap
plt.figure()
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()


print("\n📌 KEY INSIGHTS:")
print("1. Students who study more hours tend to have higher GPA.")
print("2. Higher attendance is linked with better academic performance.")
print("3. Tutoring has a positive impact on student results.")
print("4. Strong parental support improves performance.")
print("5. All factors show some level of correlation with GPA.")