from typing import Optional, Union


class Keypair:
    def __init__(
        self,
        ss58_address: Optional[str] = None,
        public_key: Optional[Union[bytes, str]] = None,
        private_key: Optional[Union[bytes, str]] = None,
        ss58_format: int = 42,
        seed_hex: Optional[str] = None,
        crypto_type: int = 1,
    ) -> None: ...

    @staticmethod
    def generate_mnemonic(n_words: int = 12) -> str: ...

    @staticmethod
    def create_from_mnemonic(mnemonic: str) -> "Keypair": ...

    @staticmethod
    def create_from_seed(seed: Union[bytes, str]) -> "Keypair": ...

    @staticmethod
    def create_from_private_key(private_key: str) -> "Keypair": ...

    @staticmethod
    def create_from_encrypted_json(
            json_data: str, passphrase: str
    ) -> "Keypair": ...

    @staticmethod
    def create_from_uri(uri: str) -> "Keypair": ...

    def sign(self, data: Union[str, bytes]) -> bytes: ...

    def verify(
            self, data: Union[str, bytes], signature: Union[str, bytes]
    ) -> bool: ...

    @property
    def ss58_address(self) -> str: ...

    @property
    def public_key(self) -> Optional[bytes]: ...

    @property
    def ss58_format(self) -> int: ...

    @property
    def crypto_type(self) -> int: ...

    @crypto_type.setter
    def crypto_type(self, value: int) -> None: ...
