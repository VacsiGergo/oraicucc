import unittest

def armstrong(n: int):
    osszeg = 0
    szamjegyek = len(str(n))
    for i in str(n):
        osszeg += int(i) ** szamjegyek
    if osszeg == n:
        return True
    else:
        return False

megadottSzam = int(input("Input: "))
print(f"Return: {armstrong(megadottSzam)}")

class TestArmstrong(unittest.TestCase):
    
    def test_armstrong_valid(self):
        self.assertTrue(armstrong(153))

    def test_armstrong_invalid(self):
        self.assertFalse(armstrong(123))

if __name__ == '__main__':
    unittest.main()

##------------------------------------------------------##
##------------------------------------------------------##

def jelszo_erosseg(s: str):
    erosseg = 1
    nemjo = "jelszo"
    nemjoszam = "123"
    if nemjo not in s and nemjoszam not in s or len(s) == 0:
        if len(s) >= 5:
            erosseg += 1
            if len(s) >= 8:
                erosseg += 2
        for char in s:
            if char == "_" or char == "-" or char == ".":
                erosseg += 2
    else:
        erosseg = 0
    return erosseg

jelszo = input("Input: ")
print(f"Return: {jelszo_erosseg(jelszo)}")

class TestJelszoErosseg(unittest.TestCase):
    
    def test_jelszo_mukszik(self):
        self.assertEqual(jelszo_erosseg("hazi_macska_4_life"), 10)
    
    def test_jelso_works(self):
        self.assertEqual(jelszo_erosseg("ez1feltorhetetlenjelszo"), 0)
    
if __name__ == '__main__':
    unittest.main()

##------------------------------------------------------##
##------------------------------------------------------##

