import matplotlib.pyplot as plt
import numpy as np

# Define the swordsmanship styles and their respective scores from competitions
styles = ["Samurai\nKenjutsu", "Medieval\nLongsword", "Renaissance\nRapier", "Viking\nSwordsmanship"]
scores_kenjutsu = [85, 88, 82, 89, 90, 95, 83, 87, 88, 92, 94, 78, 85, 81, 89]
scores_longsword = [78, 75, 80, 76, 84, 83, 82, 79, 77, 81, 85, 88, 86, 90]
scores_rapier = [90, 92, 94, 95, 88, 93, 91, 90, 92, 94, 89, 85, 87, 93, 91]
scores_viking = [70, 72, 68, 74, 77, 76, 75, 73, 69, 70, 72, 74, 76, 71, 75]

# Combine the scores into a list for the boxplot
boxplot_data = [scores_kenjutsu, scores_longsword, scores_rapier, scores_viking]

# Calculate average scores for the bar chart
avg_scores = [np.mean(scores) for scores in boxplot_data]

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Box plot
axs[0].boxplot(boxplot_data, patch_artist=True, notch=True,
               boxprops=dict(facecolor="lightblue", color="blue"),
               capprops=dict(color="blue"),
               whiskerprops=dict(color="blue"),
               flierprops=dict(markerfacecolor='red', marker='o'),
               medianprops=dict(color="green"))

axs[0].set_title("Legendary Swordsmanship Festival:\nScores of Various Sword Styles", fontsize=14, pad=15)
axs[0].set_xlabel("Swordsmanship Styles", fontsize=12)
axs[0].set_ylabel("Score", fontsize=12)
axs[0].set_xticks(np.arange(1, len(styles) + 1))
axs[0].set_xticklabels(styles, fontsize=11)
axs[0].grid(axis='y', linestyle='--', alpha=0.7)

# Bar chart
bars = axs[1].bar(styles, avg_scores, color=['skyblue', 'lightgreen', 'salmon', 'goldenrod'])
axs[1].set_title("Average Scores for Swordsmanship Styles", fontsize=14, pad=15)
axs[1].set_xlabel("Swordsmanship Styles", fontsize=12)
axs[1].set_ylabel("Average Score", fontsize=12)

# Add value labels on the bars
for bar in bars:
    yval = bar.get_height()
    axs[1].text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, round(yval, 2), ha='center', va='bottom')

# Automatically adjust layout to fit all elements
plt.tight_layout()

# Display the plots
plt.show()