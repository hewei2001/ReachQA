import matplotlib.pyplot as plt
import numpy as np

# Data for stress levels across different professions
professions = ['Software Developers', 'Teachers', 'Healthcare Workers', 'Construction Workers', 'Customer Service']
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
data = [software_developers, teachers, healthcare_workers, construction_workers, customer_service]

# Construct average stress data as a new perspective
average_stress = [np.mean(prof_data) for prof_data in data]
profession_indices = np.arange(len(professions))

# Create a figure with 1x2 subplots
fig, axs = plt.subplots(1, 2, figsize=(18, 8))

# Plot the horizontal box plot
axs[0].boxplot(data, vert=False, patch_artist=True, notch=True,
               boxprops=dict(facecolor="lightblue", color="blue"),
               whiskerprops=dict(color="blue"),
               capprops=dict(color="blue"),
               medianprops=dict(color="darkblue"),
               flierprops=dict(markerfacecolor='red', marker='o', alpha=0.5))
axs[0].set_yticklabels(professions)
axs[0].set_title('Stress Levels Across Different Professions\nInsights into Occupational Health', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Stress Level (Score)')
axs[0].set_ylabel('Profession')
axs[0].grid(linestyle='--', alpha=0.7)

# Plot an additional bar chart of average stress levels
axs[1].barh(profession_indices, average_stress, color='skyblue', edgecolor='blue')
axs[1].set_yticks(profession_indices)
axs[1].set_yticklabels(professions)
axs[1].set_title('Average Stress Levels\nPer Profession', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Average Stress Level (Score)')
axs[1].grid(linestyle='--', alpha=0.7)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()