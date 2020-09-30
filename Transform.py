def convertpass(plaintext):
key = [plaintext[0]]
counter = 1
i = 0
while counter != 16:
key.append(plaintext[(i+i//2)%len(plaintext)])
i += 9
counter += 1
return "".join(key)
def convertToMUL8(m):
length = len(m)
spaces = length % 8
spaces = 8 - spaces
return m + " "*spaces
def convertToOriginal(ciphertext):
return ciphertext.rstrip()
CreateDB.py
import sqlite3
if __name__ == "__main__":
conn = sqlite3.connect("Data.db")
c = conn.cursor()
c.execute("CREATE TABLE USERS(ID INTEGER PRIMARY KEY AUTOINCREMENT, USERNAME TEXT, PASSWORD TEXT);")
c.execute("CREATE TABLE PASSES(ID INTEGER, APPLICATION TEXT, USERNAME TEXT, PASSWORD TEXT, IV TEXT);")
print("DataBase Created.")
