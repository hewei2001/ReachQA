import matplotlib.pyplot as plt
import numpy as np

# Categories for cybersecurity threats
categories = ['Malware', 'Phishing', 'Ransomware', 'Insider Threats', 'DDoS Attacks', 'Zero-day Exploits']
n_categories = len(categories)

# Severity scores for each threat category (1 to 10 scale)
severity_scores = np.array([8, 6, 7, 5, 9, 8])

# Duplicate the first value to close the radar chart loop
scores = np.concatenate((severity_scores, [severity_scores[0]]))

# Angles for each category on the radar chart
angles = np.linspace(0, 2 * np.pi, n_categories, endpoint=False).tolist()
angles += angles[:1]

# Create radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot radar chart data
ax.plot(angles, scores, color='red', linewidth=2, linestyle='solid')
ax.fill(angles, scores, color='red', alpha=0.3)

# Add labels for each category
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)

# Set y-axis limits and remove y-ticks labels
ax.set_ylim(0, 10)
ax.set_yticklabels([])

# Add title and styling
plt.title("Cybersecurity Threat Landscape 2023\nSeverity Levels of Various Threats", size=15, weight='bold', pad=30)
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_facecolor('#eef0f2')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()