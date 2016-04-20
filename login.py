from iniConfig import bacaConfig
from mysql.connector import MySQLConnection, Error
from menuAdmin import daftarMenuAdmin
import re
def cekMasuk(user,pswd):
    try:
        dbConfig = bacaConfig()
        conn = MySQLConnection(**dbConfig)
        query = conn.cursor()
        query.execute("SELECT * FROM user")

        rows = query.fetchall()

        #cek mysql dan dimasukan kedalam array
        cekNama = []
        cekPswd = []
        cekAkses = []
        cekEmail = []
        cekAlamat = []
        cekHP = []

        #iterasi pengulangan
        itNama = 0
        itPswd = 0
        itAkses = 0
        itEmail = 0
        itAlamat = 0
        ithp = 0
        itSaldo = 0
        
        c = 0
        stop = "berhenti"
        for row in rows:
            cekNama.insert(itNama,row[1])
            cekPswd.insert(itPswd,row[2])
            cekAkses.insert(itAkses,row[3])
            cekSaldo.insert(itSaldo,row[4])
            cekEmail.insert(itEmail,row[5])
            cekAlamat.insert(itAlamat,row[7])
            cekHP.insert(ithp, row[6])

            itNama += 1
            itPswd += 1
            itAkses += 1
            ithp += 1
            itEmail +=1
            itAlamat += 1
            itSaldo += 1

        while stop == "berhenti" and c < len(cekNama):
            if cekNama[c] == user and cekPswd[c] == pswd:
                if cekAkses[c] == 'Admin':
                    nama = cekNama[c]
                    pswd = cekPswd[c]
                    auth = cekAkses[c]
                    email = cekEmail[c]
                    alamat = cekAlamat[c]
                    handphone = cekHP[c]
                    daftarMenuAdmin()
                else:
                    nama = cekNama[c]
                    pswd = cekPswd[c]
                    auth = cekAkses[c]
                    email = cekEmail[c]
                    alamat = cekAlamat[c]
                    handphone = cekHP[c]
                    #menuAnggota()
                auth = "True"
                stop = "lanjut"
            else:
                auth = "False"
                stop = "berhenti"
                
            c += 1

        if auth == "True":
            print "Silahkan masuk"
            
        else:
            print "Gagal login"
            loginNama()

    except Error as e:
        print(e)

def loginNama():
    user = raw_input("Masukan nama : ")
    if re.match('^[A-Za-z]*$',user):
        pswd = raw_input("Masukan password : ")
        cekMasuk(user,pswd)
    else:
        print 'Tidak boleh menggunakan angka'
        loginNama()
