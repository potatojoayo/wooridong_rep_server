from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import RepVerificationMessage 
import json

from src.lib import message

@receiver(post_save, sender=RepVerificationMessage)
def send_rep_verification_message(sender, instance,created, **kwargs):

    if created:

        if isinstance(instance, RepVerificationMessage):

            data = {
                'message': {
                    'to': instance.unit.phone_number,
                    'from': '16602606',
                    'kakaoOptions': {
                    'pfId': 'KA01PF220417023828732kAeE8jCxWjw',
                    'templateId': 'KA01TP220417024646290bKYbR7vv269',
                    # 변수: 값 형식으로 모든 변수에 대한 변수값 입력
                    'variables': {
                        '#{건물이름}': instance.unit.villa.name,
                        '#{동대표이름}': instance.rep.name,
                        '#{동대표id}': instance.rep.id,
                        '#{호id}': instance.unit.id
                    }
                    }
                } 
            }

            res = message.send_one(data)
            print(json.dumps(res.json(), indent=2, ensure_ascii=False))
            
            
            
        

    

