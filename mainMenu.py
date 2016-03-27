from register import registNama
from login import loginNama

def mainMenu():
    print '1. Login '
    print '2. Register'
    print '3. Checking laundry with ID'
    pilih = input('Masukan pilihan anda : ')

    if pilih == 1:
        loginNama()
    elif pilih == 2:
        registNama()
    elif pilih == 3:
        print 'Menu belum tersedia'
    else:
        print 'Input error'
        
        

if __name__ == '__main__':
    mainMenu()
