import json
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

def encrypt(text, key, iv):
    # Pad the key to make it the correct length
    padded_key = key.ljust(16, '\0')
    cipher = AES.new(padded_key.encode(), AES.MODE_CTR, initial_value=iv, nonce=b'')
    encrypted_bytes = cipher.encrypt(text.encode())
    return b64encode(encrypted_bytes).decode()




def decrypt(encrypted_text, key, iv):
    # Pad the key to make it the correct length
    padded_key = key.ljust(16, '\0')
    cipher = AES.new(padded_key.encode(), AES.MODE_CTR, initial_value=iv, nonce=b'')
    decrypted_bytes = cipher.decrypt(b64decode(encrypted_text))
    return decrypted_bytes.decode()




def __main__():
    text = '{"a": ["apple"], "b": "banana", "c": "cherry"}'
    key  = "py01"
    iv   = b"1234123412341234"

    encrypted_text = encrypt(text, key, iv)
    print("encrypted_text:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, key, iv)
    print("decrypted_text:", decrypted_text)


    label_dict = json.loads(decrypted_text)
    print("json dictionary:", label_dict)
    print("json dictionary keys:", label_dict.keys())



if __name__ == "__main__":
    __main__()