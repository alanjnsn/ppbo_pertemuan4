class Orang:
    def __init__(self,nama_depan,nama_belakang,ID):
        self.nama_depan=nama_depan
        self.nama_belakang=nama_belakang
        self.ID=ID


class Pelajar:
    def __init__(self):
        self.matkul=[]

    def enrol(self,addmatkul):
        self.matkul.append(addmatkul)


class Pengajar:
    def __init__(self):
        self.matkul_diajar=[]

    def mengajar(self,addmatkul):
        self.matkul_diajar.append(addmatkul)


class Asdos(Orang,Pelajar,Pengajar):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.matkul=[]
        self.matkul_diajar=[]

uswatun= Asdos('Uswatun','Hasanah',456456)
uswatun.enrol('Big Data')
uswatun.mengajar('Kecerdasan Artifisial')
print(uswatun.__dict__)
