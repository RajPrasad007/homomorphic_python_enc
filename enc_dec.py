from phe import paillier

public,private = paillier.generate_paillier_keypair()

def enc(data):
    enc_data = public.encrypt(data)
    enc_pub_res = {}
    enc_pub_res["vals"] = int(str(enc_data.ciphertext()), enc_data.exponent)
    return enc_pub_res["vals"]


def decrypt(data):
    enc_datas = paillier.EncryptedNumber(public, int(data))
    plain_ = {}
    plain_['plain_text'] = private.decrypt(enc_datas)
    return plain_['plain_text']



input_ = int(input("Give a number to encrypt and then it will decrypt: "))
add_data = int(input("Enter number to add: "))
enc_add_data = enc(add_data)
mul_data = int(input("Enter number to multiple: "))
enc_mul_data = enc(mul_data)
enc_data = enc(input_)
print(f"Your plain text is encrypted to -> {enc_data}")
print()
print(f"Addition -> {enc_data+enc_add_data}")
print()
print(f"Multiplication -> {enc_data * enc_mul_data}")
print(f" The plaintext is: {decrypt(enc_data)}")
