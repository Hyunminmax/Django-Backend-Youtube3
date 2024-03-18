from django.test import TestCase
from django.contrib.auth    import get_user_model

# Create your tests here.
# TDD (User 관련 테스트 코드)

class UserTestCase(TestCase):
    # 슈퍼 유저 생성 테스트
    def test_create_superuser(self):
        email = 'hyunmin.etc@gmail.com'
        password = 'its_secret.'

        user = get_user_model().objects.create_superuser(
            email=email,
            password = password
        )
        # 슈퍼유저
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


    
    # 일반 유저 생성 테스트
    def test_create_user(self):
        email = 'hyunmin.shin81@gmail.com'
        password = 'its_secret.'

        user = get_user_model().objects.create_user(email=email, password=password)
        
        # 유저가 정상적으로 잘 만들어졌는지 확인
        self.assertEqual(user.email, email)
        # 아래 두 방식으로 패스워드확인
        # self.assertEqual(user.check_password(password), True)
        self.assertTrue(user.check_password(password))
        # 아래 두 방식으로 슈퍼유저 확인
        # self.assertEqual(user.is_superuser, False)
        self.assertFalse(user.is_superuser)

    
    # docker-compose run --rm app sh -c 'python manage.py test users'