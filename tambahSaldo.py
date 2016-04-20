from iniConfig import bacaConfig
from mysql.connector import MySQLConnection, Error
def saldoTambah(saldo_user,fix_update,user):
    try:
        dbConfig = bacaConfig()
        conn = MySQLConnection(**dbConfig)
        query = conn.cursor()
        query.execute("SELECT * from user")
        rows = query.fetchall()
        f_user1 = []
        a = 0
        b = 0
        f_iter = 0
        stop = "True"
        terdaftar = "True"
        for row in rows:
            f_user1.insert(a,row[1])
            a += 1
        while stop == "True" and f_iter < len(f_user1):
            if f_user1[f_iter] == user:
                terdaftar = "True"
                stop = "False"
            else:
                terdaftar = "False"
                stop = "True"
            f_iter += 1
        if terdaftar == "False":
            print "User tidak ditemukan"
            saldoTambah()
        else:
            print "User ditemukan"
            saldo = input("Masukan jumlah saldo : ")
            fix_total = saldo + saldo_user - fix_update
            try:
                
                dbConfig1 = bacaConfig()
                conn1 = MySQLConnection(**dbConfig1)
                query = conn1.cursor()
                query1 = "UPDATE user SET saldo = %s WHERE user = %s"
                data1 = (fix_total,user)
                query.execute(query1,data1)
                conn1.commit()
            except Error as e:
                print (e)
    except Error as e:
        print (e)
