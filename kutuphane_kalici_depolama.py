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
    book = newBookName + ";" + newBookAuthor
    with open("library.txt", "r") as f:
      data = f.readlines()
    if book not in data:
      with open("library.txt", "a") as f:
        f.write(book + "\n")
      print(newBookName,"kitabı listeye eklendi")
    else:
      print("Bu kitap zaten kütüphanede kayıtlı.")
  elif operation == 2:
      searchAuthor = input("Lütfen almak istediğiniz kitabın yazarını giriniz: ").casefold()
      foundBooks = []
      z = 1

      with open("library.txt", "r") as f:
        data = f.readlines()

      for book in data:
        parts = book.strip().split(";")

        if len(parts) == 2:
          name, author = parts

          if author.casefold() == searchAuthor:
            print(z, ".", name)
            foundBooks.append(book)
            z += 1

      if len(foundBooks) == 0:
        print("Bu yazara ait kitap bulunamadı!")
      else:
        selectedBook = int(input("Lütfen almak istediğiniz kitabın numarasını giriniz: "))

        if selectedBook<1 or selectedBook > len(foundBooks):
          print("Geçersiz seçim.")
        else:
          with open("library.txt", "r") as f:
            data = f.readlines()

          with open("library.txt", "w") as f:
            for line in data:
              if line.strip() != foundBooks[selectedBook - 1].strip():
                f.write(line)
          name = foundBooks[selectedBook - 1].split(";")[0]
          print(name,"adlı kitabı aldınız. İyi okumalar.")
  elif operation == 3:
    with open("library.txt", "r") as f:
      data = f.read()
    print(data)
