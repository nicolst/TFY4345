import numpy as np
import threading


# RK4 algorithm for a particle
class RK4Particle(threading.Thread):
    def __init__(self, step_size: float, init_pos: np.ndarray, init_vel: np.ndarray, mass: float):
        self.step_size = step_size
        self.positions = [init_pos]
        self.velocities = [init_vel]
        self.mass = mass

        threading.Thread.__init__(self)

    # Start method if used as a Thread
    def run(self):
        i = 1
        while not self.rk4_done():
            # print("{0}: Step {1}".format(self.getName(), i))
            i += 1

            self.step()

        print("{0}: Done".format(self.getName()))

    # Acceleration at position
    def acc(self, coords: np.ndarray, vel: np.ndarray) -> np.ndarray:
        raise NotImplementedError()

    # Current velocity
    def vel(self) -> np.ndarray:
        return self.velocities[-1]

    # Current position
    def pos(self) -> np.ndarray:
        return self.positions[-1]

    # Stopping condition
    def rk4_done(self) -> bool:
        raise NotImplementedError()

    # One step of RK4 algorithm, general implementation
    # Can provide custom step size for adaptive methods
    def step(self, step_size=None):
        pos = self.pos()
        vel = self.vel()

        # If custom step size is not provided, use the value given at class init
        if step_size is None:
            step_size = self.step_size

        # k variables for velocity and position
        k1_v = self.acc(pos, vel)
        k1_r = vel

        k2_v = self.acc(pos + (step_size / 2) * k1_r, k1_r)
        k2_r = vel + (step_size / 2) * k1_v

        k3_v = self.acc(pos + (step_size / 2) * k2_r, k2_r)
        k3_r = vel + (step_size / 2) * k2_v

        k4_v = self.acc(pos + step_size * k3_r, k3_r)
        k4_r = vel + step_size * k3_v

        # New position and velocity
        vel_n = vel + (step_size / 6) * (k1_v + 2 * (k2_v + k3_v) + k4_v)
        pos_n = pos + (step_size / 6) * (k1_r + 2 * (k2_r + k3_r) + k4_r)

        self.velocities.append(vel_n)
        self.positions.append(pos_n)
