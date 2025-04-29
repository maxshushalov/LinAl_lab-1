
def subtract (a,b):
    return (b[0]-a[0], b[1]-a[1], b[2]-a[2])

def cross (u,v):
    return (
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v [0]
    )

def dot (u,v):
    return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]

def isVisible(triangle, camera):
    a, b, c = triangle
    ab = subtract(a, b)
    ac = subtract(a, c)
    normal = cross (ab, ac)
    to_camera = subtract(camera, a)
    return dot(normal, to_camera) > 0
