import matplotlib.pyplot as plt

# Enhanced data representing global share of energy sources over the years
energy_sources = [
    'Coal', 'Natural Gas', 'Nuclear', 'Hydroelectric', 'Solar', 
    'Wind', 'Biomass & Others', 'Geothermal', 'Tidal'
]

# 2020-2023 data to show change over time, adding subcategories like offshore/onshore wind
energy_shares_2020 = [25, 22, 11, 12, 10, 10, 5, 3, 2]
energy_shares_2021 = [24, 23, 11, 12, 11, 11, 4, 3, 1]
energy_shares_2022 = [23, 22, 12, 11, 13, 12, 4, 2, 1]
energy_shares_2023 = [22, 21, 12, 10, 15, 13, 4, 2, 1]

# Distinct colors for each source and subcategory
colors = [
    '#444444', '#99CCFF', '#FFDD44', '#44AA44', '#FFDD88', 
    '#88CCAA', '#BB4444', '#6666CC', '#FFAAAA'
]

# Setting up subplots for time series comparison
fig, axes = plt.subplots(2, 2, figsize=(14, 12), subplot_kw=dict(aspect="equal"))
fig.suptitle("Global Energy Sources Distribution\nfrom 2020 to 2023", fontsize=18, weight='bold', ha='center')

years_data = {
    2020: energy_shares_2020,
    2021: energy_shares_2021,
    2022: energy_shares_2022,
    2023: energy_shares_2023
}

for ax, (year, shares) in zip(axes.flatten(), years_data.items()):
    explode = [0.1 if share == max(shares) else 0 for share in shares]
    wedges, texts, autotexts = ax.pie(
        shares, labels=energy_sources, autopct='%1.1f%%', 
        startangle=140, explode=explode, colors=colors, shadow=True,
        wedgeprops=dict(width=0.3), textprops=dict(color="black", size=8)
    )

    ax.set_title(f'{year}', fontsize=14, weight='bold')
    plt.setp(autotexts, size=8, weight="bold", color="darkblue")

# Adding legends outside the last subplot
axes[1, 1].legend(wedges, energy_sources, title="Energy Sources", loc="center left", bbox_to_anchor=(1.2, 0.5), fontsize=10)

# Ensuring equal aspect ratio for all charts
for ax in axes.flatten():
    ax.axis('equal')

# Automatic layout adjustment
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the chart
plt.show()