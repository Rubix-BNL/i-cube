from svgpathtools import svg2paths2
import numpy as np
import csv
import matplotlib.pyplot as plt

# Bestanden
svg_bestand = 'pad.svg'
csv_bestand = 'pad_coordinaten.csv'
step_size = 1.0  # Sampleafstand

# SVG uitlezen
paths, attributes, svg_attributes = svg2paths2(svg_bestand)

def sample_path(path, step):
    """Genereer (x, y)-punten op basis van een SVG-path-object"""
    length = path.length()
    num_points = max(int(length / step), 2)
    return [(p.real, p.imag) for p in [path.point(i / num_points) for i in range(num_points + 1)]]

# Verzamel alle punten
alle_punten = []

for path in paths:
    alle_punten.extend(sample_path(path, step_size))

# Schrijf naar CSV
with open(csv_bestand, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['X', 'Y'])
    for x, y in alle_punten:
        writer.writerow([f'{x:.3f}', f'{y:.3f}'])

print(f"{len(alle_punten)} punten opgeslagen in {csv_bestand}")

# Omzetten naar DataFrame om te plotten
import pandas as pd
df = pd.DataFrame(alle_punten, columns=['X', 'Y'])

# Y-as corrigeren (spiegelen)
df['Y_corrected'] = df['Y'].max() - df['Y']

# Plot
plt.figure(figsize=(8, 6))
plt.plot(df['X'], df['Y_corrected'], linestyle='-', marker='.', color='orange')
plt.title('Padcoördinaten uit SVG (correct georiënteerd)')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.grid(True)

# Controleer of we in een GUI-omgeving zijn of in een container
import os
if os.environ.get('MPLBACKEND') == 'Agg':
    # In container: sla de plot op als afbeelding
    plt.savefig('pad_visualisatie.png')
    print("Plot opgeslagen als 'pad_visualisatie.png'")
else:
    # Normale modus: toon het plot-venster
    plt.show()