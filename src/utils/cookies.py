from cryptography.fernet import Fernet
import json
import os

class CookieManager:
    def __init__(self, file_path):
        self.file_path = file_path
        # In a real application, the key should be stored securely and not regenerated each time.
        # For this project, we'll generate it on the fly. A .env file would be a good place for it.
        self.key = os.getenv("ENCRYPTION_KEY")
        if not self.key:
            self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def save(self, cookies):
        """Encrypts and saves cookies to a file."""
        if not cookies:
            return
        encrypted = self.cipher.encrypt(json.dumps(cookies).encode('utf-8'))
        with open(self.file_path, 'wb') as f:
            f.write(encrypted)

    def load(self):
        """Loads and decrypts cookies from a file."""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'rb') as f:
                encrypted = f.read()
            if not encrypted:
                return []
            decrypted = self.cipher.decrypt(encrypted).decode('utf-8')
            return json.loads(decrypted)
        return []
