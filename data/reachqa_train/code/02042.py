import matplotlib.pyplot as plt

# Data for workshops
espresso_machines_participants = [55, 60, 65, 58, 70]
pour_over_participants = [45, 50, 47, 52, 53]
french_press_participants = [40, 42, 43, 45, 44]
cold_brew_participants = [30, 35, 33, 37, 36]
aeropress_participants = [25, 28, 30, 27, 31]

# Aggregate data for box plot
brewing_data = [espresso_machines_participants, pour_over_participants,
                french_press_participants, cold_brew_participants, aeropress_participants]

# Workshop labels
workshop_labels = ['Espresso Machines', 'Pour Over', 'French Press', 'Cold Brew', 'Aeropress']

# Create cumulative participant data
def cumulative_data(participants):
    cumulative = []
    total = 0
    for num in participants:
        total += num
        cumulative.append(total)
    return cumulative

espresso_cumulative = cumulative_data(espresso_machines_participants)
pour_over_cumulative = cumulative_data(pour_over_participants)
french_press_cumulative = cumulative_data(french_press_participants)
cold_brew_cumulative = cumulative_data(cold_brew_participants)
aeropress_cumulative = cumulative_data(aeropress_participants)

# Time periods (e.g., months)
time_periods = range(1, len(espresso_machines_participants) + 1)

# Plot setup
fig, axs = plt.subplots(1, 2, figsize=(18, 7))

# First subplot: Box Plot
axs[0].boxplot(brewing_data, vert=False, patch_artist=True, labels=workshop_labels, notch=True,
               boxprops=dict(facecolor='lightgoldenrodyellow', color='darkgoldenrod'),
               whiskerprops=dict(color='darkgoldenrod'),
               capprops=dict(color='darkgoldenrod'),
               medianprops=dict(color='maroon', linewidth=1.5))
colors = ['bisque', 'sandybrown', 'peachpuff', 'tan', 'peru']
for patch, color in zip(axs[0].patches, colors):
    patch.set_facecolor(color)
axs[0].set_title('The Evolution of Coffee Brewing Techniques:\nAn Artful Journey in Coffee Houses', fontsize=16, weight='bold', pad=20)
axs[0].set_xlabel('Number of Participants', fontsize=12)
axs[0].set_ylabel('Brewing Techniques', fontsize=12)
axs[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7, axis='x')

# Second subplot: Line Plot
axs[1].plot(time_periods, espresso_cumulative, marker='o', color='bisque', label='Espresso Machines')
axs[1].plot(time_periods, pour_over_cumulative, marker='o', color='sandybrown', label='Pour Over')
axs[1].plot(time_periods, french_press_cumulative, marker='o', color='peachpuff', label='French Press')
axs[1].plot(time_periods, cold_brew_cumulative, marker='o', color='tan', label='Cold Brew')
axs[1].plot(time_periods, aeropress_cumulative, marker='o', color='peru', label='Aeropress')
axs[1].set_title('Cumulative Growth in Workshop Participation', fontsize=16, weight='bold', pad=20)
axs[1].set_xlabel('Time Period (Months)', fontsize=12)
axs[1].set_ylabel('Cumulative Number of Participants', fontsize=12)
axs[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
axs[1].legend(loc='upper left')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()