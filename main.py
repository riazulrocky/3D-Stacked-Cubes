import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Cube generator
def create_cube_vertices(x, y, z, size=0.5):
    return np.array([
        [x, y, z, 1],
        [x + size, y, z, 1],
        [x + size, y + size, z, 1],
        [x, y + size, z, 1],
        [x, y, z + size, 1],
        [x + size, y, z + size, 1],
        [x + size, y + size, z + size, 1],
        [x, y + size, z + size, 1]
    ])

# Faces for cube
cube_faces = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [0, 1, 5, 4],
    [2, 3, 7, 6],
    [1, 2, 6, 5],
    [0, 3, 7, 4]
]

# Draw function
def draw_object(ax, components, faces, colors=None, alpha=0.9, edgecolor='black'):
    if colors is None:
        colors = ['#8B4513'] * len(components)
    for i, component in enumerate(components):
        for face in faces:
            square = [component[j][:3] for j in face]
            ax.add_collection3d(
                Poly3DCollection(
                    [square],
                    facecolors=colors[i],
                    linewidths=1,
                    edgecolors=edgecolor,
                    alpha=alpha
                )
            )

if __name__ == "__main__":
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Create 3 stacked cubes
    cube1 = create_cube_vertices(0, 0, 0, size=0.5)
    cube2 = create_cube_vertices(0, 0, 0.5, size=0.5)
    cube3 = create_cube_vertices(0, 0, 1.0, size=0.5)

    cubes = [cube1, cube2, cube3]
    cube_colors = ['red', 'green', 'blue']  # different colors for clarity

    draw_object(ax, cubes, cube_faces, colors=cube_colors, alpha=0.9)

    # Axes setup
    ax.set_xlim([-1, 2])
    ax.set_ylim([-1, 2])
    ax.set_zlim([0, 2])
    ax.view_init(elev=20, azim=-60)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3 Stacked Cubes - Computer Graphics')

    ax.grid(False)
    ax.set_box_aspect([1, 1, 1])
    plt.tight_layout()
    plt.show()
    fig.savefig("stacked_cubes.png", dpi=300)
