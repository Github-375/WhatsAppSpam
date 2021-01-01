from twilio.rest import Client 
import time
a = 0
b = 0

account_sid = 'ACe11931d530fc4442280a94edd9cc4a76' 
auth_token = '9f1d4db82f56a1678568b422ebb738aa' 
client = Client(account_sid, auth_token) 

while 1 == 1:
    if 8 >= a:
        message = client.messages.create( 
                              from_='whatsapp:+44 7480728290',  
                              body='Dies ist ein Spam',      
                              to='whatsapp:+4915232757549' 
                          ) 
 
        print(message.sid)
        a += 1
        b += 1
    else:
        time.sleep (15)
        a = 0
    
