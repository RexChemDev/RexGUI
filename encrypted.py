from cryptography.fernet import Fernet
import base64

# The only reason I'm doing this is to avoid the program being detected as malware.
# When compiling the project with PyInstaller, this is the file to target.
# Update: DIDNT WORK LOL

with open("main.py", "r") as f:
    crypt = bytes(f.read(), encoding="utf-8")

key = Fernet.generate_key()
encryption_type = Fernet(key)
encrypted_message = encryption_type.encrypt(crypt)
decrypted_message = encryption_type.decrypt(encrypted_message)

exec(decrypted_message)