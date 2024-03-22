from django.db import models
from common.models import CommonModel
from django.db.models   import Count, Q

# Create your models here.
# User: FK
# Video: FK
# reaction(like, dislike, cancel)

class Reaction(CommonModel):
    # subscriber(내가 구독한 사람)
    # subscribed_to(나를 구독한 사람)
    # User:Subscription(FK) >> User: subscriber, subscriber, ... (o)
    # User:Subscription(FK) >> User: subscribed_to, subscribed_to, ... (o)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)

    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0

    REACTION_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
        (NO_REACTION, 'No Reaction')
    )

    reaction = models.IntegerField(
        choices=REACTION_CHOICES, 
        default=NO_REACTION
    )
    @staticmethod # ORM depth2 모델.objects.get, filter().aggregate() # SQL: Join Query
    def get_video_reaction(video):
        reactions = Reaction.objects.filter(video=video).aggregate(
            likes_count = Count('pk', filter=Q(reaction=Reaction.LIKE)), 
            dislikes_count = Count('pk', filter=Q(reaction=Reaction.DISLIKE)), 
        )

        return reactions
