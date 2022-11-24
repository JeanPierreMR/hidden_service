import rsa
import service_utils

publicKey, privateKey = service_utils.load_key()

def read():
    message = ''
    try:
        with open("message.txt", "rb") as f:
            message = rsa.decrypt(f.read(), privateKey)
            f.close()
    except Exception as e: 
        print(e)
        message = 'No messages'
    return message

print(read())