import matplotlib.pyplot as plt

# Data Construction
years = list(range(2010, 2024))

# Technology Adoption Rates (in percentage)
adoption_rates = {
    'DAW Adoption': [30, 35, 45, 50, 60, 65, 68, 70, 72, 75, 77, 80, 82, 85],
    'Streaming Services': [5, 10, 15, 20, 30, 40, 45, 55, 60, 70, 75, 80, 85, 90],
    'AI Music Production': [0, 0, 1, 2, 3, 5, 7, 10, 12, 15, 18, 20, 25, 30],
    'VR/AR Music Experiences': [0, 0, 0, 0, 1, 2, 3, 5, 6, 10, 12, 15, 18, 20]
}

# Technology Revenue Growth in the music industry
revenue_growth = {
    'DAW Adoption': [500, 550, 700, 800, 1000, 1200, 1260, 1300, 1340, 1400, 1460, 1500, 1540, 1600],
    'Streaming Services': [100, 200, 300, 500, 700, 900, 1200, 1500, 1600, 1800, 2000, 2200, 2400, 2500],
    'AI Music Production': [10, 10, 20, 30, 40, 60, 80, 100, 120, 140, 160, 180, 220, 250],
    'VR/AR Music Experiences': [0, 0, 0, 0, 10, 20, 30, 50, 70, 100, 120, 140, 180, 200],
}

# Extract data for easier access
daw_data = adoption_rates['DAW Adoption']
streaming_data = adoption_rates['Streaming Services']
ai_music_data = adoption_rates['AI Music Production']
vrar_data = adoption_rates['VR/AR Music Experiences']

daw_revenue = revenue_growth['DAW Adoption']
streaming_revenue = revenue_growth['Streaming Services']
ai_music_revenue = revenue_growth['AI Music Production']
vrar_revenue = revenue_growth['VR/AR Music Experiences']

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

# First Subplot: Technology Adoption Rates
ax1.plot(years, daw_data, label='Digital Audio Workstations', color='blue', marker='o', linewidth=2)
ax1.plot(years, streaming_data, label='Streaming Services', color='green', marker='s', linestyle='--', linewidth=2)
ax1.plot(years, ai_music_data, label='Artificial Intelligence in Music', color='red', marker='^', linewidth=2)
ax1.plot(years, vrar_data, label='Virtual Reality/Augmented Reality\nMusic Experiences', color='purple', marker='D', linewidth=2)

ax1.set_xlabel('Year')
ax1.set_ylabel('Adoption Rate (%)')
ax1.set_title('Trends in Technology Adoption for Music Production\nand Consumption (2010-2023)')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(title='Technology')

# Second Subplot: Technology Revenue Growth
ax2.bar(years, daw_revenue, width=0.8, label='Digital Audio Workstations', color='blue', alpha=0.7)
ax2.bar(years, streaming_revenue, width=0.8, label='Streaming Services', bottom=daw_revenue, color='green', alpha=0.7)
ax2.bar(years, ai_music_revenue, width=0.8, label='Artificial Intelligence in Music', bottom=[i+j for i,j in zip(daw_revenue, streaming_revenue)], color='red', alpha=0.7)
ax2.bar(years, vrar_revenue, width=0.8, label='VR/AR Music Experiences', bottom=[i+j+k for i,j,k in zip(daw_revenue, streaming_revenue, ai_music_revenue)], color='purple', alpha=0.7)

ax2.set_xlabel('Year')
ax2.set_ylabel('Revenue (in million $)')
ax2.set_title('Technology Revenue Growth in the Music Industry (2010-2023)')
ax2.legend(title='Technology')

# Adjust the layout to avoid overlapping labels
plt.tight_layout()

# Show plot
plt.show()