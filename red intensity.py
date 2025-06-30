import numpy as np
import cv2
import matplotlib.pyplot as plt

# === Chemins des trois images ===
image_paths = [
    r"D:\test stage\0maty.jpg",
    r"D:\test stage\1maty.jpg",
    r"D:\test stage\2maty.jpg"
]

# === Initialisation des histogrammes ===
histograms = []
bins = np.linspace(0, 256, 51)  # 50 intervalles

# === Calcul des histogrammes rouges normalisés ===
for path in image_paths:
    # Chargement de l'image
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Image non trouvée : {path}")

    # Extraction du canal rouge (OpenCV = BGR → Rouge = canal 2)
    red_channel = img[:, :, 2]

    # Calcul de l'histogramme
    hist, _ = np.histogram(red_channel, bins=50, range=(0, 256))
    hist = hist / hist.sum()  # Normalisation
    histograms.append(hist)

# === Affichage des histogrammes sur le même graphique ===
plt.figure(figsize=(10, 5))
labels = ['couloir sans souris', 'couloir avec une souris', 'couloir avec 2 souris']
colors = ['red', 'green', 'blue']

for hist, label, color in zip(histograms, labels, colors):
    plt.plot(bins[:-1], hist, label=label, color=color, marker='o')

plt.title("Histogrammes rouges normalisés")
plt.xlabel("Intensité rouge (0–255)")
plt.ylabel("Fréquence normalisée")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
