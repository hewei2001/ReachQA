import matplotlib.pyplot as plt
import numpy as np

# Define years and publication data for each technology
years = np.arange(2015, 2026)
ai_publications = np.array([300, 350, 400, 480, 550, 630, 700, 780, 850, 950, 1050])
quantum_computing_publications = np.array([50, 60, 80, 100, 120, 160, 200, 250, 300, 380, 460])
biotech_publications = np.array([200, 220, 250, 270, 290, 320, 350, 390, 430, 480, 540])
renewable_energy_publications = np.array([150, 180, 220, 250, 280, 310, 360, 420, 490, 570, 650])
cybersecurity_publications = np.array([180, 210, 240, 280, 320, 370, 420, 480, 540, 620, 710])

# Calculate percentage share for new plot
total_publications = ai_publications + quantum_computing_publications + biotech_publications + \
                     renewable_energy_publications + cybersecurity_publications

ai_share = (ai_publications / total_publications) * 100
quantum_share = (quantum_computing_publications / total_publications) * 100
biotech_share = (biotech_publications / total_publications) * 100
renewable_share = (renewable_energy_publications / total_publications) * 100
cybersecurity_share = (cybersecurity_publications / total_publications) * 100

# Initialize subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Stacked Bar Plot
ax1.bar(years, ai_publications, label='AI', color='#ff9999', edgecolor='black')
ax1.bar(years, quantum_computing_publications, bottom=ai_publications, label='Quantum Computing', color='#66b3ff', edgecolor='black')
ax1.bar(years, biotech_publications, bottom=ai_publications + quantum_computing_publications, label='Biotechnology', color='#99ff99', edgecolor='black')
ax1.bar(years, renewable_energy_publications, bottom=ai_publications + quantum_computing_publications + biotech_publications, label='Renewable Energy', color='#ffcc99', edgecolor='black')
ax1.bar(years, cybersecurity_publications, bottom=ai_publications + quantum_computing_publications + biotech_publications + renewable_energy_publications, label='Cybersecurity', color='#c2c2f0', edgecolor='black')

ax1.set_title('Evolution of Research Publications\nin Emerging Technologies (2015-2025)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Publications', fontsize=12)
ax1.legend(loc='upper left', title='Technology Sectors', fontsize=10, title_fontsize='13')
ax1.grid(True, linestyle='--', alpha=0.5)

# Line Plot for Percentage Share
ax2.plot(years, ai_share, marker='o', label='AI', color='#ff9999')
ax2.plot(years, quantum_share, marker='s', label='Quantum Computing', color='#66b3ff')
ax2.plot(years, biotech_share, marker='^', label='Biotechnology', color='#99ff99')
ax2.plot(years, renewable_share, marker='d', label='Renewable Energy', color='#ffcc99')
ax2.plot(years, cybersecurity_share, marker='*', label='Cybersecurity', color='#c2c2f0')

ax2.set_title('Percentage Share of Publications\nin Emerging Technologies (2015-2025)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Percentage Share (%)', fontsize=12)
ax2.legend(loc='upper right', title='Technology Sectors', fontsize=10, title_fontsize='13')
ax2.grid(True, linestyle='--', alpha=0.5)

# Adjust ticks and layout
ax1.set_xticks(years)
ax2.set_xticks(years)
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
plt.tight_layout()

# Display the plot
plt.show()