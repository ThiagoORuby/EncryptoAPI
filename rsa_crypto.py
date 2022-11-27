import math


class RSA:

    def __init__(self):
        #creating the number convert lists
        _alfabeto = "abcdefghijklmnopqrstuvwxyz "
        self._letras = {_alfabeto[i-2] : i for i in range(2,29)}
        self._numeros = {i : _alfabeto[i-2] for i in range(2,29)}
    
    # Extended Euclides Algorithm
    def _modinverse(self, a, b, x, y):
        if(a % b == 0): return y
        q = a // b
        return self._modinverse(b, a % b, y, x - y*q)

    def generatePublicKey(self, p, q, e):
        # Testar se p e q são primos
        n = p * q

        # Testa se e é relativamente primo a tot de n -> mdc(tot, e) = 1
        tot = (p - 1)*(q - 1)
        if math.gcd(tot, e) != 1:
            raise ValueError("O valor de e não é primo com totiente de n")

        return n, e

    def _listToString(self, list):
        newList = [str(i) for i in list]
        return " ".join(newList)
    
    def encrypting(self, mensage, n, e):
        code_m = [self._letras[i] for i in mensage.lower()]
        cripted = [i**e % n for i in code_m]
        return self._listToString(cripted)

    def fast_mod_exp(self, b, exp, m):
        res = 1
        while exp > 1:
            if exp & 1:
                res = (res * b) % m
            b = b ** 2 % m
            exp >>= 1
        return (b * res) % m    

    def decrypting(self, cripted, p, q, e):
        tot = (p - 1)*(q - 1)
        print(tot)
        print(e)
        #d = pow(e, -1, tot) % tot
        d = self._modinverse(e, tot, 1, 0) % tot
        print(d)
        cripted = cripted.split()
        n = p*q
        decrypted = [self.fast_mod_exp(int(i), d, n) for i in cripted]
        mensage = [self._numeros[i] for i in decrypted]
        return ''.join(mensage).upper()

