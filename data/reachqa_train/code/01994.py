import matplotlib.pyplot as plt

# Define months and satisfaction scores for three fictional schools
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
school_a_scores = [65, 70, 75, 78, 82, 85]
school_b_scores = [60, 64, 69, 72, 75, 79]
school_c_scores = [58, 62, 66, 70, 74, 77]

# Set up the plotting area
plt.figure(figsize=(12, 6))

# Plot lines with markers for each school
plt.plot(months, school_a_scores, marker='o', linestyle='-', color='#FF5733', linewidth=2, label='School A')
plt.plot(months, school_b_scores, marker='s', linestyle='-', color='#33FFBD', linewidth=2, label='School B')
plt.plot(months, school_c_scores, marker='^', linestyle='-', color='#FF33A6', linewidth=2, label='School C')

# Annotate each data point with its satisfaction score
for i, (a, b, c) in enumerate(zip(school_a_scores, school_b_scores, school_c_scores)):
    plt.text(months[i], a + 1, f"{a}", ha='center', va='bottom', fontsize=9, color='#FF5733', fontweight='bold')
    plt.text(months[i], b + 1, f"{b}", ha='center', va='bottom', fontsize=9, color='#33FFBD', fontweight='bold')
    plt.text(months[i], c + 1, f"{c}", ha='center', va='bottom', fontsize=9, color='#FF33A6', fontweight='bold')

# Title and axis labels
plt.title('Impact of Innovative Teaching Methods\non Student Satisfaction (2023)', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Satisfaction Score', fontsize=12)

# Add a grid and legend to the plot
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Schools', loc='lower right', fontsize=10)

# Automatically adjust the layout
plt.tight_layout()

# Show the plot
plt.show()