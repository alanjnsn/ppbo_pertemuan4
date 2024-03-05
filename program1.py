class Orang:
    def __init__(self,nama_depan,nama_belakang,ID):
        self.nama_depan=nama_depan
        self.nama_belakang=nama_belakang
        self.ID=ID



class Mahasiswa(Orang):
    SARJANA,MASTER,DOKTOR= range(3)
    def __init__(self, nama_depan, nama_belakang, ID, jenjang):
        super().__init__(nama_depan, nama_belakang, ID)
        self.jenjang=jenjang
        self.matkul=[]

    def enrol(self,addmatkul):
        self.matkul.append(addmatkul)


class Karyawan(Orang):
    TETAP,TDK_TETAP= range(2)
    def __init__(self, nama_depan, nama_belakang, ID, status):
        super().__init__(nama_depan, nama_belakang, ID)
        self.status= status

    
class Dosen(Karyawan):
    def __init__(self, nama_depan, nama_belakang, ID, status):
        super().__init__(nama_depan, nama_belakang, ID, status)
        self.matkul_diajar=[]

    def mengajar(self,addmatkul):
        self.matkul_diajar.append(addmatkul)
    

bowo= Mahasiswa('Bowo',"Nugroho",987654,Mahasiswa.SARJANA)
bowo.enrol('Basis Data')

rizki= Dosen('Rizki','Setiabudi',456789,Karyawan.TETAP)
rizki.mengajar('Statistik')

print(bowo.__dict__)
print(rizki.__dict__)