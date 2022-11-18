print("~~~~CAFE TEKNIK~~~~")
pembeli = input("\nMasukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 
total1=0
jenis1=""
porsi=0
gelas=0

def fungsimakanan():
   global total1
   global porsi
   global jenis1
   print ("\n~~~~Menu Makanan~~~~")
   print("1. Nasi kebuli - Rp15000")
   print("2. Ayam Goreng - Rp15000")
   print("3. Ikan Goreng - Rp10000\n")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       total1=porsi*15000
       print (porsi," porsi Nasi Kebuli = Rp", total1)
       jenis1=("Nasi Kebuli")
   elif nomor==2:
       total1=porsi*15000
       print (porsi," Ayam Goreng = Rp", total1)
       jenis1=("Ayam Goreng")
   elif nomor==3:
       total1=porsi*10000
       print (porsi, " Ikan Goreng = Rp", total1)
       jenis1=("Ikan Goreng")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()


fungsimakanan()

total2=0
jenis2=""

def fungsiminuman():
   global total2
   global jenis2
   global gelas
   print("\n~~~~Menu Minuman~~~~")
   print("1. Es teh - Rp5000")
   print("2. Es jeruk - Rp7000")
   print("3. Es kopi - Rp5000\n")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       total2=gelas*5000
       print (gelas," Es Teh = Rp", total2)
       jenis2=("Es Teh")
   elif nomor==2:
       total2=gelas*7000
       print (gelas, " Gelas Es Jeruk = Rp", total2)
       jenis2=("Es Jeruk")
   elif nomor==3:
       total2=gelas*5000
       print (gelas, " Gelas Es Kopi = Rp", total2)
       jenis2=("Es Kopi")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()



fungsiminuman()
    
totalsemua=0
totalsemua=total1+total2
print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp."))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n========== C A F E   T E K N I K ===========")
print("============ S T R U K   B E L I ===========")
print("============================================")
print (" Nama         :",pembeli)
print (" Beli         :",porsi,jenis1,"-", total1)
print ("              :",gelas,jenis2,"-", total2)
print (" Tagihan      : Rp.",totalsemua)
print (" Uang         : Rp.",uang)
print (" Kembalian    : Rp.",kembalian)
print("============================================")
print("==================TERIMA KASIH==============")
