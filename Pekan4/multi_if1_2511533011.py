umur = int(input("input umur anda : "))
sim = input("Apakah anda sudah punya sim C (y/t) : ")[0]

if umur >= 17 and sim == 'y' :
    print("Anda sudah dewasa dan boleh bawa motor")

if umur >= 17 and sim != 'y' :
    print("Anda suda dewasa tetapi tidak boleh membawa motor")

if umur < 17 and sim == 'y' :
    print("Anda belum cukup umur tetapi sudah memiliki sim")

if umur < 17 and sim != 'y' :
    print("Anda belum cukup umur dan tidak boleh membawa motor")