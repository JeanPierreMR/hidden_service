import rsa

def read():
  try:
    with open("message.txt", "r") as f:
      x = len(f.readlines())
      f.close()
  except:
    with open("message.txt", "w+") as f:
      x = 0
      f.close()
  return x

def write(message):
  with open("message.txt", "wb") as f:
    if len(message) < 100:
        f.write(message)
    f.close()

def save_key(public_key, private_key):
    # Save the public_key
    with open("public_key.pem", "wb") as public_file:
        public_file.write(public_key.save_pkcs1())
 
    # Save the private_key
    with open("private_key.pem", "wb") as private_file:
        private_file.write(private_key.save_pkcs1())
 
def load_key():
    # Read the public_key
    with open("public_key.pem", "rb") as public_file:
        public_key = rsa.PublicKey.load_pkcs1(public_file.read())
 
    # Read the private_key
    with open("private_key.pem", "rb") as private_file:
        private_key = rsa.PrivateKey.load_pkcs1(private_file.read())
 
    return public_key, private_key