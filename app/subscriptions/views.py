from django.shortcuts import render
from rest_framework.views     import APIView
from rest_framework.response    import Response
from .serializers   import SubSerializer
from .models    import Subscription
from django.shortcuts   import get_object_or_404
from rest_framework     import status

# Create your views here.
# 구독 관련 REST API

# SubscriptionList
# api/v1/subscription
# [POST]: 구독 하기
class SubscriptionList(APIView):
    def post(self, request):
        user_data = request.data # json > object(Serializer)
        serializer = SubSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save(subscriber=request.user)

        return Response(serializer.data, 201)

# SubscriptionDetail
# api/v1/subscription/{user_id}
# [GET]: 특정 유저의 구독자 리스트 조회
# [DELETE]: 구독 취소
class SubscriptionDetail(APIView):
    def get(self, request, pk):
        subs = Subscription.objects.filter(subscribed_to=pk) # objects >> json
        serializer = SubSerializer(subs, many=True)
        
        return Response(serializer.data) # get의 경우 200이 자동으로 내려감

    # api/v1/sub/{pk}
    def delete(self, request, pk):
        sub = get_object_or_404(Subscription, pk=pk, subscriber=request.user)
        sub.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        # *arg, **kwargs
        # grg: 위치기반?
        # kwargs: 키워드 기반?