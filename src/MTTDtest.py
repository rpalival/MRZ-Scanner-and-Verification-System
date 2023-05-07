import unittest
from unittest.mock import patch
from MRTD import decode,encode,mismatch,checkDigit,charValue

#Mock Classes for Hardware Scanner which has sample data in form of a string and dictionary to pass them into decode and encode functions
class MockResponse():
    MRZ = "P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G54CIV5910106F9707302AJ010215I<<<<<<6"
    sampleData = {
            "line1": {
                "issuing_country": "CIV",
                "last_name": "LYNN",
                "given_name": "NEVEAH BRAM"
            },
            "line2": {
                "passport_number": "W620126G5",
                "country_code": "CIV",
                "birth_date": "591010",
                "sex": "F",
                "expiration_date": "970730",
                "personal_number": "AJ010215I"
            }
        }
class MockResponse1():
    MRZ = "P<ABWMALDONADO<<CAMILLA<<<<<<<<<<<<<<<<<<<<<;V008493B64ABW7809095M0909088QZ181922T<<<<<<5"
    sampleData = {
            "line1": {
                "issuing_country": "ABW",
                "last_name": "MALDONADO",
                "given_name": "CAMILLA"
            },
            "line2": {
                "passport_number": "V008493B6",
                "country_code": "ABW",
                "birth_date": "780909",
                "sex": "M",
                "expiration_date": "090908",
                "personal_number": "QZ181922T"
            }
        }
class MockResponse2():
    MRZ = "P<LKABLACK<<DOMINIQUE<CORALIE<<<<<<<<<<<<<<<;R724644M28LKA6301307M6801184RZ671583Y<<<<<<6"
    sampleData = {
            "line1": {
                "issuing_country": "LKA",
                "last_name": "BLACK",
                "given_name": "DOMINIQUE CORALIE"
            },
            "line2": {
                "passport_number": "R724644M2",
                "country_code": "LKA",
                "birth_date": "630130",
                "sex": "M",
                "expiration_date": "680118",
                "personal_number": "RZ671583Y"
            }
        }
class MockResponse2():
    MRZ = "P<LKABLACK<<DOMINIQUE<CORALIE<<<<<<<<<<<<<<<;R724644M28LKA6301307M6801184RZ671583Y<<<<<<6"
    sampleData = {
            "line1": {
                "issuing_country": "LKA",
                "last_name": "BLACK",
                "given_name": "DOMINIQUE CORALIE"
            },
            "line2": {
                "passport_number": "R724644M2",
                "country_code": "LKA",
                "birth_date": "630130",
                "sex": "M",
                "expiration_date": "680118",
                "personal_number": "RZ671583Y"
            }
        }
class MockResponse3():
    MRZ = "P<LKABLACK<<DOMINIQUE<CORALIE<<<<<<<<<<<<<<<;R724644M28LKA6301307M6801184RZ671583Y<<<<<<6"
    sampleData = {
            "line1": {
                "issuing_country": "LKA",
                "last_name": "BLACK",
                "given_name": "DOMINIQUE CORALIE"
            },
            "line2": {
                "passport_number": "R724644M3",
                "country_code": "LKA",
                "birth_date": "630130",
                "sex": "M",
                "expiration_date": "680118",
                "personal_number": "RZ671583Y"
            }
        }
class MockResponse4():
    MRZ = "P<LKABLACK<<DOMINIQUE<CORALIE<<<<<<<<<<<<<<<;R724644M28LKA6301307M6801184RZ671583Y<<<<<<6"
    sampleData = {
            "line1": {
                "issuing_country": "LKA",
                "last_name": "BLACK",
                "given_name": "DOMINIQUE CORALIE"
            },
            "line2": {
                "passport_number": "R724644M3",
                "country_code": "LKA",
                "birth_date": "640130",
                "sex": "M",
                "expiration_date": "680118",
                "personal_number": "RZ671583Y"
            }
        }



class TestMRTD(unittest.TestCase):
    #Test case 1: to mock hardware scanner and to test decode function
    @patch('MRTD.HardwareScanner', side_effect = MockResponse)
    def test_decode(self, mock_obj):
        self.assertEqual(decode(),('4', '6', '2', '6', 'W620126G5', '591010', '970730', 'AJ010215I', 'CIV', 'LYNN', 'NEVEAH BRAM', 'P', 'CIV', 'F'))
    
    #Test case 2: to mock hardware scanner and to test decode function on a person with single given name
    @patch('MRTD.HardwareScanner', side_effect = MockResponse1)
    def test_decode1(self, mock_obj):
        self.assertEqual(decode(),('4', '5', '8', '5', 'V008493B6', '780909', '090908', 'QZ181922T', 'ABW', 'MALDONADO', 'CAMILLA', 'P', 'ABW', 'M'))
    
    #Test case 3: to mock hardware scanner and to test decode function on a person with first name and last name as given name
    @patch('MRTD.HardwareScanner', side_effect = MockResponse2)
    def test_decode2(self, mock_obj):
        self.assertEqual(decode(),('8', '7', '4', '6', 'R724644M2', '630130', '680118', 'RZ671583Y', 'LKA', 'BLACK', 'DOMINIQUE CORALIE', 'P', 'LKA', 'M'))

    #Test case 4: to mock Database and to test encode function
    @patch('MRTD.sampleDatabase', side_effect = MockResponse)
    def test_encode(self, mock_obj):
        self.assertEqual(encode(),('W620126G5', '591010', '970730', 'AJ010215I', 'P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G54CIV5910106F9707302AJ010215I<<<<<<6'))

    #Test case 5: to mock Database and to test encode function for the same person as in my 2nd test case
    @patch('MRTD.sampleDatabase', side_effect = MockResponse1)
    def test_encode1(self, mock_obj):
        self.assertEqual(encode(),('V008493B6', '780909', '090908', 'QZ181922T', 'P<ABWMALDONADO<<CAMILLA<<<<<<<<<<<<<<<<<<<<<;V008493B64ABW7809095M0909088QZ181922T<<<<<<5'))

    #Test case 6: to mock Database and to test encode function for the same person as in my 3rd test case
    @patch('MRTD.sampleDatabase', side_effect = MockResponse2)
    def test_encode2(self, mock_obj):
        self.assertEqual(encode(),('R724644M2', '630130', '680118', 'RZ671583Y', 'P<LKABLACK<<DOMINIQUE<CORALIE<<<<<<<<<<<<<<<;R724644M28LKA6301307M6801184RZ671583Y<<<<<<6'))

    # Test case 7: to mock and test mismatch function by checking the hardware scanner check digit with the computed check digit from database
    @patch('MRTD.HardwareScanner',side_effect = MockResponse)
    @patch('MRTD.sampleDatabase',side_effect = MockResponse)
    def test_mismatch(self, mock_obj,mock_obj2):
        self.assertEqual(mismatch(),["No mismatch found!"])
    
    # Test case 8: To kill a mutant, Added this new test case, which tests mismatch in passport number
    @patch('MRTD.HardwareScanner',side_effect = MockResponse3)
    @patch('MRTD.sampleDatabase',side_effect = MockResponse3)
    def test_mismatch1(self, mock_obj,mock_obj2):
        self.assertEqual(mismatch(),['mismatch found in Passport Number'])
    
    # Test case 9: To kill a mutant, Added this new test case, which tests mismatch in passport number and birthdate
    @patch('MRTD.HardwareScanner',side_effect = MockResponse4)
    @patch('MRTD.sampleDatabase',side_effect = MockResponse4)
    def test_mismatch2(self, mock_obj,mock_obj2):
        self.assertEqual(mismatch(),['mismatch found in Passport Number', 'mismatch found in Birth Date'])
        
    # Test case 10: To kill a mutant, added this test case to cover checkDigit function for checking passport number check digit
    def test_checkDigit(self):
        self.assertEqual(checkDigit("V008493B6"),4)
    
    # Test case 11: To kill a mutant, added this test case to cover checkDigit function for checking birth date check digit
    def test_checkDigit1(self):
        self.assertEqual(checkDigit("591010"),6)
    
    # Test case 12: To kill a mutant, added this test case to cover charValue function as well
    def test_charValue(self):
        self.assertEqual(charValue("C"),12)
    
    # Test case 13: To kill a mutant, added this test case to cover charValue function as well with different character
    def test_charValue1(self):
        self.assertEqual(charValue("<"),0)

    # Test case 14: To kill a mutant, added this test case to cover charValue function as well with different character number
    def test_charValue2(self):
        self.assertEqual(charValue("4"),5)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
