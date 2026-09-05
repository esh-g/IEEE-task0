# Q6 - matplotlib plots
# uses the processed csv from q5, so run q5.py first

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed_student_performance.csv")

# 1. bar chart of students vs final score
plt.figure(figsize=(14, 6))
plt.bar(df["Student"], df["Final_Score"])
plt.xticks(rotation=90, fontsize=7)
plt.title("Final Score of Each Student")
plt.xlabel("Student")
plt.ylabel("Final Score")
plt.tight_layout()
plt.savefig("plots/final_scores.png")
plt.close()

# 2. scatter of hours studied vs final score
plt.figure()
plt.scatter(df["Hours_Studied"], df["Final_Score"])
plt.title("Hours Studied vs Final Score")
plt.xlabel("Hours Studied")
plt.ylabel("Final Score")
plt.tight_layout()
plt.savefig("plots/study_vs_score.png")
plt.close()

# 3. histogram of final scores
plt.figure()
plt.hist(df["Final_Score"], bins=10, edgecolor="black")
plt.title("Distribution of Final Scores")
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("plots/score_distribution.png")
plt.close()

# 4. my own plot - attendance vs final score
# wanted to check if attendance matters as much as study hours, looks like it doesn't
plt.figure()
plt.scatter(df["Attendance"], df["Final_Score"], color="green")
plt.title("Attendance vs Final Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Final Score")
plt.tight_layout()
plt.savefig("plots/custom_plot.png")
plt.close()

print("all 4 plots saved in plots folder")
