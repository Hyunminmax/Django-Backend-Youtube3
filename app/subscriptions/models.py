from django.db import models
from common.models import CommonModel
from users.models import User


# Create your models here.
class Subscription(CommonModel):
    # subscriber(내가 구독한 사람)
    # subscribed_to(나를 구독한 사람)
    # User:Subscription(FK) >> User: subscriber, subscriber, ... (o)
    # User:Subscription(FK) >> User: subscribed_to, subscribed_to, ... (o)
    subscriber = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscriptions"
    )
    subscribed_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscribers"
    )

    # subscriber_set >> subscriptions (내가 구독한 사람)
    # subscribed_to_set >> subscribers (나를 구독한 사람)
