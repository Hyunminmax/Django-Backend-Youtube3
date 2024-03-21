from django.test import TestCase
from rest_framework.test    import APITestCase
from users.models   import User
from django.urls    import reverse

# Create your tests here.
class SubscriptionTestCase(APITestCase):
    # 테스트 코드 실행시 가장 먼저 실행되는 함수
    # 데이터 생성
    # 2명의 유저 데이터 생성, 1명의 유저 로그인
    def setUp(self):
        # ORM방식으로 유저 생성
        self.user1 = User.objects.create_user(email='abc@abc.com',password='passpass123')
        self.user2 = User.objects.create_user(email='def@abc.com',password='passpass123')
        
        self.client.login(email='abc@abc.com', password='passpass123')

    # 구독 버튼 테스트
    # [POST] api/v1/sub
    def test_sub_list_post(self):
        url = reverse('sub-list')
        # Subscriptions 모델 데이터
        data = {
            'subscriber'    : self.user1.pk,
            'subscribed_to' : self.user2.pk

        }

        res = self.client.post(url, data)

        self.assertEqual(res.status_code, 201)# 201: CREATED
        from .models    import Subscription
        self.assertEqual(Subscription.objects.get().subscribed_to, self.user2)
        self.assertEqual(Subscription.objects.count(), 1)

    # 특정 유저의 구독자 리스트
    # [GET] api/v1/sub/{user_id}
    def test_sub_detail_get(self):
        pass

    # 구독 취소
    def test_sub_detail_delete(self):
        pass