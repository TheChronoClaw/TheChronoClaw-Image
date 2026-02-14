import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch

fig, ax = plt.subplots(figsize=(7, 9), facecolor='black')
ax.set_aspect('equal')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.5, 1.2)
ax.axis('off')

gradient = np.linspace(0, 1, 256).reshape(1, -1)
gradient = np.vstack((gradient, gradient))
ax.imshow(np.flipud(gradient), extent=[-1.2,1.2,-1.5,1.2], cmap='Blues_r', alpha=0.4, zorder=0)

cape = FancyBboxPatch((-0.9, -1.4), 1.8, 2.0, boxstyle="round,pad=0.1", 
                      fc='#4B0082', ec='purple', alpha=0.7, zorder=1)
ax.add_patch(cape)

body = Rectangle((-0.45, -0.9), 0.9, 1.4, fc='black', ec='gray', lw=1.5, zorder=2)
ax.add_patch(body)

choker = Rectangle((-0.35, 0.25), 0.7, 0.12, fc='#111111', ec='silver', lw=2, zorder=3)
ax.add_patch(choker)
ax.add_patch(Circle((0, 0.31), 0.09, fc='silver', ec='white', zorder=4))

face = Circle((0, 0.55), 0.35, fc='#f0e8d9', ec='none', zorder=5)
ax.add_patch(face)

ax.add_patch(Circle((-0.12, 0.62), 0.08, fc='#00b7eb', ec='white', lw=1.5, zorder=6))
ax.add_patch(Circle(( 0.12, 0.62), 0.08, fc='#00b7eb', ec='white', lw=1.5, zorder=6))
ax.scatter([-0.10, 0.14], [0.64, 0.64], s=30, c='white', zorder=7)

hair_x = np.linspace(-0.4, 0.4, 100)
hair_y = 0.55 + 0.35 * np.sin(hair_x * 8) * np.exp(-hair_x**2 * 5)
ax.plot(hair_x, hair_y + 0.35, c='silver', lw=8, alpha=0.9, zorder=4)
ax.plot([0.05, 0.05, 0.4], [0.9, 0.4, -0.3], c='silver', lw=10, alpha=0.8, zorder=3)

theta = np.linspace(0, 20*np.pi, 2000)
r = 0.02 + 0.0008*theta
x = r * np.cos(theta) * 1.1
y = r * np.sin(theta) * 0.9 - 0.1
ax.plot(x, y, c='#00ffff', lw=0.8, alpha=0.7, zorder=10)

np.random.seed(42)
for _ in range(18):
    cx = np.random.uniform(-1.1, 1.1)
    cy = np.random.uniform(-0.8, 1.0)
    size = np.random.uniform(0.03, 0.10)
    alpha = np.random.uniform(0.4, 0.9)
    color = np.random.choice(['cyan', '#00bfff', '#7df9ff'])
    ax.add_patch(Rectangle((cx-size/2, cy-size/2), size, size, 
                          fc=color, ec='white', lw=0.8, alpha=alpha, zorder=12))
  
    ax.scatter(cx, cy, s=40, c='white', alpha=0.6, zorder=13)

plt.tight_layout(pad=0)
plt.show()
