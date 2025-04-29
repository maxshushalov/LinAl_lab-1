import math

def generationSpiralSurface(alpha, beta, u_steps, v_steps, u_max, v_max):  # альфа, бета, кол-во шагов, максимальное u и v
    points = []

    dv = v_max / v_steps
    du = u_max / u_steps

    for i in range(u_steps + 1):
        u = i * du
        row = []
        for j in range(v_steps + 1):
            v = j * dv
            x = (alpha + beta * math.cos(v)) * math.cos(u)
            y = (alpha + beta * math.cos(v)) * math.sin(u)
            z = beta * math.sin(v) + alpha * u
            row.append((x, y, z))
        points.append(row)
    return points


def create_triangle(points):
    triangles = []

    u_count = len(points)
    v_count = len(points[0])

    for i in range(u_count - 1):
        for j in range(v_count - 1):
            p1 = points[i][j]
            p2 = points[i + 1][j]
            p3 = points[i][j + 1]
            p4 = points[i + 1][j + 1]

            triangles.append((p1, p2, p3))
            triangles.append((p2, p4, p3))

    return triangles
