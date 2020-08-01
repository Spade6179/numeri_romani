import unittest, re
from hypothesis import given
from hypothesis.strategies import integers, text
from numeri_romani import *

class TestNumeri_Romani(unittest.TestCase):

    @given(integers(1,3999))
    def test_OutputIsString(self, g):
        self.assertTrue(type(numeri_romani(g)) == str)
    
    @given(text())
    def test_InputIsInt(self, g):
        if type(g) != int:
            self.assertRaises(ValueError, numeri_romani, g)
            
    def test_ConvertStrToInt(self):
        self.assertEqual(numeri_romani("1"),"I")

    @given(integers())
    def test_InputOutOfRange(self, g):
        if g < 1 or g > 3999:
            self.assertRaises(ValueError, numeri_romani, g)

    @given(integers(1,3999))
    def test_IsStandardOrthography(self, g):
        output = numeri_romani(g)
        ortho = ["I","V","X","L","C","D","M"]
        non_numerals = 0
        for char in output:
            if char not in ortho:
                non_numerals += 1
        self.assertEqual(non_numerals,0)

    @given(integers(1,3999))    
    def test_NoOverDuplication(self, g):
        output = numeri_romani(g)
        invalidSequences = ["IIII", "VV", "XXXX", "LL", "CCCC", "DD", "MMMM"]
        for seq in invalidSequences:
            self.assertFalse(seq in output, f"Too many {seq[0]} in output {output}.".format())

    @given(integers(1,3999))
    def test_Modulo10NumeralsNeverChange(self, g):
        # The numeral for 1 - 9 always appear when that digit is in the ones position.
        # e.g. "IV" appears in 24 (XXIV) and 94 (XCIV).
        lastDigit = g % 10
        single_digit_numeral = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        if lastDigit != 0:
            output = numeri_romani(g)
            self.assertTrue(output.endswith(single_digit_numeral[lastDigit - 1]))
            
    @given(integers(1,3999))
    def test_1000to3999MustHaveNumeral_M(self, g):
        output = numeri_romani(g)
        if g > 999:
            self.assertTrue("M" in output)

    @given(integers(1,3999))
    def test_X_Precedes_L_And_C(self, g):
        output = numeri_romani(g)
        if g % 50 >= 40:
            self.assertTrue("XL" in output or "XC" in output)

    def test_LoneDigitsMatchNumeral(self):
        convertedNumerals = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        for integer, numeral in convertedNumerals.items():
            output = numeri_romani(integer)
            if output != numeral:
                self.fail(f"Expected {numeral} for {integer}, but returned {output}.".format())
    
    @given(integers(1,3999))
    def test_NoPolygraphemicReduplication(self, g):
        # Numeral sequences do not repeat, e.g. XYXY, XYZXYZ, XYZAXYZA
        output = numeri_romani(g)
        invalidPattern = r"([IVXLCDM][IVXLCDM])\1"
        self.assertIsNone(re.search(invalidPattern, output),f"{output} contains illegal duplication of a numeral sequence.".format())
    
    @given(integers(1,3999))
    def test_NoDouble_DLV(self, g):
        output = numeri_romani(g)
        invalidPattern = r"([DLV]).*\1"
        self.assertIsNone(re.search(invalidPattern, output),f"{output} contains illegal duplication of numeral D, L, or V.".format())
    
    @given(integers(1,3999))
    def test_MalformedAntecedents(self, g):
        output = numeri_romani(g)
        invalidSingles = [r"V[XLCDM]", r"X[DM]", r"L[CDM]"]
        invalidDoubles = [r"II[^I]", r"XX[LCDM]", r"CC[DM]", r"IV.", r"IX.", r"XL[XLCDM]", r"XC[XLCDM]", r"CD[CDM]", r"CM[CDM]"]
        invalidOthers = [r"[^M]C[DM]"]
        invalidPatterns = invalidSingles + invalidDoubles + invalidOthers
        for pattern in invalidPatterns:
            self.assertIsNone(re.search(pattern, output),f"{output} contains invalid numeral sequence (matches illegal regex pattern \"{pattern}\").".format())

    @given(integers(1,3999))
    def test_JueHan_RegexTest(self, g):
        # From https://juehan.github.io/DiveIntoPython3_Korean_Translation/unit-testing.html
        # Makes other tests sort of redundant, but they still help to narrow down issue.
        JueHanPattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
        output = numeri_romani(g)
        self.assertIsNotNone(re.search(JueHanPattern,output),f"{g} {output} does not match Jue Han pattern.")

if __name__ == "__main__":
    unittest.main()