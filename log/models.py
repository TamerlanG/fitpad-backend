from django.db import models
from common.models import BaseModel
from users.models import CustomUser


class Log(BaseModel):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE
    )


