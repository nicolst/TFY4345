import rk4
import numpy as np


class DragCannon2DIsothermal(rk4.RK4Particle):
    y0 = 1.0E4
    b2_m = 4.0E-5

    def acc(self, coords: np.ndarray, vel: np.ndarray):
        rho_ratio = np.exp(-coords[1] / self.y0)
        direction = -np.sign(vel)
        if direction[0] > 0:
            print("ERROR")
            exit(1)
        v_squared = np.linalg.norm(vel) * vel

        gravity = np.array([0.0, -9.81])

        total_acc: np.ndarray = gravity + direction * rho_ratio * self.b2_m * v_squared

        return total_acc

    def rk4_done(self):
        return self.positions[-1][1] < 0


class DragCannon2DAdiabatic(rk4.RK4Particle):
    y0 = 1.0E4
    b2_m = 4.0E-5
    alpha = 2.5
    a = 6.5E-3
    T0 = 288

    def acc(self, coords: np.ndarray, vel: np.ndarray):
        rho_ratio = np.power(1 - self.a * coords[1] / self.T0, self.alpha)
        direction = -np.sign(vel)
        if direction[0] > 0:
            print("ERROR")
            exit(1)
        v_squared = np.linalg.norm(vel) * vel

        gravity = np.array([0, -9.81])

        total_force: np.ndarray = gravity + direction * rho_ratio * self.b2_m * v_squared

        return total_force

    def rk4_done(self):
        return self.positions[-1][1] < 0
