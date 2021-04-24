from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
url = 'https://thingspeak.com/channels/1104680/field/1.csv'
msg = input("Введите зашифрованное сообщение: ")
password_provided = input("Введите ключ : ")
password = password_provided.encode()
salt = b'salt_'
kdf = PBKDF2HMAC(
	algorithm=hashes.SHA256(),
	length=32,
	salt=salt,
	iterations=100000,
	backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))
f=Fernet(key)
print("\nЗашифрованное сообщение :\n"+msg)
msg=msg[2:-1]
msg=bytes(msg,'utf-8')
msg=f.decrypt(msg)
print("\nОригинальный текст сообщения: \n"+str(msg)[2:-1])
input("")