# a = 10, a adalah variabel dengan nilai 10

# angka satuan yang gk ada koma nya = integer
DataInteger = 3
print("data :",DataInteger)
print("tipe data :",type(DataInteger))

# angka dengan koma = float
DataFloat = 6.90
print("data :",DataFloat)
print("tipe data :",type(DataFloat))

# kumpulan karakter = string
DataString = "apa coba"
print("data :",DataString)
print("tipe :",type(DataString))

# biner true/false
DataBoolean = True # huruf pertama harus besar
print("data :",DataBoolean)
print("tipe :",type(DataBoolean))

"""tipe data khusus"""

# bilangkan kompleks
DataComplex = complex(3,6)
print("data :",DataComplex)
print("tipe :",type(DataComplex))

# tipe data dari bahasa c
from ctypes import c_double,c_char
DataC_double = c_double(50.69)
print("data :",DataC_double)
print("tipe :",type(DataC_double))