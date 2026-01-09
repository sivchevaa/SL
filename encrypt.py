import base64
from pathlib import Path

password = str(input("Enter password: "))

encoded_bytes = base64.b64encode(password.encode("utf-8"))
encoded_password = encoded_bytes.decode("utf-8")

Path("password.txt").write_text(encoded_password)
print(f"Encrypted: {encoded_password}")

encrypted_file = Path("password.txt").read_text()

decoded_bytes = base64.b64decode(encrypted_file.encode("utf-8"))
decrypted_password = decoded_bytes.decode("utf-8")

print(f"Decrypted: {decrypted_password}")