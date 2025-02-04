#tuple(demetler) parantezlerle oluşturulur. elemanlarını değiştiremeyiz. ya boş demet diye ya da içini doldurarak oluşturulabilirler.
demet = tuple()
demet = tuple(("ankara","istanbul", "kayseri"))
#eğer tek elemanlı oluşturulmak isteniyorsa ilk elemandan sonra virgül koyulmalıdır. eğer koyulmazsa veri tipi string olur.
#oluşturulan demet değişkenlerinin tipinin kontrol edilmesi için;
print(type(demet)) #<class 'tuple'>
#bir demetin elemanlarına ulaşmak için indexler kullanırız. index her zaman 0'dan başlar.
demet = ("ceviz", "fındık", "fıstık", "leblebi")
print(demet[0]) #ceviz
print(demet[1]) #fındık
print(demet[2]) #fıstık
print(demet[3]) #leblebi
#negatif indexleme: negatif index kullanarak demeti tersten başlanarak ele alınabilir. (0) kullanılmaz.
print(demet[-1]) #leblebi
print(demet[-2]) #fıstık
print(demet[-3]) #fındık
print(demet[-4]) #ceviz
#yeni demet oluşturmak
demet = ("a", "b", "c", "d", "e", "f", "g")
yenidemet = demet[2:5]
print(yenidemet) #("c", "d", "e")
#negatif indexle yeni demet oluşturmak
demet = ("a", "b", "c", "d", "e", "f", "g")
yenidemet = demet[-3:-1]
print(yenidemet) #("e", "f")
#demet elemanlarını sıralayarak ekrana yazdırmak
demet = ("a", "b", "c", "d", "e", "f", "g")
for x in demet:
    print(x)
#bu şekilde x üzerinden demetin tüm değerlerini otomatilk olarak sıralayarak ekrana yazdıracaktır.
#bir elemanın demette kaç defa bulunduğunu öğrenmek istediğimizde count kullanırız.
demet = ("a", "b", "c", "d", "e", "f", "g")
sayac = demet.count("c")
print(sayac) #3
demet = ("a", "b", "c", "d", "e", "f", "g")
y = list(demet)
y[1] = "h"
demet = tuple(y)
print(demet) #("a", "h", "c", "d", "e", "f", "g")
#kopyalamak ve çoğaltmak
demet = ("a", "b", "c", "d", "e", "f", "g")
yenidemet = tuple(demet)
print(yenidemet) #("a", "b", "c", "d", "e", "f", "g")
#print(demet) yazarak da aynı sonuca ulaşabiliriz.
#demet birleştirme
demet1 = ("a", "b", "c")
demet2 = ("D", "E")
demet3 = demet1 + demet2
print(demet3) #("a", "b", "c", "D", "E")
#bir elemanın indexini bulmak

#bir elemanın varlığını kontrol etmek
demet = ("a", "b", "c", "d", "e", "f", "g")
if "h" in demet: 
    print("evet")
else:
    print("hayır")
#demetlerin listelerle olan farkları;
#genellikle farklı veri türleri için tanımlama grupları ve benzer veri türleri için listeler kullanılır.
#demetler değişmez olduğu için demet üzerinden yineleme yapmak listeden daha hızlıdır.
#değişmez öğeler içeren demetler sözlük olarak da kullanılabilirler.
#değişmeyen verileri demet olarak uygulamak, yazmaya karşı korumalı olunmasını sağlar.