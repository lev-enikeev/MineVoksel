from ursina import *
import numpy as np

number_of_particles = 10   # keep this as low as possible
points = np.array([Vec3(0,1,0) for i in range(number_of_particles)])
directions = np.array([Vec3(random.random()-.5,.2,random.random()-.5)*.05 for i in range(number_of_particles)])
frames = []

# simulate the particles once and cache the positions in a list.
for i in range(60*1):
    points += directions
    frames.append(copy(points))


class ParticleSystem(Entity):
    def __init__(self, **kwargs):
        super().__init__(model=Mesh(vertices=points, mode='point', static=False, render_points_in_3d=True, thickness=.052), t=0, duration=.5, **kwargs)

        for key, value in kwargs.items():
            setattr(self, key, value)


    def update(self):
        self.t += time.dt
        if self.t >= self.duration:
            destroy(self)
            return

        self.model.vertices = frames[floor(self.t * 60)]
        self.model.generate()
