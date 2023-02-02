import unittest #importo libreria
from lez5.unittest import somma #importo funzione da altro file

class TestSomma(unittest.TestCase): 
    def test_somma(self):
        self.assertEqual(somma(1, 6), 7) #chiamo la funzione con i valori ed il risultato aspettato


if __name__ == "__main__":
    unittest.main()