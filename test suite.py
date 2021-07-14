from weak_cryptology import ceasar, vigenere_cypher as vigenere
from attacks import ceasar_brute_force_attack

plain_text_lower = "abc"
plain_text_upper = "ABC"

assert ceasar(1, plain_text_lower, "ENCRYPT") == "bcd"
assert ceasar(1, plain_text_lower) == ceasar(1, plain_text_upper).lower()
assert ceasar(1, ceasar(1, plain_text_lower, "ENCRYPT"), "DECRYPT") == plain_text_lower
assert ceasar(1, ceasar(1, plain_text_lower, "ENCRYPT"), "DECRYPT") == ceasar(1, ceasar(1, plain_text_lower, "DECRYPT"), "ENCRYPT")

# The ceasar cipher is weak, we can brute force it quickly as can be seen here. At maximum we need to test for 26 keys:
test_ceasar_brute_force = False
if(test_ceasar_brute_force):
    message = "We attack at noon!"
    key = 5
    crypto_message = ceasar(5, message, "ENCRYPT")
    ceasar_brute_force_attack(crypto_message)

## Vigenere cipher, an intervowing of the ceasar cipher (see week cryptology)
assert vigenere([1,2,3],"aa", "ENCRYPT") == "bc"
assert vigenere([1,2,3], "bc", "DECRYPT") == "aa"
assert vigenere([1,2],"aaaaaaaa") == "bcbcbcbc"
