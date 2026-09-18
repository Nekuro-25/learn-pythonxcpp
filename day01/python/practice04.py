#Data
anggur = int(input("Berapa kilogram anggur yang akan difermentasi? Minimal 10 : "))
anggur_matang = int(input("Berapa hari agar anggur matang dan siap difermentasi? : "))
proses = int(input("Berapa hari proses fermentasi? : "))

#Proses_anggur
anggur_minum = int(anggur_matang + proses + (anggur / 10))

print(f"Anggur yang akan difermentasi sebanyak {anggur} kg. Namun, anggur tersebut masih mentah dan butuh {anggur_matang} hari lagi untuk matang, ditambah lagi proses fermentasi memakan waktu sampai {proses} hari. Sehingga anggur siap dipasarkan minimal dalam {anggur_minum} hari lagi")
