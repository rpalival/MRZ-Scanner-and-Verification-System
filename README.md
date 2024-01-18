# SSW567A-Final-Project-Group-9
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/rpalival/MRZ-Scanner-and-Verification-System/tree/main.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/rpalival/MRZ-Scanner-and-Verification-System/tree/main)

[![Code Coverage](./coverageReport/coverage.svg)](./coverageReport/index.html)
    
Final Project Work for SSW 567-A Class

This Project Repo is made for our final project submission from Group-9

Project Requirements:
Suppose you are a developer for the project to implement a system that can read the MRZ of a travel document, process and obtain its fields, and check the fields against the check digits. Following are some requirements and specifications of your system:

1. The system shall be able to scan the MRZ of a travel document using a hardware device scanner and get the information in MRZ as two strings (line 1 and line 2 from the above Figure). Note that you do not need to worry about the implementation of the hardware device. But you need to define this method for the software part. This means that you define an empty method for this function. 
2. The system shall be able to decode the two strings from specification #1 into their respective fields and identify the respective check digits for the fields, following the same format in the above example.
3. The system shall be able to encode travel document information fields queried from a database into the two strings for the MRZ in a travel document. This is the opposite process compared to specification #2. Assume that the database function is not ready. But for testing purposes, you need to define a method for database interaction and leave it empty.
4. The system shall be able to report a mismatch between certain information fields and the check digit. The system shall report where the miss match happened, i.e. which information field does not match its respective check digit.


Team Members:
1.Raj Palival
2.Amith Vishnu
3.Kaijie Ma
4.Pranav Muralidhar Rao


The Files Submitted Here Include:
1. Two Graph Image Files
2. Two CSV Files which shows the excecution Time of PART-3
3. Two Json Files which were used as input for performance testing
4. Main Function file of the project is : MRTD.py
5. Main Test Function file of the project is : MTTDTest.py
6. Source files for performance testing are: decode.py and encode.py
7. All 4 Parts Project Reports are numbered accordingly and uploaded here.
