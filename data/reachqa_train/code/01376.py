import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2021)

# Hypothetical data: Monthly active users in millions
lingualeap_users = [0.5, 1.0, 1.5, 2.5, 3.5, 4.5, 6.0, 7.0, 9.0, 11.0, 12.5]
polyglotpro_users = [0.2, 0.3, 0.6, 1.0, 1.8, 3.0, 4.5, 5.5, 8.5, 12.0, 15.0]
verboventures_users = [1.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 5.5, 6.5, 7.0, 7.5]

# Create a figure and axis for plotting
fig, ax = plt.subplots(figsize=(12, 6))

# Plot lines for each app with different styles
ax.plot(years, lingualeap_users, marker='o', linestyle='-', color='#4a90e2', linewidth=2, label='LinguaLeap')
ax.plot(years, polyglotpro_users, marker='s', linestyle='--', color='#e94e77', linewidth=2, label='PolyglotPro')
ax.plot(years, verboventures_users, marker='^', linestyle='-.', color='#50e3c2', linewidth=2, label='VerboVentures')

# Customize the title and axis labels
ax.set_title('The Evolution of Language Learning Apps\nMonthly Active Users (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Monthly Active Users (Millions)', fontsize=12)

# Customize x-ticks
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

# Add a legend
ax.legend(title='Language Learning Apps', loc='upper left', fontsize=10)

# Annotate key milestones
annotations = {
    2015: ("LinguaLeap Features Launch", lingualeap_users[5]),
    2018: ("PolyglotPro Partnerships", polyglotpro_users[8]),
    2020: ("VerboVentures Steady Growth", verboventures_users[10]),
}

for year, (text, y_value) in annotations.items():
    ax.annotate(text, xy=(year, y_value), xytext=(year, y_value + 1.5),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5), fontsize=10, color='black', ha='center')

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()