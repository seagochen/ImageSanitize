import numpy as np

def translate(points, dx, dy):
    """
    对坐标进行平移变换
    :param points: 输入的点坐标列表，格式为 [(x1, y1), (x2, y2), ...]
    :param dx: x方向平移的量
    :param dy: y方向平移的量
    :return: 平移后的坐标列表
    """
    translated_points = [(x + dx, y + dy) for x, y in points]
    return translated_points

def scale(points, sx, sy):
    """
    对坐标进行缩放变换
    :param points: 输入的点坐标列表，格式为 [(x1, y1), (x2, y2), ...]
    :param sx: x方向的缩放因子
    :param sy: y方向的缩放因子
    :return: 缩放后的坐标列表
    """
    scaled_points = [(x * sx, y * sy) for x, y in points]
    return scaled_points

def rotate(points, angle):
    """
    对坐标进行旋转变换
    :param points: 输入的点坐标列表，格式为 [(x1, y1), (x2, y2), ...]
    :param angle: 旋转角度，单位为弧度
    :return: 旋转后的坐标列表
    """
    cos_theta = np.cos(angle)
    sin_theta = np.sin(angle)
    rotated_points = [(x * cos_theta - y * sin_theta, x * sin_theta + y * cos_theta) for x, y in points]
    return rotated_points

def transform(points, dx=0, dy=0, sx=1, sy=1, angle=0):
    """
    对坐标进行平移、缩放和旋转的组合变换
    :param points: 输入的点坐标列表，格式为 [(x1, y1), (x2, y2), ...]
    :param dx: x方向平移的量
    :param dy: y方向平移的量
    :param sx: x方向的缩放因子
    :param sy: y方向的缩放因子
    :param angle: 旋转角度，单位为弧度
    :return: 变换后的坐标列表
    """
    # 先进行缩放
    points = scale(points, sx, sy)
    # 再进行旋转
    points = rotate(points, angle)
    # 最后进行平移
    points = translate(points, dx, dy)
    return points


if __name__ == '__main__':
    
    # 输入坐标点
    points = [(1, 1), (2, 2), (3, 3)]

    # 进行组合变换: 平移 (dx=1, dy=2), 缩放 (sx=2, sy=2), 旋转 (angle=np.pi / 4)
    transformed_points = transform(points, dx=1, dy=2, sx=2, sy=2, angle=np.pi / 4)

    # Output should be
    output = [(1.0000000000000002, 4.828427124746191), (1.0000000000000004, 7.6568542494923815), (1.0, 10.485281374238571)]

    # Assert
    assert np.allclose(transformed_points, output)
    print('Passed')