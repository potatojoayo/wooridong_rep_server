from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import UserVerificationMessage 

import json

from src.lib import message

@receiver(post_save, sender=UserVerificationMessage)
def send_user_verification_message(sender, instance,created, **kwargs):

    if created:

        if isinstance(instance, UserVerificationMessage): 
            data = {
                'message': {
                    'to': instance.phone_number,
                    'from': '16602606',
                    'kakaoOptions': {
                    'pfId': 'KA01PF220417023828732kAeE8jCxWjw',
                    'templateId': 'KA01TP220417024259229pJxVzkuQ2UI',
                    # 변수: 값 형식으로 모든 변수에 대한 변수값 입력
                    'variables': {
                        '#{인증번호}': instance.code,
                    }
                    }
                } 
            } 
            res = message.send_one(data)
            print(json.dumps(res.json(), indent=2, ensure_ascii=False))
            
            
            
        

    

