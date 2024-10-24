import matplotlib.pyplot as plt
import numpy as np

# Define years and publication data for each technology
years = np.arange(2015, 2026)
ai_publications = np.array([300, 350, 400, 480, 550, 630, 700, 780, 850, 950, 1050])
quantum_computing_publications = np.array([50, 60, 80, 100, 120, 160, 200, 250, 300, 380, 460])
biotech_publications = np.array([200, 220, 250, 270, 290, 320, 350, 390, 430, 480, 540])
renewable_energy_publications = np.array([150, 180, 220, 250, 280, 310, 360, 420, 490, 570, 650])
cybersecurity_publications = np.array([180, 210, 240, 280, 320, 370, 420, 480, 540, 620, 710])

# Stack the data
publication_data = np.vstack([ai_publications, quantum_computing_publications, biotech_publications, 
                              renewable_energy_publications, cybersecurity_publications])

# Initialize plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plotting the stacked bars
ax.bar(years, ai_publications, label='AI', color='#ff9999', edgecolor='black')
ax.bar(years, quantum_computing_publications, bottom=ai_publications, label='Quantum Computing', color='#66b3ff', edgecolor='black')
ax.bar(years, biotech_publications, bottom=ai_publications + quantum_computing_publications, label='Biotechnology', color='#99ff99', edgecolor='black')
ax.bar(years, renewable_energy_publications, bottom=ai_publications + quantum_computing_publications + biotech_publications, label='Renewable Energy', color='#ffcc99', edgecolor='black')
ax.bar(years, cybersecurity_publications, bottom=ai_publications + quantum_computing_publications + biotech_publications + renewable_energy_publications, label='Cybersecurity', color='#c2c2f0', edgecolor='black')

# Adding title and labels
ax.set_title('Evolution of Research Publications\nin Emerging Technologies (2015-2025)', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Publications', fontsize=12)

# Adding a legend
ax.legend(loc='upper left', title='Technology Sectors', fontsize=10, title_fontsize='13')

# Adding grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Adjusting ticks and layout
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 3001, 300))  # Adjust y-axis ticks
plt.tight_layout()

# Display the plot
plt.show()