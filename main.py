print("-welcome to CV generator program-")


isim=input("adınız nedir?")
while True:
  yas=int(input("yaşınız nedir?"))
  if 0<yas<1000:
    break
  else:
    print("tekrar dene")
eğitim=input("hangi üniversiteden mezunsunuz?")
mail=input("mailinizi giriniz:")
def cv_metni():
  metin=f"""
  ---//CV\\---
  name:{isim}
  age:{yas}
  Email:{mail}
  Education:{eğitim}
  """
  return metin
içerik=cv_metni()
print(içerik)
with open("cv.txt","w") as filecv:
  filecv.write(içerik)



