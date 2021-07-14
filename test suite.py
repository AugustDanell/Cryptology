from weak_cryptology import ceasar, vigenere_cypher as vigenere

plain_text_lower = "abc"
plain_text_upper = "ABC"

assert ceasar(1, plain_text_lower, "ENCRYPT") == "bcd"
assert ceasar(1, plain_text_lower) == ceasar(1, plain_text_upper).lower()
assert ceasar(1, ceasar(1, plain_text_lower, "ENCRYPT"), "DECRYPT") == plain_text_lower
assert ceasar(1, ceasar(1, plain_text_lower, "ENCRYPT"), "DECRYPT") == ceasar(1, ceasar(1, plain_text_lower, "DECRYPT"), "ENCRYPT")

## Vigenere cipher, an intervowing of the ceasar cipher (see week cryptology)
assert vigenere([1,2,3],"aa", "ENCRYPT") == "bc"
assert vigenere([1,2,3], "bc", "DECRYPT") == "aa"
assert vigenere([1,2],"aaaaaaaa") == "bcbcbcbc"
