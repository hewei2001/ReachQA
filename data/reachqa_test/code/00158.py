import matplotlib.pyplot as plt
import squarify

# Define planets and their primary languages with distribution percentages
planets_languages = {
    'Planet Xylon': ('Xylonic', 25),
    'Planet Veloria': ('Velorian', 15),
    'Planet Zorgon': ('Zorgonese', 10),
    'Planet Quara': ('Quaralian', 8),
    'Planet Fintar': ('Fintarian', 12),
    'Planet Hurmia': ('Hurmi', 5),
    'Planet Zentar': ('Zentarish', 10),
    'Planet Thalos': ('Thalorian', 5),
    'Planet Krella': ('Krellan', 10)
}

# Additional data for planet populations in billions
planet_populations = {
    'Planet Xylon': 1.2,
    'Planet Veloria': 0.8,
    'Planet Zorgon': 0.5,
    'Planet Quara': 0.3,
    'Planet Fintar': 0.9,
    'Planet Hurmia': 0.2,
    'Planet Zentar': 0.6,
    'Planet Thalos': 0.2,
    'Planet Krella': 0.5
}

# Extract languages and distribution data
languages = [f"{language}\n({planet})" for planet, (language, _) in planets_languages.items()]
distribution = [percentage for _, (_, percentage) in planets_languages.items()]

# Extract planet names and populations
planets = list(planet_populations.keys())
populations = list(planet_populations.values())

# Define colors for the plots
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2', '#f0b3ff', '#b3b3cc']

# Create figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(16, 8))

# Plotting the treemap
squarify.plot(ax=axs[0], sizes=distribution, label=languages, color=colors, alpha=0.8, edgecolor="white", linewidth=2)
axs[0].set_title('Interstellar Language Distribution\nAcross the Galaxy', fontsize=14, fontweight='bold')
axs[0].axis('off')

# Plotting the bar chart
axs[1].barh(planets, populations, color=colors, edgecolor='black')
axs[1].set_xlabel('Population (Billions)', fontsize=12)
axs[1].set_title('Planetary Population Size', fontsize=14, fontweight='bold')
axs[1].invert_yaxis()  # To match the order of languages on the treemap

# Improve layout
plt.tight_layout()

# Display the plots
plt.show()