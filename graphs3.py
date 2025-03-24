import matplotlib.pyplot as plt
import numpy as np

# Data
classes = ['English', 'Science', 'Math', 'World Language', 
           'Social Studies/Humanities', 'Art', 'Technology', 'Health']
percentages = [73.7, 52.5, 8.4, 35.5, 54.5, 16.4, 11.5, 1.4]

# Set up the plot with a professional style
plt.figure(figsize=(10, 6))
plt.style.use('seaborn-v0_8-whitegrid')

# Create horizontal bar chart
bars = plt.barh(classes, percentages, color='#3498db', edgecolor='black')

# Add percentage labels to the end of each bar
for bar in bars:
    width = bar.get_width()
    plt.text(width + 1, bar.get_y() + bar.get_height()/2, f'{width:.1f}%', 
             ha='left', va='center', fontweight='bold')

# Customize the plot
plt.title('Percentage of Students Using MagicSchool AI by Class', 
          fontsize=15, fontweight='bold')
plt.xlabel('Percentage of Students', fontsize=12)
plt.xlim(0, 80)  # Set x-axis limit

# Tight layout to prevent cutting off labels
plt.tight_layout()

# Show the plot
plt.show()
