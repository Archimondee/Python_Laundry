import time
import sys
class Parkir(object):
    jumlah = 1
    def __init__(self):
        self.motor = 30
        self.mobil = 10
        #self.jumlah = 1
        self.nopol = []
        self.jenis = []
        self.waktu_jam = []
        self.waktu_menit = []
        a = []
        for b in time.localtime():
            a.append(b)
        self.masuk_jam = a[3]
        self.masuk_menit = a[4]
        #self.nopol = ""
        #self.jenis = ""

    def kendaraan_masuk(self):
        print ""
        print "---- Selamat Datang ----"
        print "Pilih kendaraan : "
        print "1. Mobil"
        print "2. Motor"
        print "Silahkan pilih jenis kendaraan"
        masuk = raw_input("> ")
        if masuk in ('mobil',"1","Mobil"):
            #self.nopol = pol #Nomor polisi
            #self.kendaraan["jenis"] = "Mobil" #Jenis kendaraan
            #self.kendaraan["nopol"] = pol #Nomor polisi
            #self.kendaraan["waktu"] = self.masuk #Waktu kendaraan masuk
            self.mobil -= 1
            if self.mobil <= 0:
                print "Parkiran untuk mobil penuh"
                print "Segera kembali ke menu parkiran"
                Parkir()

            else:
                print "Masukan Nomor Polisi Kendaraan :"
                pol = raw_input("> ")
                self.nopol.append(pol)
                self.jenis.append("Mobil")
                self.waktu_jam.append(self.masuk_jam)
                self.waktu_menit.append(self.masuk_menit)
                print "Data berhasil disimpan"
                print "Kembali ke menu parkiran"
                print ""
                raw_input()
                Parkir() #kembali ke kelas parkir

        elif masuk in ("motor","2","Motor"):
            #self.kendaraan["jenis"] = "Motor"
            #self.kendaraan["nopol"] = pol
            #self.kendaraan["waktu"] = self.masuk
            self.motor -= 1
            if self.motor <= 0:
                print "Parkiran untuk motor penuh"
                print "Segera kembali ke menu parkiran"
                Parkir() #kembali ke menu parkir
            else:
                print "Masukan Nomor Polisi Kendaraan :"
                pol = raw_input("> ")
                self.nopol.append(pol)
                self.jenis.append("Motor")
                self.waktu_jam.append(self.masuk_jam)
                self.waktu_menit.append(self.masuk_menit)
                print "Data berhasil disimpan"
                print "Kembali ke menu parkiran"
                print ""
                raw_input()
                Parkir()
        else:
            print "Tak ada pilihan tersebut"
            Parkir.kendaraan_masuk(self) #jika salah input

    def kendaraan_keluar(self):
        print ""
        print "---- Selamat datang ----"
        print "Silahkan masukan Nomor Polisinya : "
        out_pol = raw_input("> ")
        benar = "False"
        b = 0
        print len(self.nopol)
        print self.nopol[0]
        while benar == "False" and b <= len(self.nopol):
            if out_pol == self.nopol[b]:
                right = "False"
                benar = "True"
                print "Informasi kendaraan dengan Nopol", out_pol
                print "No. Polisi:",self.nopol[b]
                print "Jenis Kendaraan:",self.jenis[b]
                print "Waktu Masuk:",self.waktu_jam[b], ":", self.waktu_menit[b]
                #in_jam = self.waktu_jam[b]
                #in_menit = self.waktu_menit[b]
                out_jam = []
                out_menit = []
                for x in time.localtime():
                    out_jam.append(x)
                    out_menit.append(x)
                print "Waktu Keluar:",self.waktu_jam[b],":",self.waktu_menit[b]
                keluar_jam = out_jam[3] - self.waktu_jam[b]
                keluar_menit = out_menit[4] - self.waktu_menit[b]
                #print keluar_jam,keluar_menit
                if keluar_menit < 0:
                    keluar_jam -= 1

                if self.jenis[b] == "Mobil":
                    biaya = 3000
                    if keluar_jam <= 2:
                        biaya = 3000
                    elif keluar_jam >= 3:
                        for u in range(3,keluar_jam,1):
                            biaya += 2500
                    else:
                        pass
                    print "Total Parkir : Rp.",biaya
                    print "Kembali ke menu parkir"
                    raw_input()
                    self.mobil += 1 #menambahkan angka 1 ke kendaraan motor
                    Parkir()
                elif self.jenis[b] == "Motor":
                    biaya = 2000
                    if keluar_jam <= 2:
                        biaya = 2000
                    elif keluar_jam >= 3:
                        biaya = 1500
                    else:
                        pass
                    print "Total Parkir : Rp.",biaya
                    print "Kembali ke menu parkir"
                    raw_input()
                    self.motor += 1 #Menambahkan angka 1 ke kendaraan motor
                    Parkir()
                else:
                    pass
            else:
                benar = "False"
                print "Tidak ada kendaraan dengan Nopol",out_pol
            b+=1


if __name__ == '__main__':
    coba = Parkir()
    while True:
        print "---- Selamat Datang ----"
        print "Silahkan pilih menu berikut : "
        print "1. Parkir kendaraan masuk"
        print "2. Parkir kendaraan keluar"
        print "3. Keluar"
        pil = raw_input("> ")
        if pil in ("1","masuk","Masuk","parkir"):
            coba.kendaraan_masuk()
        elif pil in ("2","keluar","Keluar","Keluar Parkir"):
            coba.kendaraan_keluar()
        elif pil in ("3","exit"):
            sys.exit(1)
        else:
            print "Tidak pilihan berikut"
            Parkir()