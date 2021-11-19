#!/usr/bin/env python
# encoding: utf-8

"""
@description: 多种加密算法

@author: baoqiang
@time: 2021/6/1 9:28 下午
"""
import hmac
import hashlib
import os
import sys
from pyDes import des, CBC, PAD_PKCS5
import binascii
from Crypto.Cipher import AES
import base64
import rsa
from rsa import common

secret = b'a very secret hahaha'
des_secret = b'66668888'


def encrypt():
    """
    usage:
        python3 encrypt.py "that's it呀"
    :return:
    """
    s = sys.argv[1]

    digest(s)
    symmetric_enc(s)
    asymmetric_enc(s)


def digest(s):
    md5 = hashlib.md5()
    md5.update(s.encode())

    sha1 = hashlib.sha1()
    sha1.update(s.encode())

    mac = hmac.new(key=secret, msg=s.encode(), digestmod='sha256')

    print(f'data {s} md5 digest is {md5.hexdigest()}, len: {len(md5.hexdigest())}')  # 32
    print(f'data {s} sha1 digest is {sha1.hexdigest()}, len: {len(sha1.hexdigest())}')  # 40
    print(f'data {s} mac digest is {mac.hexdigest()}, len: {len(mac.hexdigest())}')  # 64


def symmetric_enc(s):
    des_encrypted = des_encrypt(des_secret, s.encode())
    des_decrypted = des_decrypt(des_secret, des_encrypted)

    aes_encrypted = aes_encrypt(str(secret), s)
    aes_decrypted = aes_decrypt(str(secret), aes_encrypted)

    print(f'data {s} des encrypted is {des_encrypted}, len: {len(des_encrypted)}')  # 32
    print(f'data {des_encrypted} des decrypted is {des_decrypted}')

    print(f'data {s} aes encrypted is {aes_encrypted}, len: {len(aes_encrypted)}')  # 32
    print(f'data {aes_encrypted} aes decrypted is {aes_decrypted}')


def asymmetric_enc(s):
    rsa_util = RsaUtil()
    rsa_encrypted = rsa_util.encrypt(s)
    rsa_decrypted = rsa_util.decrypt(rsa_encrypted)
    print(f'data {s} rsa encrypted is {rsa_encrypted}, len: {len(rsa_encrypted)}')  # 32
    print(f'data {rsa_encrypted} rsa decrypted is {rsa_decrypted}')

    sign = rsa_util.sign(s)
    verify = rsa_util.verify(s, sign)
    print(f'data {s} sign is {sign}, verify is {verify}')


# rsa class
class RsaUtil:
    PUB_KEY_PATH = os.environ['HOME'] + '/dev/test/pub_8.pem'
    PRI_KEY_PATH = os.environ['HOME'] + '/dev/test/private_1.pem'

    def __init__(self):
        self.pub_key = rsa.PublicKey.load_pkcs1_openssl_pem(open(self.PUB_KEY_PATH, 'rb').read())
        self.pri_key = rsa.PrivateKey.load_pkcs1(open(self.PRI_KEY_PATH, 'rb').read())

    def get_max_length(self, rsa_key, encrypt=True):
        blocksize = common.byte_size(rsa_key.n)
        reserve_size = 11
        if not encrypt:
            reserve_size = 0
        max_len = blocksize - reserve_size
        return max_len

    def encrypt(self, msg):
        result = b''
        max_len = self.get_max_length(self.pub_key)
        while msg:
            batch = msg[:max_len]
            output = rsa.encrypt(batch.encode(), self.pub_key)
            result += output
            # next one
            msg = msg[max_len:]
        return base64.b64encode(result)

    def decrypt(self, msg):
        result = b''
        max_len = self.get_max_length(self.pri_key, False)
        msg = base64.b64decode(msg)

        while msg:
            batch = msg[:max_len]
            output = rsa.decrypt(batch, self.pri_key)
            result += output
            # next one
            msg = msg[max_len:]
        return result.decode()

    def sign(self, data):
        signature = rsa.sign(data.encode(), priv_key=self.pri_key, hash_method='SHA-1')
        return base64.b64encode(signature)

    def verify(self, data, signature):
        signature = base64.b64decode(signature)
        return rsa.verify(data.encode(), signature, self.pub_key)


# helpers
def des_encrypt(secret_key, s):
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)
    # return en.hex()


def des_decrypt(secret_key, s):
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    # de = k.decrypt(bytes.fromhex(s), padmode=PAD_PKCS5)
    return de.decode()


def aes_encrypt(key, text):
    aes = AES.new(add_to_16(key), AES.MODE_ECB)  # 初始化加密器
    encrypt_aes = aes.encrypt(add_to_16(text))  # 先进行aes加密
    # print(encrypt_aes, type(encrypt_aes))
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
    return encrypted_text


def aes_decrypt(key, text):
    aes = AES.new(add_to_16(key), AES.MODE_ECB)  # 初始化加密器
    base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))  # 优先逆向解密base64成bytes
    decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')  # 执行解密密并转码返回str
    return decrypted_text


def add_to_16(value):
    bvalues = str.encode(value)
    while len(bvalues) % 16 != 0:
        bvalues += b'\0'
    return bvalues  # 返回bytes


if __name__ == '__main__':
    encrypt()
