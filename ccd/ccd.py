import matplotlib.pyplot as plt
import math
import numpy as np
from typing import List
from ccd import Segment


def distance(coord1: List[float], coord2: List[float]):
    squared_dist = np.sum((np.array(coord1) - np.array(coord2))**2, axis=0)
    dist = np.sqrt(squared_dist)
    return dist


class CCD:
    def __init__(self, segments: List[Segment]):
        """ Main Cyclic Coordinate Descent implementation class
        Args:
            segments (list): List of arm segments to execute inverse kinematics on.
        """
        self.solved = False
        self.err_to_target = math.inf
        self.segments = segments
        self.max_iter = 100
        self.allowed_error = 0.02  # Allowed error distance to target coords

    def update_arm(self):
        for segment in self.segments:
            segment.calculate_endpoint()

    def move_to(self, target_coords: List[float]):
        loop = 0
        while loop < self.max_iter and not self.solved:
            for segment in self.segments:
                segment.move_to_target(target_coords, self.segments[-1].get_endpoint_location())
                self.update_arm()
                loop += 1
                self.err_to_target = self.get_error(target_coords)
                if self.err_to_target < self.allowed_error:
                    self.solved = True

    def plot_arm(self):
        fig = plt.figure()
        fig_ax = fig.add_subplot(1, 1, 1)

        fig.suptitle("Cyclic Coordinate Descent", fontsize=12)
        fig_ax.set_xlim(-30, 30)
        fig_ax.set_ylim(-30, 30)

        for i in range(len(self.segments)):
            start = self.segments[i].mount_point.get_endpoint_location() if self.segments[i].mount_point else (0, 0, 0)
            end = self.segments[i].get_endpoint_location()
            fig_ax.plot([start[0], end[0]], [start[1], end[1]], linewidth=4)

        plt.show()

    def get_error(self, target_coords: List[float]):
        return round(distance(self.segments[-1].get_endpoint_location(), target_coords), 3)
