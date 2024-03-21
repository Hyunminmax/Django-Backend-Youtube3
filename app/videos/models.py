from django.db import models
from common.models  import CommonModel
from users.models   import User


    # title
    # description
    # link
    # category
    # views_count
    # thumbnail
    # video_file
    # user: FK

class Video(CommonModel):
    # Create your models here.
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    link = models.URLField()
    category = models.CharField(max_length=20)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField() #s3 Bucket >> Save file >> URL >> Save URL
    video_file = models.FileField(upload_to='storage/') # 파일저장 방법 교육용!
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
        
# User:Video >> User : Videos (o) 1:N
# Video:User >> Video : Users (x) 
    
    # docker-compose run --rm app sh -c 'python manage.py makemigrations'
    # docker-compose run --rm app sh -c 'python manage.py migrate'
    # makemigrations (장고한테 알려주는 것)
    # migrate(장고가 DB 찾아가는 것)