class Mahasiswa():
    def __init__(self, nama, nim, alamat, jurusan, gender, perangkat, foto):
        self.nama = nama
        self.nim = nim
        self.alamat = alamat
        self.jurusan = jurusan
        self.gender = gender
        self.perangkat = perangkat
        self.foto = foto

    def get_nama(self):
        return self.nama

    def get_nim(self):
        return self.nim

    def get_alamat(self):
        return self.alamat

    def get_jurusan(self):
        return self.jurusan

    def get_gender(self):
        return self.gender

    def get_perangkat(self):
        return self.perangkat

    def get_foto(self):
        return self.foto