import string
import smtplib
import random
import urllib.request
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#Генератор ключей
def key_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

msg=str(input('Введите сообщение : '))
mail = str(input('Введите почту получателя : '))
password_provided = key_generator()

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
urllib.request.urlopen
msg=msg.encode()
f = Fernet(key)
msg=f.encrypt(msg)
msg=str(msg)
print("\nВаш зашифрованный текст: "+msg)

#SMTP
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#Почта, созданная для ВездеКода. Именнно с нее будут отправляться сообщения
server.login("ExampleVezdehod@gmail.com", "VezdehodTula71")
#Отправка
server.sendmail("ExampleVezdehod@gmail.com", mail, msg)

print("\nСообщение было отправлено!\nПолучателю необходим ключ для расшифровки: " +password_provided)
input("")