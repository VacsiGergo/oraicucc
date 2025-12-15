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