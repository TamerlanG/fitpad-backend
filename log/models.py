from django.db import models
from common.models import BaseModel
from users.models import CustomUser
from workout.models import Workout


class Log(BaseModel):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE
    )
    workouts = models.ManyToManyField(Workout)


