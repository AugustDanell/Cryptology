from weak_cryptology import ceasar

''' ceasar_brute_force_attack
    Naturally the Ceasar cipher is not very powerful simply because it can easily be brute forced, that is we try to crack it by systematically iterate through all possible keys. The Ceasar cipher uses the 26 letters of the alphabet and so what we can do is iterate through every possible key and test it. 
'''

def ceasar_brute_force_attack(cryptotext):
    key = 0
    inp = "no"
    while(not (inp.lower() == "yes")):
        print(ceasar(key, cryptotext, "DECRYPT"))
        inp = input("Is this your wanted cryptotext?")
        key += 1
