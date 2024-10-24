import matplotlib.pyplot as plt
import numpy as np

# Define the data for extended years and quarterly granularity
years = np.arange(1980, 2025, 0.25)  # From 1980 to 2024 in quarterly increments

# Define growth functions for technologies
def logistic_growth(t, L=100, k=0.1, x0=2000):
    return L / (1 + np.exp(-k * (t - x0)))

# Data for each communication technology (normalized between 0 and 100)
email_usage = logistic_growth(years, x0=2000, L=80)
social_media_usage = logistic_growth(years, x0=2010, L=90)
video_conferencing_usage = logistic_growth(years, x0=2015, L=85)
messaging_apps_usage = logistic_growth(years, x0=2010, L=100)
mobile_apps_usage = logistic_growth(years, x0=2008, L=95)
iot_devices_usage = logistic_growth(years, x0=2020, L=50)

# Plotting setup
fig, ax = plt.subplots(figsize=(14, 8))

# Stacked area plot
ax.stackplot(years, email_usage, social_media_usage, video_conferencing_usage, messaging_apps_usage, 
             mobile_apps_usage, iot_devices_usage,
             labels=['Email', 'Social Media', 'Video Conferencing', 'Messaging Apps', 'Mobile Apps', 'IoT Devices'],
             colors=['#FFD700', '#87CEEB', '#FF69B4', '#32CD32', '#FF4500', '#8A2BE2'], alpha=0.8)

# Customizing plot appearance
ax.set_title("Evolution of Digital Communication Technologies\n(1980 - 2024)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Global Usage (% Normalized)', fontsize=14)
ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 500)  # Adjusted to accommodate the new technology data

# Set x-ticks to show every 5 years
ax.set_xticks(np.arange(1980, 2025, 5))

# Rotate x-axis labels to avoid overlap
plt.xticks(rotation=45)

# Adding a legend
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title="Communication Mediums", fontsize=12)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Add annotations for significant technological milestones
milestones = {
    1985: "Introduction of Internet",
    2007: "Smartphones become mainstream",
    2010: "Social Media Boom",
    2020: "Rise of IoT Devices"
}

for year, event in milestones.items():
    plt.annotate(event, xy=(year, 20), xytext=(year, 100),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 fontsize=10, rotation=45, ha='center')

# Show the chart
plt.show()