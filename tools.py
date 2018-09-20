

def interpolate_zero(point_1, point_2):
    if point_1[1] * point_2[1] > 0:
        raise ValueError("Point 1 and 2 have the same sign")
    diff = point_2 - point_1
    intersect_point = point_1 + (point_1[1] / (point_1[1] - point_2[1])) * diff
    return intersect_point
