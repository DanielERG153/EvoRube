from .face_score import FaceColourScore
_REG={'face_colour_sqsum':FaceColourScore()}
get_fitness=lambda n='face_colour_sqsum':_REG[n]