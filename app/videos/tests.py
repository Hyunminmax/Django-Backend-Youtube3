# video REST API 관련 테스트
from rest_framework.test    import APITestCase
from users.models   import User
from .models    import Video
from django.urls    import reverse
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
import pdb #python debugger

# 테스트별로 클래스를 만들면 환경 설정에 오래 걸리고 테스트 값이 달라 결과가 다를수도 있다.
class VideoAPITestCase(APITestCase):
    # 테스트 코드가 실행되기 전 동작하는 함수
    #  - 데이터를 만들어줘야함.
    #     1. 유저 생성/로그인
    #     2. 비디오 생성
    def setUp(self):
        # ORM방식으로 유저 생성
        self.user = User.objects.create_user(
            email='abc@abc.com',
            password='passpass123'
        )
        self.client.login(email='abc@abc.com', password='passpass123')

        self.video = Video.objects.create(
            title = 'test video',
            link = 'https://www.test.com',
            user=self.user
        )

    # 전체 비디오 조회
    # 127.0.0.1:8000/api/v1/video [GET]
    def test_video_list_get(self):
        # url = 'http://127.0.0.1:8000/api/v1/video'
        url = reverse('video-list')
        res = self.client.get(url) # 전체 비디오 조회 데이터
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.headers['Content-Type'], 'application/json')
        self.assertTrue(len(res.data)>0)
        
        
        # title 컬럼이 응답 데이터에 잘 들어있는지 확인
        for video in res.data:
            self.assertIn('title', video)

    # 비디오 생성
    def test_video_list_post(self):
        url = reverse('video-list') # api/v1/video

        data = {
            'title':'test video2',
            'link':'http://test.com',
            'category':'test category',
            'thumbnail':'http://test.com',
            'video_file': SimpleUploadedFile('file.mp4', b'file_content', 'video/mp4'),
            'user': self.user.pk
        }

        res = self.client.post(url, data)
        # pdb.set_trace() # python debugger 이 문장위까지 확인 가능
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['title'], 'test video2')
    
    # 특정 비디오 조회
    def test_video_Detail_get(self):
        # url: api/v1/video/1
        url = reverse('video-detail', kwargs={'pk':self.video.pk})

        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    
    # 특정 비디오 업데이트
    def test_video_Detail_put(self):
        url = reverse('video-detail', kwargs={'pk':self.video.pk})
    
        data = {
            'title':'updated video',
            'link':'http://test.com',
            'category':'test category',
            'thumbnail':'http://test.com',
            'video_file': SimpleUploadedFile('file.mp4', b'file_content', 'video/mp4'),
            'user': self.user.pk
        }

        res = self.client.put(url, data)
        # pdb.set_trace()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['title'], 'updated video')#Json 형식으로 data있음.

    # 특정 비디오 삭제
    def test_video_Detail_delete(self):
        
        url = reverse('video-detail', kwargs={'pk':self.video.pk})

        res = self.client.delete(url)#[DELETE] api/v1/video/{pk}  >> REST API
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

        #docker-compose run --rm app sh -c 'python manage.py test videos'

