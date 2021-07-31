def ascii_to_alphabetic_num(x):
    if(x.isupper()):
        return (ord(x)-65), True
    elif(x.islower()):
        return (ord(x)-97), False

def alphabetic_num_to_ascii(x,isUpper, alphabet_size = 26):
    if(isUpper):
        return chr((x%alphabet_size)+65)
    else:
        return chr((x%alphabet_size)+97)

def find_modular_inverse(x,mod):
    x_inv = 1
    while(not ((x_inv*x)%mod == 1)):
        x_inv+= 1

    return x_inv

def ceasar(secret_key, plaintext, op = "ENCRYPT"):
    encrypted_text = ""
    if(op == "DECRYPT"):
        secret_key = -secret_key

    for i in plaintext:
        back_into_ascii = " "
        if(i.isalpha()):
            normalized_id, isUpper = ascii_to_alphabetic_num(i)
            back_into_ascii = alphabetic_num_to_ascii(normalized_id + secret_key, isUpper)
            alphabet_size = 26

        encrypted_text += back_into_ascii

    return encrypted_text

def vigenere_cypher(secret_key, plaintext, op = "ENCRYPT"):
    index = 0
    roof = len(secret_key)
    crypto_list = []
    for i in plaintext:
        crypto_list.append(ceasar(secret_key[index], i, op))
        index += 1
        index %= roof

    return "".join(crypto_list)

def reconstruct_key(secret_key, crypto_text):
    key = secret_key
    tabula_recta = [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z"]] * 26


    return key

print(reconstruct_key("hey"))

def autokey_cipher(secret_key, plaintext, op = "ENCRYPT"):
    if(op == "ENCRYPT"):
        big_key = list (plaintext)
        init_len = len(big_key)
        for i in reversed(range(len(secret_key))):
            big_key.insert(0, secret_key[i])
        vigenere_key = list (map(ascii_to_alphabetic_num, big_key))
        keystream = list (map(lambda x: x[0], vigenere_key))

        return vigenere_cypher(keystream, plaintext, op="ENCRYPT") # Ciphertext
    else:
        cyphertext = plaintext
        # 1. We need to reconstruct the entire key.
        reconstructed_keystream = reconstruct_key(secret_key)

        # 2. We can apply then, surely, vigenere backwards.
        return vigenere_cypher(reconstructed_keystream, cyphertext, op = "DECRYPT")

print(autokey_cipher("ACM", "SENDMOREMONKEYS"))
print(autokey_cipher("ACM", "SGZVQBUQAFRWSLC", op = "DECRYPT"))

def affine_cypher(key_a, key_b, plaintext, op = "ENCRYPT"):
    alphabet_size = 26
    crypto_text = []

    if (op == "DECRYPT"):
        a_inv = find_modular_inverse(key_a, alphabet_size)

    for i in plaintext:
        alpha_number, isUpper = ascii_to_alphabetic_num(i)
        secret_key = ((alpha_number+1) * key_a + key_b) % alphabet_size

        if(op == "DECRYPT"):
            pass

        transform = alpha_number + secret_key
        crypto_text.append(alphabetic_num_to_ascii(transform, isUpper, alphabet_size))

    return "".join(crypto_text)
