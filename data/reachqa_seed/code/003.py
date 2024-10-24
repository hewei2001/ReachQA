import matplotlib.pyplot as plt
import numpy as np

people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
performance = [8, 6, 9, 7, 5]
error = [0.5, 0.4, 0.3, 0.6, 0.2]

y_pos = np.arange(len(people))

fig, ax = plt.subplots()

hbars = ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

# Label with specially formatted floats
ax.bar_label(hbars, fmt='%.2f')
ax.set_xlim(right=10)  # adjust xlim to fit labels

plt.show()
