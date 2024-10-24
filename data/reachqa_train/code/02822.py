import matplotlib.pyplot as plt
import numpy as np

# Hypothetical stress level scores for different professions
software_developers = [55, 60, 52, 48, 50, 65, 70, 54, 58, 62, 57, 63, 59, 56, 61, 68, 64, 66, 71, 53,
                       55, 60, 52, 48, 50, 65, 70, 54, 58, 62, 57, 63, 59, 56, 61, 68, 64, 66, 71, 53,
                       55, 60, 52, 48, 50, 65, 70, 54, 58, 62, 57, 63, 59, 56, 61, 68, 64, 66, 71, 53,
                       55, 60, 52, 48, 50, 65, 70, 54, 58, 62, 57, 63, 59, 56, 61, 68, 64, 66, 71, 53,
                       55, 60, 52, 48, 50, 65, 70, 54, 58, 62, 57, 63, 59, 56, 61, 68, 64, 66, 71, 53]

teachers = [70, 75, 72, 80, 69, 74, 76, 78, 73, 77, 81, 79, 71, 75, 72, 80, 69, 74, 76, 78,
            70, 75, 72, 80, 69, 74, 76, 78, 73, 77, 81, 79, 71, 75, 72, 80, 69, 74, 76, 78,
            70, 75, 72, 80, 69, 74, 76, 78, 73, 77, 81, 79, 71, 75, 72, 80, 69, 74, 76, 78,
            70, 75, 72, 80, 69, 74, 76, 78, 73, 77, 81, 79, 71, 75, 72, 80, 69, 74, 76, 78,
            70, 75, 72, 80, 69, 74, 76, 78, 73, 77, 81, 79, 71, 75, 72, 80, 69, 74, 76, 78]

healthcare_workers = [85, 90, 88, 86, 92, 87, 89, 91, 93, 84, 88, 86, 90, 89, 85, 92, 87, 93, 84, 86,
                      85, 90, 88, 86, 92, 87, 89, 91, 93, 84, 88, 86, 90, 89, 85, 92, 87, 93, 84, 86,
                      85, 90, 88, 86, 92, 87, 89, 91, 93, 84, 88, 86, 90, 89, 85, 92, 87, 93, 84, 86,
                      85, 90, 88, 86, 92, 87, 89, 91, 93, 84, 88, 86, 90, 89, 85, 92, 87, 93, 84, 86,
                      85, 90, 88, 86, 92, 87, 89, 91, 93, 84, 88, 86, 90, 89, 85, 92, 87, 93, 84, 86]

construction_workers = [65, 68, 70, 66, 72, 64, 69, 71, 67, 73, 64, 68, 70, 66, 72, 64, 69, 71, 67, 73,
                        65, 68, 70, 66, 72, 64, 69, 71, 67, 73, 64, 68, 70, 66, 72, 64, 69, 71, 67, 73,
                        65, 68, 70, 66, 72, 64, 69, 71, 67, 73, 64, 68, 70, 66, 72, 64, 69, 71, 67, 73,
                        65, 68, 70, 66, 72, 64, 69, 71, 67, 73, 64, 68, 70, 66, 72, 64, 69, 71, 67, 73,
                        65, 68, 70, 66, 72, 64, 69, 71, 67, 73, 64, 68, 70, 66, 72, 64, 69, 71, 67, 73]

customer_service = [60, 62, 59, 65, 63, 61, 67, 64, 62, 66, 64, 63, 61, 62, 65, 66, 60, 68, 64, 62,
                   60, 62, 59, 65, 63, 61, 67, 64, 62, 66, 64, 63, 61, 62, 65, 66, 60, 68, 64, 62,
                   60, 62, 59, 65, 63, 61, 67, 64, 62, 66, 64, 63, 61, 62, 65, 66, 60, 68, 64, 62,
                   60, 62, 59, 65, 63, 61, 67, 64, 62, 66, 64, 63, 61, 62, 65, 66, 60, 68, 64, 62,
                   60, 62, 59, 65, 63, 61, 67, 64, 62, 66, 64, 63, 61, 62, 65, 66, 60, 68, 64, 62]

# Create data list
data = [software_developers, teachers, healthcare_workers, construction_workers, customer_service]

# Create the horizontal box plot
fig, ax = plt.subplots(figsize=(14, 8))
ax.boxplot(data, vert=False, patch_artist=True, notch=True,
           boxprops=dict(facecolor="lightblue", color="blue"),
           whiskerprops=dict(color="blue"),
           capprops=dict(color="blue"),
           medianprops=dict(color="darkblue"),
           flierprops=dict(markerfacecolor='red', marker='o', alpha=0.5))

# Customizing the y-axis with profession labels
ax.set_yticklabels(['Software Developers', 'Teachers', 'Healthcare Workers', 'Construction Workers', 'Customer Service'])

# Add titles and labels
plt.title('Stress Levels Across Different Professions - 2023\nInsights into Occupational Health', fontsize=14, fontweight='bold')
plt.xlabel('Stress Level (Score)', fontsize=12)
plt.ylabel('Profession', fontsize=12)

# Add grid for better readability
plt.grid(linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()