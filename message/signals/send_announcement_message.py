from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import AnnouncementMessage 
import json

from src.lib import message

@receiver(post_save, sender=AnnouncementMessage)
def send_announcement_message(sender, instance,created, **kwargs): 

    if created: 

        data = {
            'message': {
                'to': instance.unit.phone_number,
                'from': '16602606',
                'text': instance.message,
                'kakaoOptions': {
                'pfId': 'KA01PF220417023828732kAeE8jCxWjw',
                }
            } 
        }

        res = message.send_one(data)
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))
            
            
        

    

