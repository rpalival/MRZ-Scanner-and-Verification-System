"""
@author - RAJ PALIVAL
This python file has 2 Dummy functions namely HardwareScanner() and sampleDatabase(),
These dummy functions will be mocked in the unittest file.

The other main functions are: decode() and encode()
decode: takes in a complete MRZ string from hardware scanner and returns all the information fields in their respective variables
encode: takes in a complete information of the passport holder as a dictionary and return the complete MRZ strip.
        along with the certain information fields whose check digit is to be computed

There are two seperate functions to implement the check-digit calculation:
charValue(): This function takes in a character and returns the numeric value of that character starting from A=10 B=11...and '<' = 0
checkDigit(): This funtion takes in a information field from the encode function in form of a string and returns the check digit for that field

Last function which is mismatch:
mismatch(): This function compares the checkdigit from decode() and checkdigit computed from checkDigit() and
            matches them, if there is a mismatch it outputs which information field did the mismatch happen.

"""
class HardwareScanner():   #Dummy hardware Scanner function 1; giving out random MRZ data to be used by function 2
    # MRZ = "P<LKABLACK<<DOMINIQUE<CORALIE<<<<<<<<<<<<<<<;R724644M28LKA6301307M6801184RZ671583Y<<<<<<6"
    pass

def decode():
    MRZLine = HardwareScanner()
    sName = MRZLine.MRZ
    lines = sName.split(";")
    L1 = lines[0]
    L2 = lines[1]
    Lfirstsplit = L1.split("<<")[0]
    Rfirstsplit = L1.split("<<")[1]
    document_type = Lfirstsplit.split("<")[0]
    issuing_country = Lfirstsplit.split("<")[1][:3]
    last_name = Lfirstsplit.split("<")[1][3:]
    if('<' in Rfirstsplit):
        given_name = Rfirstsplit.split("<")
        given_name = str(given_name[0]+ " " +given_name[1])
    else:
        given_name = Rfirstsplit

    passport_number = L2[:9]
    passport_number_Cdigit = L2[9]
    country_code = L2[10:13]
    birth_date = L2[13:19]
    birth_date_Cdigit = L2[19]
    sex = L2[20]
    expiration_date = L2[21:27]
    expiration_date_Cdigit = L2[27]
    personal_number = L2[28:37]
    personal_number_Cdigit = L2[-1]

    return (passport_number_Cdigit, birth_date_Cdigit, expiration_date_Cdigit, personal_number_Cdigit,
    passport_number, birth_date, expiration_date,personal_number,country_code, last_name, given_name,
    document_type, issuing_country,sex)

# print(decode())
class sampleDatabase():
    # sampleData = {
    #         "line1": {
    #             "issuing_country": "LKA",
    #             "last_name": "BLACK",
    #             "given_name": "DOMINIQUE CORALIE"
    #         },
    #         "line2": {
    #             "passport_number": "R724644M3",
    #             "country_code": "LKA",
    #             "birth_date": "630130",
    #             "sex": "M",
    #             "expiration_date": "680118",
    #             "personal_number": "RZ671583Y"
    #         }
    #     }
    pass

def charValue(c):
    if c >= '0' and c <= '9':
        return ord(c) - ord('0')
    if c >= 'A' and c <= 'Z':
        return ord(c) - ord('A') + 10
    if c == '<':
        return 0

def checkDigit(data):
    multiplier = [7, 3, 1]
    sum = 0
    for index,char in enumerate(data):
        product = charValue(char) * multiplier[index % len(multiplier)]
        sum += product
    cdigit = sum % 10
    return cdigit

def encode():
    dictObj = sampleDatabase()
    d = dictObj.sampleData
    given_name = d['line1']['given_name']
    if(" " in (d['line1']['given_name'])):
        given_name = given_name.replace(" ","<")
    else:
        given_name = given_name
    passport_number = d['line2']['passport_number']
    birth_date = d['line2']['birth_date']
    expiration_date = d['line2']['expiration_date']
    personal_number = d['line2']['personal_number']
    line1 = f"P<{d['line1']['issuing_country']+d['line1']['last_name']}<<{given_name}"
    N = 44 - len(line1)
    finalline1 = str(line1.ljust(N + len(line1),'<'))

    line2 = f"{passport_number+str(checkDigit(passport_number))}{d['line2']['country_code']}"
    line2a = f"{birth_date+str(checkDigit(birth_date))+d['line2']['sex']}"
    line2b = f"{expiration_date+str(checkDigit(expiration_date))+personal_number}"
    finalline2 = str(line2+line2a+line2b)+f"<<<<<<{str(checkDigit(personal_number))}"
    finalline = finalline1+";"+finalline2
    return passport_number,birth_date,expiration_date,personal_number,finalline

# print(encode())

var_dict = {0:'Passport Number', 1:'Birth Date', 2:'Expiration Date', 3:'Personal Number'}
def mismatch():
    a = True
    mismatch_fields = []
    for x in range(len(var_dict)):
        digit= decode()[x]
        field = checkDigit(encode()[x])

        if(str(digit) != str(field)):
            a = False
            value = (f"mismatch found in {var_dict[x]}")
            mismatch_fields.append(value)
    if(a==True):
        value = ("No mismatch found!")
        mismatch_fields.append(value)
    return mismatch_fields
        
# print(mismatch())