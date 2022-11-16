"""File with class Ball."""
import math

turnaround = 360


class Ball:
    """Class finds angle after moves."""

    def __init__(self, speed=0, acceleration=0, radius=1, time=0):
        """Method which initialize class Ball.

        Args:
            speed: int, float - speed of the ball.
            acceleration: int, float - acceleration of the ball.
            radius: int, float - radius of the ball.
            time: int, float - rolling time.

        Raises:
            ValueError: Exception - if sides in allowed values.
        """
        self.speed = speed
        self.acceleration = acceleration
        self.radius = radius
        self.time = time
        if not self.check_instance():
            raise ValueError
        self.length_circle = 2 * self.radius * math.pi

    def find_angle_speed(self):
        """Method which finds deviation in degrees by speed.

        Returns:
            angle: float - angle in degrees.
        """
        path = self.speed * self.time
        return round((path % self.length_circle) / self.length_circle * turnaround, 2)

    def find_angle_acceleration(self):
        """Method which finds deviation in degrees by acceleration.

        Returns:
            angle: float - angle in degrees.
        """
        path = self.acceleration * self.time ** 2 / 2
        return round((path % self.length_circle) / self.length_circle * turnaround, 2)

    def check_instance(self):
        """Method which checks class parameters.

        Returns:
            flag: bool - if parameters is int and bigger than 0.
        """
        class_variables = [self.radius, self.acceleration, self.time, self.speed]
        return not isinstance(all(class_variables), (int, float)) or all(class_variables) < 0
# print(Ball(0, 55, 1.2, 9).find_angle_acceleration())
