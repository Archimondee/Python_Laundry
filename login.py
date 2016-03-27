from iniConfig import bacaConfig
from mysql.connector import MySQLConnection, Error

def cekMasuk(user,pswd):
    try:
        dbConfig = bacaConfig()
        conn = MySQLConnection(**dbConfig)
        query = conn.cursor()
        query.execute("SELECT * FROM user")

        rows = query.fetchall()

        cekNama = []
        cekPswd = []
        cekAkses = []
        itNama = 0
        itPswd = 0
        itAkses = 0
        c = 0
        stop = "berhenti"
        for row in rows:
            cekNama.insert(itNama,row[1])
            cekPswd.insert(itPswd,row[2])
            cekAkses.insert(itAkses,row[3])

            itNama += 1
            itPswd += 1
            itAkses += 1

        while stop == "berhenti" and c < len(cekNama):
            if cekNama[c] == user and cekPswd[c] == pswd:
                if cekAkses[c] == 'Admin':
                    print 'Saya admin'
                else:
                    print 'Saya anggota'
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
    pswd = raw_input("Masukan password : ")
    cekMasuk(user,pswd)
