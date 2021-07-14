from weak_cryptology import ceasar

plain_text_lower = "abc"
plain_text_upper = "ABC"

assert ceasar(1, plain_text_lower, "ENCRYPT") == "bcd"
assert ceasar(1, plain_text_lower) == ceasar(1, plain_text_upper).lower()
assert ceasar(1, ceasar(1, plain_text_lower, "ENCRYPT"), "DECRYPT") == plain_text_lower
assert ceasar(1, ceasar(1, plain_text_lower, "ENCRYPT"), "DECRYPT") == ceasar(1, ceasar(1, plain_text_lower, "DECRYPT"), "ENCRYPT")
