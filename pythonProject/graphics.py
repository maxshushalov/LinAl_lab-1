def project(point, width, height, camera, fov=300):
    x, y, z = point
    x -= camera[0]
    y -= camera[1]
    z -= camera[2]
    factor = fov / (z + 20)
    screen_x = x*factor
    screen_y = -y*factor
    screen_x = max(0, min(width - 1, width // 2 + int(screen_x)))
    screen_y = max(0, min(height - 1, height // 2 + int(screen_y)))
    return (screen_x, screen_y)


def fill_triangles(p1, p2, p3, color, canvas):
    sortedPoints = sorted([p1, p2, p3], key=lambda p: p[1])
    (x1, y1), (x2, y2), (x3, y3) = sortedPoints

    if y1 == y3 or (x1 == x2 and x2 == x3): # проверка на вырожденность
        return

    def edgeInterpolate(y_start, y_end, x_start, x_end):
        if y_start == y_end:
            return [(int(y_start), x_start)]
        x_values = []
        slope = (x_end - x_start) / (y_end - y_start)
        for y in range(int(y_start), int(y_end) + 1):
            x = x_start + slope * (y - y_start)
            x_values.append((y, x))
        return x_values

    leftEdge = edgeInterpolate(y1, y2, x1, x2) + edgeInterpolate(y2, y3, x2, x3)
    rightEdge = edgeInterpolate(y1, y3, x1, x3)

    minLen = min(len(leftEdge), len(rightEdge))
    leftEdge = leftEdge[:minLen]
    rightEdge = rightEdge[:minLen]

    for i in range(minLen):
        y = int(leftEdge[i][0])
        x_start = int(min(leftEdge[i][1], rightEdge[i][1]))
        x_end = int(max(leftEdge[i][1], rightEdge[i][1]))
        canvas.create_line(x_start, y, x_end, y, fill=color)


def draw_axes(canvas, width, height, camera):
    origin = project((0, 0, 0), width, height, camera)
    x_axis = project((5, 0, 0), width, height, camera)
    y_axis = project((0, 5, 0), width, height, camera)
    z_axis = project((0, 0, 5), width, height, camera)
    canvas.create_line(origin[0], origin[1], x_axis[0], x_axis[1], fill="red")
    canvas.create_line(origin[0], origin[1], y_axis[0], y_axis[1], fill="green")
    canvas.create_line(origin[0], origin[1], z_axis[0], z_axis[1], fill="blue")
