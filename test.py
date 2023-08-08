import json
from src.lib import message

if __name__ == '__main__':
    data = {
        'message': 
            { 
            'to': '01032523069',
            'from': '01032523069',
            'text': '테스트'
            } 
    }

    res = message.send_one(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
