import matplotlib.pyplot as plt
import numpy as np

# Define the years (quarterly data from 2010 to 2020)
quarters = np.arange(2010, 2020.75, 0.25)  # Changed the end value to ensure it has the same length as user arrays

# Hypothetical data: Quarterly active users in millions
lingualeap_users = np.array([0.5, 0.7, 0.8, 1.0, 1.2, 1.4, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.5, 9.0, 10.0, 11.0, 12.0, 12.5, 13.0, 14.0, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5])
polyglotpro_users = np.array([0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.75, 1.0, 1.2, 1.4, 1.8, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.5, 15.0, 16.0, 17.0, 18.5, 19.5, 21.0, 22.0, 23.5, 24.0, 25.0, 26.0, 27.0, 28.0, 29.5, 30.0])
verboventures_users = np.array([1.0, 1.2, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5])

# Create a figure with subplots
fig, ax = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# Plot user data with additional detail
ax[0].plot(quarters, lingualeap_users, marker='o', linestyle='-', color='#4a90e2', linewidth=2, label='LinguaLeap')
ax[0].plot(quarters, polyglotpro_users, marker='s', linestyle='--', color='#e94e77', linewidth=2, label='PolyglotPro')
ax[0].plot(quarters, verboventures_users, marker='^', linestyle='-.', color='#50e3c2', linewidth=2, label='VerboVentures')

# Calculate and plot the rate of change (first derivative)
lingualeap_rate = np.gradient(lingualeap_users)
polyglotpro_rate = np.gradient(polyglotpro_users)
verboventures_rate = np.gradient(verboventures_users)

ax[1].plot(quarters, lingualeap_rate, marker='o', linestyle='-', color='#4a90e2', linewidth=1.5, label='LinguaLeap Growth Rate')
ax[1].plot(quarters, polyglotpro_rate, marker='s', linestyle='--', color='#e94e77', linewidth=1.5, label='PolyglotPro Growth Rate')
ax[1].plot(quarters, verboventures_rate, marker='^', linestyle='-.', color='#50e3c2', linewidth=1.5, label='VerboVentures Growth Rate')

# Customize the title and axis labels
ax[0].set_title('The Evolution of Language Learning Apps\nMonthly Active Users (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax[0].set_ylabel('Monthly Active Users (Millions)', fontsize=12)
ax[1].set_title('Growth Rate of Monthly Active Users (Millions)', fontsize=14, fontweight='bold', pad=20)
ax[1].set_xlabel('Year', fontsize=12)
ax[1].set_ylabel('Rate of Change (Millions/Quarter)', fontsize=12)

# Customize x-ticks
ax[1].set_xticks(quarters[::4])  # Show ticks only on the start of the year
ax[1].set_xticklabels(range(2010, 2021), rotation=45)

# Add legends
ax[0].legend(title='Language Learning Apps', loc='upper left', fontsize=10)
ax[1].legend(title='Growth Rates', loc='upper right', fontsize=10)

# Annotate key milestones on the user plot
annotations_users = {
    2015: ("LinguaLeap\nFeatures Launch", lingualeap_users[20]),
    2018: ("PolyglotPro\nPartnerships", polyglotpro_users[32]),
    2020: ("VerboVentures\nSteady Growth", verboventures_users[42]),
}

for year, (text, y_value) in annotations_users.items():
    ax[0].annotate(text, xy=(year, y_value), xytext=(year, y_value + 2),
                   arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
                   fontsize=9, color='black', ha='center')

# Add grids for better readability
ax[0].grid(True, linestyle='--', alpha=0.6)
ax[1].grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()