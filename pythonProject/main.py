from tkinter import Tk, Canvas
from surface import generationSpiralSurface, create_triangle
from geometry import isVisible
from graphics import project, fill_triangles, draw_axes
from math import pi


def main():
    width, height = 800, 600
    root = Tk()
    root.title("Spiral Surface")
    canvas = Canvas(root, width=width, height=height, bg='white')
    canvas.pack()

    alpha = 3.0
    beta = 1.0
    u_steps = 50
    v_steps = 30
    u_max = 4 * pi
    v_max = 2 * pi

    points = generationSpiralSurface(alpha, beta, u_steps, v_steps, u_max, v_max)

    triangles = create_triangle(points)

    camera = (4,4,12)

    canvas.delete("all")
    draw_axes(canvas, width, height, camera)

    sorted_triangles = []
    for tri in triangles:
        z_avg = (tri[0][2]+tri[1][2]+tri[2][2])/3
        sorted_triangles.append((z_avg, tri))
    sorted_triangles.sort(reverse = True)
    for z,triang in sorted_triangles:
        if isVisible(triang, camera):
            p1 = project(triang[0], width, height, camera)
            p2 = project(triang[1], width, height, camera)
            p3 = project(triang[2], width, height, camera)

            fill_triangles(p1, p2, p3, 'skyblue', canvas)

    root.mainloop()


if __name__ == '__main__':
    main()