from django.db import models
from common.models  import CommonModel
from users.models   import User
from videos.models  import Video

# Create your models here.
# User : FK
# Video : FK
# content
# like
# dislike

class Comment(CommonModel):
# Create your models here.
# User : FK
# Video : FK
# content
# like
# dislike
    content = models.TextField()
    like = models.PositiveIntegerField(default = 0)
    dislike = models.PositiveIntegerField(default = 0)
    
    # User:comment >> 1:N
    # User >> Comment, Comment, Comment, ... (O)
    # Comment >> USer, User (X)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Video:comment >> 1:N
    # Video >> Comment, Comment, Comment, ... (O)
    # Comment >> Video(이지금), Video(돈깡), ... (X)

    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    # 법에의해서 일정기간 보관해야 하는 경우도 있음.

    # 모델 수정후 
    # docker-compose run --rm app sh -c 'python manage.py makemigrations'
    # docker-compose run --rm app sh -c 'python manage.py migrate'