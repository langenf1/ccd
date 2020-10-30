import math
import numpy as np
from typing import List


def get_angle(vector1: list, vector2: list):
    unit_vector1 = vector1 / np.linalg.norm(vector1)
    unit_vector2 = vector2 / np.linalg.norm(vector2)

    dot_product = np.dot(unit_vector1, unit_vector2)
    angle = math.degrees(np.arccos(dot_product))

    return round(angle, 2)


def damping(p, r):
    diff = get_angle(p, r)
    if diff < 10:
        diff /= 1
    elif diff < 30:
        diff /= 2
    elif diff < 60:
        diff /= 3
    else:
        diff /= 4

    return diff


class Segment:
    def __init__(self, length: int, angle: int, mount_point=None):
        """ This class represents a segment of an arm.
        Args:
            length (int): Length of the arm.
            angle (int): Initial angle of the arm.
        """
        self.length = length
        self.angle = angle
        self.mount_point = mount_point
        self.end_x = self.end_y = self.end_z = 0
        self.max_angle = 150

    def get_prev_angle(self):
        if self.mount_point:
            prev_angle = self.mount_point.get_prev_angle()
            return self.angle + prev_angle
        else:
            return self.angle

    def calculate_endpoint(self):
        calculated_angle = self.angle
        if self.mount_point:
            prev_angle = self.mount_point.get_prev_angle()
            self.mount_point.calculate_endpoint()
            calculated_angle = self.angle + prev_angle

        delta_x = self.length * math.cos(math.radians(calculated_angle))
        delta_y = self.length * math.sin(math.radians(calculated_angle))
        self.end_x = self.mount_point.end_x + delta_x if self.mount_point else delta_x
        self.end_y = self.mount_point.end_y + delta_y if self.mount_point else delta_y

    def move_to_target(self, target_coords: List[float], arm_endpoint: List[float]):
        self.rotate(target_coords, arm_endpoint)

    def rotate(self, target_coords: List[float], arm_endpoint: List[float]):
        if self.mount_point:
            r = [target_coords[0] - self.mount_point.end_x,
                 target_coords[1] - self.mount_point.end_y,
                 target_coords[2] - self.mount_point.end_z]

            p = [arm_endpoint[0] - self.mount_point.end_x,
                 arm_endpoint[1] - self.mount_point.end_y,
                 arm_endpoint[2] - self.mount_point.end_z]
        else:
            r = target_coords
            p = arm_endpoint

        diff = damping(p, r)
        cross = np.cross(r, p)
        if cross[2] > 0:
            diff = -diff

        self.angle += diff

        if self.angle > self.max_angle:
            self.angle = self.max_angle

        if self.angle < -self.max_angle:
            self.angle = -self.max_angle

    def get_endpoint_location(self):
        return [round(self.end_x, 2), round(self.end_y, 2), round(self.end_z, 2)]
