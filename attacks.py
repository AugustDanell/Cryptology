from weak_cryptology import ceasar

def ceasar_brute_force_attack(cryptotext):
    key = 0
    inp = "no"
    while(not (inp.lower() == "yes")):
        print(ceasar(key, cryptotext, "DECRYPT"))
        inp = input("Is this your wanted cryptotext?")
        key += 1
