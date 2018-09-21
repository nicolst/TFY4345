import cannons
import numpy as np
import matplotlib.pyplot as plt
import tools

# Finding ideal angle for Big Bertha
angles_deg = np.arange(50, 60, 0.1)
angles = np.deg2rad(angles_deg)  # Angles to check
time_step = 0.01
init_pos = np.array((0.0, 0.0))
projectiles = [cannons.DragCannon2DAdiabatic(time_step,
                                             init_pos,
                                             1640.0 * np.array((np.cos(theta), np.sin(theta))),
                                             1.0) for theta in angles]
[p.start() for p in projectiles]

distances_adi = []
for p in projectiles:
    p.join()
    distances_adi.append(tools.interpolate_zero(p.positions[-2], p.positions[-1])[0] / 1000.0)

print("Maximum distance was {0} at theta={1}".format(max(distances_adi), angles_deg[np.argmax(distances_adi)]))

plt.figure(1)
plt.title(r"Horizontal projectile distance for different angles (Big Bertha)")
plt.xlabel(r"$\theta$", size=20)
plt.ylabel(r"$x$ (km)", size=20)
plt.plot(angles_deg, distances_adi, color='k', linestyle='--', label='adiabatic')
plt.xlim([min(angles_deg), max(angles_deg)])
plt.ylim([min(distances_adi), 1.1*max(distances_adi) - 0.1*min(distances_adi)])
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()
