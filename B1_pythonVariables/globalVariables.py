# global variabel bisa diambil sama fungsi 
x = 123
def fungsi1():
    print("python is",x)

fungsi1()

# jika kita mendeklarasikan variabel yang sama di dalam fungsi si variabel nya akan menjadi variabel lokal dan variabel global x
# tidak akan kena efek apapun dan akan tetap sama
def fungsi2():
    x = 321
    print(x)

fungsi2()

print(x)

# umumnya jika variabel di deklarasikan dalam fungsi, variabel itu akan menjadi variabel local tapi kita bisa mengubah dia menjadi global
# jika menambah kata global didepan nya
def fungsi3():
    global x
    x = 123456

fungsi3()

print(x)
