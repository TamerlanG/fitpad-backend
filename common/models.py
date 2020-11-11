from django.db import models
from users.models import CustomUser


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MuscleType(BaseModel):
    title = models.TextField()


class Exercise(BaseModel):
    title = models.TextField()
    muscle_type = models.OneToOneField(MuscleType, on_delete=models.CASCADE)


class CustomExercise(BaseModel):
    title = models.TextField()
    muscle_type = models.OneToOneField(MuscleType, on_delete=models.CASCADE)
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE
    )
