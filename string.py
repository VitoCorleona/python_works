# string-matn
ism = "Ilhomjon"
shahar = "Кокон"
viloyad = "Фаргана"
matn = "Men yangi 📱 sotib oldim"
smile = "😂"
# unicode-table dan belgilar olinadi
print (matn)
info = (ism, shahar, viloyad, matn, smile)
print(info)

# string ustidan amallar

ism ='Ahmad'
print ("Mening ismim " + ism)
# print ("Mening ismim" + ( ) + ism)
ism = 'Ilhomjon'
familya = 'Toshmurodov'
print (ism + familya)

ism = 'Ilhomjon'
familya = 'Toshmurodov'
print (ism + ' ' + familya)

# f-string yozilishi f"..." bir nechta o'zgaruvchilarni birlashtiradi
ism = 'Tolib'
familya = 'Shox'
ism_familya = f"{ism} {familya}"
print (ism_familya)

ism = 'james'
familya = 'bond'
print(f"Salom mening ismim {familya}, {ism} {familya}!")

# \t uzun bo'shliq qoldiradi. \n qatorlarga bo'ladi
print('hello world')
print('hello \tworld')
print('hello \nworld')

# string metodlar formulasi "matn.metod()"
ism = 'jim'
familya = 'cerry'
ism_sharf = f'{ism} {familya}'
print (ism_sharf.upper()) # izoh upper hamma harflarni katta harf qiladi.
ism_sharf = ism_sharf.upper() # izoh o'zgaruvchilarga boshqa qiymat berildi
print (ism_sharf.lower()) # izoh lower hariflarni kichkina qiladi
print (ism_sharf.title()) # izoh title har bir so'zning ilk harfini katta qiladi
print (ism_sharf.capitalize()) # izoh capitalize faqat ilk harifni katta qiladi

# strip, lstrip, rstrip bo'sh joylarni yo'qotadi
meva = "           olma            "
print ("men " + meva.lstrip() + "yaxshi ko'raman")
print ("men " + meva.rstrip() + "yaxshi ko'raman")
print ("men " + meva.strip() + "yaxshi ko'raman")

# input foydalanuvchidan malumot so'raydi
#ism = input('What is your name?')
# print ('Qaleysan, ' + ism)

#ism = input('What is your name? \n>>>')
# print ('Qaleysan, ' + ism.title())

ism = 'ravshan'
familya = 'yangiboyev'
ism_sharf = f'{ism} {familya}'
print (ism_sharf.title())