
Day 3. Unit 1: Validating Credit Card Numbers
Descriptions: 
You and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!
A valid credit card from ABCD Bank has the following characteristics:
► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.

Examples:
Valid Credit Card Numbers
4253625879615786
4424424424442444
5122-2368-7954-3214
Invalid Credit Card Numbers
42536258796157867       #17 digits in card number → Invalid 
4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
44244x4424442444        #Contains non digit characters → Invalid
0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid

Technical Requirements:
•	Must use Python3

------------------------------------------

Day 3. Unit 2: Find The Flag
Descriptions: 
Given a folder that contains some file that has a character of a flag and others do not. Find the flag
Example:
Not a flag: 0Not0 0this0 0file0
Contains the character “}”: } 81This81 81file81
Technical Requirements:
•	Must use Python3
•	Must use os.path module
•	Must use re module

--------------------------------------------

Day 4. Unit 1: Get all the image
Descriptions: 
Write a program to get and download all the image in https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales.
Technical Requirements:
•	Must use Python3

-------------------------------------------

Day 4. Unit 2: Get all the alerts
Descriptions: 
Write a Python program get the number of security alerts issued by US-CERT in the current year.
Source: https://www.us-cert.gov/ncas/alerts 
Technical Requirements:
•	Must use Python3

-------------------------------------------
Day 5. Unit 1: Get all the alerts (continue)
Descriptions: 
Write a Python program get alerts issued by US-CERT in the current year and write output to CSV and Excel file.
Source: https://www.us-cert.gov/ncas/alerts
Output fields: Alert ID, Alert Name, Release Date, Last revised, Tips, Alert Link
Technical Requirements:
•	Must use Python3

----------------------------------------------

Day 6. Unit 1: Base convert
Descriptions: 
Get the flag from this text:
MDAxMTAwMTEwMDExMDExMTAwMTEwMDExMDAxMTAwMTAwMDExMDAxMTAwMTExMDAwMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTEwMDEwMDAxMTAwMTEwMDExMDAwMDAwMTEwMDExMDAxMTAxMDAwMDExMDAxMTAwMTExMDAwMDAxMTAwMTEwMDExMDExMTAwMTEwMDExMDAxMTAwMTAwMDExMDAxMTAwMTEwMTAwMDAxMTAwMTEwMDExMTAwMDAwMTEwMDExMDAxMTAxMTEwMDExMDAxMTAwMTEwMDExMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTAxMDEwMDExMDAxMTAwMTEwMTExMDAxMTAwMTEwMDExMDExMDAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTEwMDAxMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTAxMTAwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMDAwMTAwMTEwMDExMDAxMTAwMDAwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTAwMDAwMDExMDAxMTAwMTEwMTAwMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTAxMDEwMDExMDAxMTAwMTEwMTExMDAxMTAwMTEwMDExMDAwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTAwMDAwMDExMDAxMTAwMTExMDAwMDAxMTAwMTEwMDExMDEwMDAwMTEwMDExMDAxMTAxMDEwMDExMDAxMTAwMTEwMDExMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTAwMDAwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMDAwMDAwMTEwMDExMDAxMTAxMDEwMDExMDAxMTAwMTEwMDAxMDAxMTAwMTEwMDExMTAwMDAwMTEwMDExMDAxMTAxMTEwMDExMDAxMTAwMTEwMTAwMDAxMTAwMTEwMDExMTAwMDAwMTEwMDExMDAxMTEwMDEwMDExMDAxMTAwMTEwMDAwMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTExMDAwMDAxMTAwMTEwMDExMDExMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTEwMDAxMDAxMTAwMTEwMDExMDEwMTAwMTEwMDExMDAxMTEwMDEwMDExMDAxMTAwMTEwMDAwMDAxMTAwMTEwMDExMDAwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMDExMTAwMTEwMDExMDAxMTAxMTAwMDExMDAxMTAwMTEwMTAwMDAxMTAwMTEwMDExMTAwMTAwMTEwMDExMDAxMTEwMDEwMDExMDAxMTAwMTEwMDAwMDAxMTAwMTEwMDExMDAwMTAwMTEwMDExMDAxMTAwMDEwMDExMDAxMTAwMTExMDAxMDAxMTAwMTEwMDExMTAwMDAwMTEwMDExMDAxMTAxMTEwMDExMDAxMTAwMTEwMTAxMDAxMTAwMTEwMDExMDExMQ==
Flag format: Py4SE{FLAG}
Process to get this text:
Base64 -> ROT13 -> decimal ->  hex -> binary -> Base 64 = x

Technical Requirements:
•	Must use Python3
------------------------------------------------------

Day 6. Unit 2: File format convert (part 2)
Descriptions: 
Write a Python program to read all the file from folder and change from:
	json or yaml to csv
	csv to json
Sample command:
python3 convert_types.py test/
Technical Requirements:
•	Must use Python3
•	Must use os.path module
-------------------------------------------------------

Day 8. Unit 1: Cat search Discord bot
Descriptions: 
Write a Discord bot that
- Send a cat image every 5 minus
- Search cat image with inline command
Technical Requirements:
•	Must use Python3
------------------------------------------------------

Day 8. Unit 2: Cat search Slack bot
Descriptions: 
Write a Slack bot that
- Send a cat image every 5 minus
- Search cat image with inline command
Technical Requirements:
•	Must use Python3
----------------------------------------------------

Day 9. Unit 1: file
Descriptions: 
Write a Python program to do everything the file command can do
Source: https://linux.die.net/man/1/file
Technical Requirements:
•	Must use Python3

------------------------------------------------------
Day 9. Unit 2: cut
Descriptions: 
Write a Python program to do everything the cut command can do
Source: https://linux.die.net/man/1/cut
Technical Requirements:
•	Must use Python3







