import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Survey data
responses = {
    'Yes': 329,
    'No': 38  
}

# Calculate percentages
total = sum(responses.values())
percentages = {k: (v/total*100) for k, v in responses.items()}

# Create custom colormap - using a gradient from deep purple to vibrant blue
colors = ['#6A0DAD', '#4B0082', '#0000FF', '#1E90FF']
custom_cmap = LinearSegmentedColormap.from_list('magic_gradient', colors)

# Create the figure with a specific style
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10, 7), facecolor='#f8f8f8')
fig.suptitle('Magic School Classroom Usage Survey', fontsize=22, fontweight='bold', y=0.95)

# Create the pie chart with a gradient effect
wedges, texts, autotexts = ax.pie(
    responses.values(),
    labels=None,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'width': 0.6, 'edgecolor': 'white', 'linewidth': 2},
    pctdistance=0.8,
    colors=[custom_cmap(i/len(responses)) for i in range(len(responses))]
)

# Style the percentage text
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(14)
    autotext.set_fontweight('bold')

# Add a circle at the center to create a donut chart
circle = plt.Circle((0, 0), 0.3, fc='#f8f8f8')
ax.add_artist(circle)

# Add the title in the center
ax.text(0, 0, "Survey\nResults", ha='center', va='center', fontsize=16, fontweight='bold')

# Add an elegant legend
ax.legend(
    wedges,
    [f"{k} ({v}/{total})" for k, v in responses.items()],
    loc="center left",
    bbox_to_anchor=(0.9, 0, 0.5, 1),
    frameon=True,
    title="Responses",
    title_fontsize=14
)

# Add a note about the total responses
ax.text(
    -1.5, -1.2,
    f"Total Responses: {total}",
    fontsize=12,
    fontweight='bold'
)

# Add a subtle decorative element
theta = np.linspace(0, 2*np.pi, 100)
r = 0.9
x = r * np.cos(theta)
y = r * np.sin(theta)
ax.plot(x, y, color='#6A0DAD', alpha=0.3, linewidth=2)

plt.tight_layout()
plt.show()
