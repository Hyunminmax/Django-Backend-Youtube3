from django.test import TestCase
from rest_framework.test    import APITestCase
from users.models   import User
from django.urls    import reverse
from .models    import Subscription

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
        # user1이  user2를 구독
        Subscription.objects.create(subscriber=self.user1, subscribed_to=self.user2)
        url = reverse('sub-detail', kwargs={'pk': self.user2.pk})
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data), 1) # 2번 유저를 구독한 구독자 수가 1이면 ok

    # 구독 취소
    def test_sub_detail_delete(self):
        sub = Subscription.objects.create(subscriber=self.user1, subscribed_to=self.user2)
        url = reverse('sub-detail', kwargs={'pk':sub.id})

        res = self.client.delete(url)
        self.assertEqual(res.status_code, 204) #204: No Centent
        self.assertEqual(Subscription.objects.count(), 0)

        