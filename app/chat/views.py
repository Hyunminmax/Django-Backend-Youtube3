from django.shortcuts import render
from rest_framework.views import APIView
from .models import ChatRoom
from .serializers import ChatRoomSerializer, ChatMessageSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import ChatMessage
from django.shortcuts import get_object_or_404



def chat_html(request):
    return render(request, 'index.html') # html 만들어주는 역할


# ChatRoom
## (1) ChatRoomList
# api/v1/chat/room
### [GET]: 전체 채팅방 조회 // AUTH - request.user
### [POST]: 채팅방 생성

class ChatRoomList(APIView):
    def get(self, request):
        chatrooms = ChatRoom.objects.all() #objs > json (직렬화 필요)
        serializer = ChatRoomSerializer(chatrooms, many=True)

        return Response(serializer.data) # status = 200

    def post(self, request):
        user_data = request.data # 유저가 보내준 데이터
        serializer = ChatRoomSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) # 저장 성공
        return Response(serializer.errors) # 저장 실패





## ChatRoomDetail - 선택사항 -
# api/v1/chat/{room_id}
### [PUT]: 채팅방 관련 수정 ex) 방제목, 인원수 제한 등등
### [DELETE]: 해당 채팅방 삭제


# ChatMessage
## (1) ChatMessageList
# api/v1/chat/{room_id}/messages
### [GET]: 전체 채팅 내역 조회
### [POST]: 채팅 메세지 생성
class ChatMessageList(APIView):
    def get(self, request, room_id):
        chatroom = get_object_or_404(ChatRoom, id=room_id)
        messages = ChatMessage.objects.filter(room=chatroom) # room 객체로 조회
        
        # 직렬화
        serializer = ChatMessageSerializer(messages, many=True)

        return Response(serializer.data)

    def post(self, request, room_id):
        user_data = request.data # 유저가 보내준 데이터
        chatroom = get_object_or_404(ChatRoom, id=room_id)

        serializer = ChatMessageSerializer(data=user_data)

        serializer.is_valid(raise_exception=True)
        serializer.save(room=chatroom, sender=request.user)

        return Response(serializer.data, 201)
