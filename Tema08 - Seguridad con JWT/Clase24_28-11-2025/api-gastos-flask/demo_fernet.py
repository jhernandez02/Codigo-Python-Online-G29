from cryptography.fernet import Fernet
#key = Fernet.generate_key()
key = 'E-uKaCAbWRBym0CT-Ul2Elg4vHjftE35cvuyHPqTDp0='
print("key:",key)
fernet = Fernet(key)
print(fernet)
token_encrypted = fernet.encrypt(b"demo@mail.com")
print("token:", token_encrypted)
token_decrypted = fernet.decrypt(token_encrypted)
print("token:", token_decrypted)