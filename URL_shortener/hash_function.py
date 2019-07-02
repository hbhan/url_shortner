#!/usr/bin/env python


__author__ = "Husain Bhanpurawala"
__email__ = "husibhan@gmail.com"

''' USING MD5 HASHING FUNCTION TO CREATE A HASH FOR THE URL.
    ENCODES IN BASE64. '''

import base64
import hashlib
import random
import string


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def hash_function(url, size_url=4):
    url = url + id_generator()
    shorter = base64.b64encode(hashlib.new('MD5', url).digest()[-size_url:])
    sanitized = shorter.replace('=', '').replace('/', '_')
    return sanitized
