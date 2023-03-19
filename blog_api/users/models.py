from django.db import models
from django.contrib.auth import get_user_model


class Subscription(models.Model):
    subscriber = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='subscriptions',
                                   verbose_name='subscriber')
    subscribed_to = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='subscribers',
                                      verbose_name='subscribed to')

    class Meta:
        db_table = 'subscriptions'



