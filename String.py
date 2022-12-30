#Latihan1

txt = 'Hello World'
panjang = len(txt)
print("Panjang dari " + txt + " : " + str(panjang))
print("index terakhir : " + txt[-1])
print("index ke-[2:5] : " + txt[2:5])
print("Menghilangkan spasi : " + txt.replace(' ',''))
print("Text besar : " + txt.upper())
print("Text kecil : " + txt.lower())
print("Mengganti karakter H menjadi J : " + txt.replace('H','J'))


#Latihan2

umur = 24
txt = 'Hello, nama saya john, dan umur saya adalah ' + str(umur) + ' tahun'
print(txt.format(umur))