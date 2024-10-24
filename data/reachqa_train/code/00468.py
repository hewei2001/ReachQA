import matplotlib.pyplot as plt
import numpy as np

# Data representing publication years and number of copies sold for each author
authors = ["Author A", "Author B", "Author C", "Author D", "Author E"]
publication_years = {
    "Author A": [2000, 2003, 2006, 2010, 2015, 2020],
    "Author B": [2001, 2005, 2009, 2012, 2018, 2022],
    "Author C": [2002, 2006, 2011, 2014, 2017, 2021],
    "Author D": [2003, 2008, 2010, 2013, 2016, 2020],
    "Author E": [2004, 2007, 2011, 2015, 2019, 2022]
}

copies_sold = {
    "Author A": [30000, 45000, 50000, 60000, 70000, 75000],
    "Author B": [20000, 40000, 55000, 60000, 65000, 80000],
    "Author C": [25000, 30000, 45000, 55000, 60000, 68000],
    "Author D": [40000, 45000, 49000, 58000, 62000, 70000],
    "Author E": [35000, 42000, 52000, 60000, 64000, 72000]
}

# Color map for authors
colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FFD433']

# Create scatter plot
plt.figure(figsize=(14, 8))
for i, author in enumerate(authors):
    plt.scatter(publication_years[author], copies_sold[author], 
                label=author, color=colors[i], s=100, alpha=0.7, edgecolors='w', linewidth=1.5)

# Adding a trendline for all data combined
all_years = np.concatenate(list(publication_years.values()))
all_sales = np.concatenate(list(copies_sold.values()))
coef = np.polyfit(all_years, all_sales, 1)
poly1d_fn = np.poly1d(coef)
plt.plot(all_years, poly1d_fn(all_years), color='black', linestyle='--', linewidth=1, label='Overall Trendline')

# Title and labels
plt.title('Historical Fiction Book Sales\nAcross Popular Authors', fontsize=16, weight='bold', pad=20)
plt.xlabel('Publication Year', fontsize=12)
plt.ylabel('Number of Copies Sold', fontsize=12)
plt.xticks(np.arange(2000, 2023, 2))
plt.yticks(np.arange(20000, 100001, 10000))

# Adding a legend
plt.legend(title='Authors', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))

# Grid and layout adjustments
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.tight_layout()

# Show plot
plt.show()