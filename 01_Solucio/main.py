import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
from sklearn.datasets import make_classification
from Perceptron import Perceptron

# Generació del conjunt de mostres
X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, n_repeated=0,
                           n_classes=2, n_clusters_per_class=1, class_sep=1.25,
                           random_state=0)

y[y == 0] = -1  # La nostra implementació esta pensada per tenir les classes 1 i -1.

# Entrenament
perceptron = Perceptron(eta=0.001, n_iter=200)
perceptron.fit(X, y)
y_prediction = perceptron.predict(X)

#  Mostram els resultats
plt.figure(1)
# Dibuixem el núvol de punts (el paràmetre c indica que pintem segons la classe)
plt.scatter(X[:, 0], X[:, 1], c=y)

# Dibuixem la recta. Usem l'equació punt-pendent
m = -perceptron.w_[1] / perceptron.w_[2]
origen = (0, -perceptron.w_[0] / perceptron.w_[2])
plt.axline(xy1=origen, slope=m)


# Extra: Dibuixam el nombre d'errors en cada iteracio de l'algorisme
plt.figure(2)
plt.plot(perceptron.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of miss classifications')
plt.show()

# Create animated GIF of perceptron learning
fig, ax = plt.subplots(figsize=(10, 8))
writer = PillowWriter(fps=1)

# Get data bounds for consistent axis limits
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

# with writer.saving(fig, "perceptron_learning.gif", 100):
#     for epoch, weights in enumerate(perceptron.w_history_):
#         ax.clear()
        
#         # Plot data points
#         ax.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', s=50, alpha=0.8)
        
#         # Draw decision boundary if weights are not zero
#         if weights[1] != 0 or weights[2] != 0:
#             # Calculate line parameters
#             if abs(weights[2]) > 1e-10:  # Avoid division by zero
#                 m = -weights[1] / weights[2]
#                 origen = (0, -weights[0] / weights[2])
                
#                 # Calculate line endpoints within plot bounds
#                 x_line = np.array([x_min, x_max])
#                 y_line = m * x_line + origen[1]
                
#                 # Plot the line
#                 ax.plot(x_line, y_line, 'g-', linewidth=2, label=f'Decision boundary')
        
#         ax.set_xlim(x_min, x_max)
#         ax.set_ylim(y_min, y_max)
#         ax.set_title(f'Perceptron Learning - Epoch {epoch + 1}\nErrors: {perceptron.errors_[epoch]}')
#         ax.set_xlabel('Feature 1')
#         ax.set_ylabel('Feature 2')
#         ax.grid(True, alpha=0.3)
#         ax.legend()
        
#         writer.grab_frame()

# plt.close(fig)
# print("GIF created: perceptron_learning.gif")

