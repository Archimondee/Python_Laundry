from mysql.connector import MySQLConnection, Error
from iniConfig import bacaConfig
import re
import menuAdmin
import getpass
def cekNama(user):
    try:
        dbConfig = bacaConfig()
        conn = MySQLConnection(**dbConfig)
        query = conn.cursor()
        query.execute("SELECT * FROM user")

        rows = query.fetchall()
        a = []
        b = 0
        c = 0
        stop = "true"
        terdaftar = "True"

        for row in rows:
            a.insert(b,row[1])
            b += 1
            
        while stop == 'true' and c < len(a):
            if a[c] == user:
                terdaftar = "True"
                stop = "false"
            else:
                terdaftar = "false"
                stop = "true"
            c += 1
            
        if terdaftar == "True":
            print "Maaf sudah terdaftar"
            registNama()
        else:
            print "Dapat digunakan"
            dataDiri(user)
            
    except Error as e:
        print (e)
def registNama():
    user = raw_input("Masukan username :")
    if re.match('^[A-Za-z]*$',user):
        cekNama(user)
    else:
        print 'Tidak dapat menggunakan angka'
        registNama()

def dataDiri(user):
    pswd = getpass.getpass('Masukan password : ',stream = None)

    akses = "Anggota"
    alamat = raw_input("Masukan alamat valid : ")
    hp = input("Masukan nomor hp valid : ")    
    email = raw_input("Masukan email valid : ")
    saldo = 10000
    query = "INSERT INTO user (user,pswd,akses,saldo,alamat,hp,email)"\
            "VALUES (%s,%s,%s,%s,%s,%s,%s)"
    args = (user,pswd,akses,saldo,alamat,hp,email)

    try:
        dbConfig = bacaConfig()
        conn = MySQLConnection(**dbConfig)

        cursor = conn.cursor()
        cursor.execute(query,args)

        nilaiId = 100000
        if cursor.lastrowid:
            print('Sukses mendaftar')
        else:
            print("Last insert id not found")

        conn.commit()
        
    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close

if __name__ == '__main__':
    registNama()
