class Hash():
    @staticmethod
    def hash_password(password: str) -> str:
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(stored_password_hash: str, provided_password: str) -> bool:
        return stored_password_hash == Hash.hash_password(provided_password)