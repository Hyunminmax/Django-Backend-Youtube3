from django.db import models
from common.models import CommonModel

# chatRoom 모델을 분리했을 때의 이점
# - 관리의 용이
# - 확장성(채팅방: 일반, 오픈, 업무-비밀번호입력해야만 입장가능)
class ChatRoom(CommonModel):
    name = models.CharField(max_length=100)

class ChatMessage(CommonModel):
    # 정보통신법 3개월 채팅 보관
    # Set_Null은 sender를 null 값으로 두겠다는 뜻. 유저1 > 계정삭제 > null
    sender = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True) # 삭제 된 경우 알수없음으로 세팅
    message = models.TextField()
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

    #User:Msg (1:N)  >> Msg(FK)
        # User: Msg, msg, msg, ...(o)
        # Msg: User, User, User ...(x)

    # Room:Msg (1:N)  >> Msg(FK)
        # Room: Msg, msg, msg, ...(o)
        # Msg: Room, Room, Room ...(x)

