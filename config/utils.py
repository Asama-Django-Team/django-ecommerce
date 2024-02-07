# from sms_ir import SmsIr
from loguru import logger
from kavenegar import *

def send_opt_code(phone_number, code):
        
    try: 
        
        api = KavenegarAPI('')
        params = {
            'sender': '',
            'receptor' : str(phone_number),
            'message' : f" {code}"
        }   
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    
    except HTTPException as e:
        print(e)

