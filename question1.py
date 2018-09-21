import cannons
import numpy as np
import matplotlib.pyplot as plt
import tools

# theta_rad = np.deg2rad(43.758)
# init_vel = 700.0 * np.array((np.cos(theta_rad), np.sin(theta_rad)))
# c = cannons.DragCannon2DAdiabatic(0.005, np.array((0.0, 0.0)), init_vel, 1.0)
# c.start()
# c.join()
# print(max([t[0] for t in c.positions]))

# Finding ideal angle for isothermal model
angles_deg = np.arange(0, 90, 0.1)
angles = np.deg2rad(angles_deg)  # Angles to check
time_step = 0.1
init_pos = np.array((0.0, 0.0))
projectiles = [cannons.DragCannon2DIsothermal(time_step,
                                              init_pos,
                                              700.0 * np.array((np.cos(theta), np.sin(theta))),
                                              1.0) for theta in angles]
[p.start() for p in projectiles]

distances_iso = []
for p in projectiles:
    p.join()
    distances_iso.append(tools.interpolate_zero(p.positions[-2], p.positions[-1])[0] / 1000.0)

print("Maximum distance was {0} at theta={1}".format(max(distances_iso), angles_deg[np.argmax(distances_iso)]))

plt.figure(1)
plt.title(r"Horizontal projectile distance for different angles")
plt.xlabel(r"$\theta$", size=20)
plt.ylabel(r"$x$ (km)", size=20)
plt.plot(angles_deg, distances_iso, color='k', linestyle='-', label='isothermic')
plt.xlim([min(angles_deg), max(angles_deg)])
plt.ylim([min(distances_iso), 1.1*max(distances_iso) - 0.1*min(distances_iso)])
# plt.grid(True)
# plt.tight_layout()
# plt.show()


# Finding ideal angle for adiabatic model
# angles_deg = np.arange(40, 50, 0.1)
# angles = np.deg2rad(angles_deg)  # Angles to check
# time_step = 0.1
init_pos = np.array((0.0, 0.0))
projectiles = [cannons.DragCannon2DAdiabatic(time_step,
                                             init_pos,
                                             700.0 * np.array((np.cos(theta), np.sin(theta))),
                                             1.0) for theta in angles]
[p.start() for p in projectiles]

distances_adi = []
for p in projectiles:
    p.join()
    distances_adi.append(tools.interpolate_zero(p.positions[-2], p.positions[-1])[0] / 1000.0)

print("Maximum distance was {0} at theta={1}".format(max(distances_adi), angles_deg[np.argmax(distances_adi)]))

# plt.figure(1)
# plt.title(r"Horizontal projectile distance for different angles")
# plt.xlabel(r"$\theta$", size=20)
# plt.ylabel(r"$x$ (km)", size=20)
plt.plot(angles_deg, distances_adi, color='k', linestyle='--', label='adiabatic')
# plt.xlim([min(angles_deg), max(angles_deg)])
# plt.ylim([min(distances_adi), 1.1*max(distances_adi) - 0.1*min(distances_adi)])
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()
