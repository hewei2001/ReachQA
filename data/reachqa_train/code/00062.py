import matplotlib.pyplot as plt

# Artificial SAT score data for five fictional universities
university_data = {
    "Univ A": [1250, 1300, 1350, 1370, 1400, 1420, 1450, 1470, 1500, 1520, 1550],
    "Univ B": [1100, 1150, 1170, 1200, 1230, 1250, 1280, 1300, 1320, 1350],
    "Univ C": [1400, 1450, 1470, 1500, 1520, 1550, 1570, 1600, 1600],
    "Univ D": [1000, 1050, 1100, 1150, 1180, 1200, 1250],
    "Univ E": [1300, 1350, 1400, 1420, 1450, 1470, 1500, 1520, 1550, 1570, 1600]
}

# Extracting university names and their corresponding score data
universities = list(university_data.keys())
scores = [university_data[uni] for uni in universities]

# Set up the figure and axis for the box plot
fig, ax = plt.subplots(figsize=(10, 6))

# Create the box plot with vertical boxes, filled with color
boxprops = dict(linestyle='-', linewidth=1.5, color='black', facecolor='lightblue', alpha=0.6)
whiskerprops = dict(linestyle='--', linewidth=1.5)
capprops = dict(linewidth=1.5)
medianprops = dict(linestyle='-', linewidth=2, color='firebrick')

ax.boxplot(scores, vert=True, patch_artist=True, labels=universities,
           boxprops=boxprops, whiskerprops=whiskerprops, capprops=capprops, medianprops=medianprops)

# Adding a title and labels to the plot
ax.set_title("SAT Score Distribution for \nUniversity Applications", fontsize=14, color='navy', pad=20)
ax.set_xlabel("Universities", fontsize=12)
ax.set_ylabel("SAT Scores", fontsize=12)

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()