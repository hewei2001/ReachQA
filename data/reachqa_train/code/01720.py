import matplotlib.pyplot as plt

# Define the data for sleep hours in a day
computer_science_sleep = [5, 6, 6, 5.5, 7, 6.5, 6, 7, 6, 8]
literature_sleep = [6, 7, 7.5, 6.5, 8, 7.5, 7, 8, 6, 7.5]
engineering_sleep = [5, 5.5, 6, 5, 6.5, 5.5, 6, 6, 5.5, 7]
psychology_sleep = [6, 7, 6.5, 7, 7.5, 7, 7, 8, 7.5, 8.5]
fine_arts_sleep = [7, 8, 8.5, 7.5, 8, 7.5, 7, 9, 8, 8.5]

# Alertness levels at different times of day (arbitrary values)
times_of_day = ['Early Morning', 'Late Morning', 'Afternoon', 'Evening', 'Night']
cs_alertness = [3, 5, 4, 6, 2]
lit_alertness = [4, 5, 6, 5, 3]
eng_alertness = [3, 4, 4, 5, 2]
psy_alertness = [5, 6, 5, 7, 4]
fa_alertness = [4, 5, 5, 6, 3]

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Box plot for sleep data
sleep_data = [computer_science_sleep, literature_sleep, engineering_sleep, psychology_sleep, fine_arts_sleep]
majors = ['Computer Science', 'Literature', 'Engineering', 'Psychology', 'Fine Arts']
boxplot = ax1.boxplot(sleep_data, vert=False, patch_artist=True, notch=True,
                      boxprops=dict(facecolor='lightblue', color='blue'),
                      whiskerprops=dict(color='blue'), capprops=dict(color='blue'),
                      flierprops=dict(marker='o', color='red', alpha=0.5),
                      medianprops=dict(color='red', linewidth=2))

ax1.set_yticklabels(majors, fontsize=12)
ax1.set_xlabel('Hours of Sleep per Day', fontsize=12)
ax1.set_title('Student Sleep Patterns\nAcross Various University Majors', fontsize=14, fontweight='bold')

colors = ['lightcoral', 'lightgreen', 'lightskyblue', 'plum', 'wheat']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

ax1.grid(axis='x', linestyle='--', alpha=0.7)

# Line plot for alertness levels
ax2.plot(times_of_day, cs_alertness, label='Computer Science', marker='o', color='lightcoral')
ax2.plot(times_of_day, lit_alertness, label='Literature', marker='o', color='lightgreen')
ax2.plot(times_of_day, eng_alertness, label='Engineering', marker='o', color='lightskyblue')
ax2.plot(times_of_day, psy_alertness, label='Psychology', marker='o', color='plum')
ax2.plot(times_of_day, fa_alertness, label='Fine Arts', marker='o', color='wheat')

ax2.set_xlabel('Time of Day', fontsize=12)
ax2.set_ylabel('Average Alertness Level', fontsize=12)
ax2.set_title('Average Student Alertness\nAcross Times of Day', fontsize=14, fontweight='bold')
ax2.legend(title='Majors', fontsize=10)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()