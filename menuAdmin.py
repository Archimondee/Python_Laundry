from iniConfig import bacaConfig
import string
import random
from tambahSaldo import saldoTambah
from mysql.connector import MySQLConnection, Error
def daftarMenuAdmin():
    print '################################################'
    print '#                Menu Admin                    #'
    print '#        1. Input laundry'
    print '#        2. Update laundry'
    print '#        3. Cek laundry'
    adminPil = input('Masukan angka untuk ke menu : ')
    if adminPil == 1:
        inputLaundry()
    else:
        print "test"
    print '#################################################'
def inputLaundry():
    user = raw_input('Masukan username :')
    try:
        dbConfig = bacaConfig()
        conn = MySQLConnection(**dbConfig)
        query = conn.cursor()
        query.execute("SELECT * FROM user")
        rows = query.fetchall()
        f_user = []
        f_iterasi = 0
        f_saldo = []
        saldo_iter = 0
        c = 0
        d = 0
        saldo_user = 0
        stop = "True"
        terdaftar = "True"

        for row in rows:
            f_user.insert(c,row[1])
            f_saldo.insert(c,row[4])
            c += 1
        while stop == 'True' and f_iterasi < len(f_user):
            if f_user[f_iterasi] == user:
                terdaftar = "True"
                stop = "False"
                saldo_user = f_saldo[f_iterasi]
            else:
                terdaftar = "False"
                stop = "True"
            f_iterasi += 1

        if terdaftar == "False":
            print "User tidak ditermukan"
            inputLaundry()
        else:
            print "User ditemukan"
            print "Username : ",user
            print "Saldo : ",saldo_user
            data_laundry(user,saldo_user)
    except Error as e:
        print (e)

    finally:
        query.close()
        conn.close()


def data_laundry(user,saldo_user):
    kodeLau = randomTiket()
    total = 0
    status = ""
    print '1. Cuci laundry'
    print '2. Cuci laundry + setrika'
    print '3. Cuci laundry + setrika + delivery'
    pilLaundry = input('Masukan pilihan : ')
    berat = input('Masukan berat pakaian : ')
    if pilLaundry == 1 :
        total = 5000 * berat
    elif pilLaundry == 2:
        total = 7000 * berat
    elif pilLaundry == 3:
        total = 7000 * berat + 3000

    fix_update = saldo_user - total
    if fix_update < 0:
        status = "Lunas"
        print "Saldo anda tidak mencukupi"
        tambah_saldo = raw_input("Ingin menambah saldo anda ? ")
        if tambah_saldo == 'y' or 'Y' or 'Ya' or 'YA' or 'ya':
            saldoTambah(saldo_user,fix_update,user)
    else:
        status = "Lunas"
        query1 = "INSERT INTO data_user (kodeLau,user,status,total)"\
             "VALUES(%s,%s,%s,%s)"
        args1 = (kodeLau,user,status,total)

        try:
            dbConfig = bacaConfig()
            connection = MySQLConnection(**dbConfig)
            query = connection.cursor()
            query.execute(query1,args1)
        
            if query.lastrowid:
                print "Data laundry berhasil dimasukan"
                query2 = "UPDATE user SET saldo = %s WHERE user = %s"
                data2 = (fix_update,user)
                try:
                    dbConfig = bacaConfig()
                    conn2 = MySQLConnection(**dbConfig)
                    cursor2 = conn2.cursor()
                    cursor2.execute(query2,data2)
                    conn2.commit()
                except Error as e:
                    print (e)
                finally:
                    cursor2.close()
                    conn2.close()
            else:
                print "Gagal menginput"
            connection.commit()

        except Error as e:
            print (e)

        finally:
            query.close()
        connection.close()
    
def randomTiket(size=10, chars=string.ascii_uppercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))    
    
if __name__ == '__main__':
    daftarMenuAdmin()
