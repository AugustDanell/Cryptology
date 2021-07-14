def ceasar(secret_key, plaintext, op = "ENCRYPT"):
    encrypted_text = ""
    if(op == "DECRYPT"):
        secret_key = -secret_key

    for i in plaintext:
        normalized_id, back_into_ascii = 0, ""
        alphabet_size = 26

        if(i.isupper()):
            normalized_id = (ord(i)-65 + secret_key)
            back_into_ascii = chr((normalized_id%alphabet_size)+65)
        else:
            normalized_id = (ord(i)-97 + secret_key)
            back_into_ascii = chr((normalized_id%alphabet_size)+97)

        encrypted_text += back_into_ascii

    return encrypted_text

def affine_cypher():
    pass