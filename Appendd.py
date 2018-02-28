nm = []
n = []
tu = []
ut = []
ua = []
stop = False
no = 0
while (not stop) :
    na = raw_input("Nama\t\t: ")
    nm.append(na)
    nim = input("NIM\t\t: ")
    n.append(nim)
    nilai_tugas = input("Nilai Tugas\t: ")
    tu.append(nilai_tugas)
    nilai_uts = input("Nilai UTS\t: ")
    ut.append(nilai_uts)
    nilai_uas = input("Nilai UAS\t: ")
    ua.append(nilai_uas)

    data = raw_input("Tambah Data (y/t)? ")
    if(data == "t"):
        stop = True
    akhir = (nilai_tugas+nilai_uts+nilai_uas)/3
    no += 1


print "=============================================================="
print " No | Nama | NIM  | Tugas  | UTS  | UAS  | Akhir "
print "==============================================================="
print " ",no, "| ", na, " | ", nim, " | ", nilai_tugas, " | ", nilai_uts, " | ", nilai_uas, " | ", akhir, " "
print " ",no, "| ", na, " | ", nim, " | ", nilai_tugas, " | ", nilai_uts, " | ", nilai_uas, " | ", akhir, " "
