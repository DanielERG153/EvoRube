from .base import Fitness
class FaceColourScore(Fitness):
    name='face_colour_sqsum'
    def evaluate(self,cube):
        a=cube.state.reshape(6,9)
        c=((a==a[:,[0]]).sum(1))
        return int((c**2).sum())