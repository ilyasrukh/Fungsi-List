Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Buat data Nama dan Nomor Telephone
>>> a = {"Nama" : ['Jane Doe', 'John Smith', 'Bob Stone'], "Telephone Number" : ['+27 555 5367', '+27 555 6254', '+27 555 5689']}
>>> #Update Nomor Baru Jane Doe
>>> a["Telephone Number"][0] = '+27 555 1024'
>>> a
{'Nama': ['Jane Doe', 'John Smith', 'Bob Stone'], 'Telephone Number': ['+27 555 1024', '+27 555 6254', '+27 555 5689']}
>>> #Tambah Data baru dengan Nama Anna Coper dan Telephone Number +27 555 3237
>>> a.update({"Nama" : ['Jane Doe', 'John Smith', 'Bob Stone', 'Anna Coperr'], "Telephone Number" : ['+27 555 5367', '+27 555 6254', '+27 555 5689', '+27 555 3237']})
>>> a
{'Nama': ['Jane Doe', 'John Smith', 'Bob Stone', 'Anna Coperr'], 'Telephone Number': ['+27 555 5367', '+27 555 6254', '+27 555 5689', '+27 555 3237']}
>>> #Mencetak Telephone Number Bob Stone
>>> a["Telephone Number"][2]
'+27 555 5689'
>>> #Mencetak Semua KEYS dari Dictionary
>>> a.keys()
['Nama', 'Telephone Number']
>>> #Mencetak Semua Values dari Dictionary
>>> a.values()
[['Jane Doe', 'John Smith', 'Bob Stone', 'Anna Coperr'], ['+27 555 5367', '+27 555 6254', '+27 555 5689', '+27 555 3237']]
>>> 
