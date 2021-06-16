#!/usr/bin/env python
# encoding: utf-8

"""
@description: 多种加密算法

@author: baoqiang
@time: 2021/6/1 9:28 下午
"""
import hmac
import hashlib
import sys
from pyDes import des, CBC, PAD_PKCS5
import binascii
from Crypto.Cipher import AES
import base64

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
    pass


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
