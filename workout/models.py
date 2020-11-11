from django.db import models
from common.models import BaseModel, Exercise
from users.models import CustomUser


class Workout(BaseModel):
    time_taken = models.IntegerField()
    comment = models.TextField()


class Set(BaseModel):
    rep = models.IntegerField()
    weight = models.IntegerField()


class Routine(BaseModel):
    workout = models.OneToOneField(Workout, on_delete=models.CASCADE)
    exercise = models.OneToOneField(Exercise, on_delete=models.CASCADE)
    sets = models.ManyToManyField(Set)
