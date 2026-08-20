library = [
    ("Kürk Mantolu Madonna","Sebahattin Ali"),
    ("İçimizdeki Şeytan","Sebahattin Ali"),
    ("Tutunamayanlar","Oğuz Atay"),
    ("Çalıkuşu","Reşat Nuri Güntekin"),
    ("Suç ve Ceza","Dostoevsky"),
    ("Savaş ve Barış","Tolstoy"),
    ("Kuyucaklı Yusuf","Sebahattin Ali"),
    ("Malcom X","Alex Haley"),
    ("Sefiller","Victor Hugo")
]

menu = ["Kitap Ekle", "Kitap Çıkar", "Kitapları Listele", "Çıkış"]

operation = 0
while operation != 4:
  y = 1
  for x in menu:
    print(y,".",x)
    y += 1
  operation = int(input("Lütfen yapmak istediğiniz işlem numarasını giriniz: "))
  if operation == 1:
    newBookName = input("Eklemek istediğiniz kitabın adını giriniz: ")
    newBookAuthor = input("Eklemek istediğiniz kitabın yazarını adını giriniz: ")
    book = (newBookName, newBookAuthor)
    if book not in library:
      library.append(book)
      print(newBookName,"kitabı listeye eklendi")
    else:
      print("Bu kitap zaten kütüphanede kayıtlı.")
  elif operation == 2:
      searchAuthor = input("Lütfen almak istediğiniz kitabın yazarını giriniz: ").casefold()
      foundBooks = []
      z = 1
      for book in library:
        if book[1].casefold() == searchAuthor:
          print(z,".",book[0])
          foundBooks.append(book)
          z += 1
      if len(foundBooks) == 0:
        print("Bu yazara ait kitap bulunamadı!")
      else:
        selectedBook = int(input("Lütfen almak istediğiniz kitabın numarasını giriniz: "))
        if selectedBook<1 or selectedBook > len(foundBooks):
          print("Geçersiz seçim.")
        else:
          library.remove(foundBooks[selectedBook - 1])
          print(foundBooks[selectedBook - 1][0],"adlı kitabı aldınız. İyi okumalar.")
  elif operation == 3:
    a = 1
    for book in library:
      print(a,".", book[0] , "," , book[1])
      a += 1
    print("\n")
