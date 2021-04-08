from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from mahasiswa import Mahasiswa

mahasiswa = []
foto_file = ""

root = Tk()
root.title("TP3 Praktikum DPBO Python")

def inputs():
    # Hide root window
    global root
    root.withdraw()

    # Reset global var
    global foto_file
    foto_file = ""

    top = Toplevel()
    top.title("Input")
    dframe = LabelFrame(top, text="Input Data Mahasiswa", padx=10, pady=10)
    dframe.pack(padx=10, pady=10)
    # Input 1
    label1 = Label(dframe, text="Nama Mahasiswa").grid(row=0, column=0, sticky="w")
    input1 = Entry(dframe, width=30)
    input1.grid(row=0, column=1, padx=20, pady=10, sticky="w")
    # Input 2
    label2 = Label(dframe, text="NIM").grid(row=1, column=0, sticky="w")
    input2 = Entry(dframe, width=30)
    input2.grid(row=1, column=1, padx=20, pady=10, sticky="w")
    # Input 3
    label3 = Label(dframe, text="Alamat").grid(row=2, column=0, sticky="w")
    input3 = Entry(dframe, width=30)
    input3.grid(row=2, column=1, padx=20, pady=10, sticky="w")
    # Input 4
    options = ["Filsafat Meme", "Sastra Mesin", "Teknik Kedokteran", "Pendidikan Gaming"]
    jurusanVar = StringVar(root)
    jurusanVar.set(options[0])
    label4 = Label(dframe, text="Jurusan").grid(row=3, column=0, sticky="w")
    input4 = OptionMenu(dframe, jurusanVar, *options)
    input4.grid(row=3, column=1, padx=20, pady=10, sticky='w')

    # Input 5 Radio Button
    label5 = Label(dframe, text="Gender").grid(row=4, column=0, sticky="w")
    radioFrame = LabelFrame(dframe, borderwidth=0)
    radioFrame.grid(row=4, column=1, padx=20, sticky="w")

    v = StringVar(radioFrame)
    radio1 = Radiobutton(radioFrame, text="Laki-Laki", variable=v, value="Laki-Laki")
    radio1.grid(row=0, column=0, sticky="w")

    radio2 = Radiobutton(radioFrame, text="Perempuan", variable=v, value="Perempuan")
    radio2.grid(row=0, column=1, sticky="w")

    # Input 6 Check Button
    label6 = Label(dframe, text="Perangkat").grid(row=5, column=0, sticky="w")
    cbframe = LabelFrame(dframe, borderwidth=0)
    cbframe.grid(row=5, column=1, padx=20, sticky="w")

    perangkat = []

    Checkbutton1 = IntVar()  
    Checkbutton2 = IntVar()  
    Checkbutton3 = IntVar()

    cb1 = Checkbutton(cbframe, text = "PC", 
                      variable = Checkbutton1,
                      height = 2,
                      width = 10)
    cb1.grid(row=0, column=0, sticky="w", pady=0)

    cb2 = Checkbutton(cbframe, text = "Laptop", 
                      variable = Checkbutton2,
                      height = 2,
                      width = 10)
    cb2.grid(row=0, column=1, sticky="w", pady=0)

    cb3 = Checkbutton(cbframe, text = "HP", 
                      variable = Checkbutton3,
                      height = 2,
                      width = 10)
    cb3.grid(row=0, column=2, sticky="w", pady=0)

    perangkat.append(Checkbutton1)
    perangkat.append(Checkbutton2)
    perangkat.append(Checkbutton3)

    # Input 7 Insert Image Button
    label7 = Label(dframe, text="Foto").grid(row=6, column=0, sticky="w")
    insImgFrame = LabelFrame(dframe, borderwidth=0)
    insImgFrame.grid(row=6, column=1, padx=20, sticky="w")
    # Browse files button
    btnFile = Button(insImgFrame, text="Pilih Foto", command=lambda:browseFiles(insImgFrame)).grid(row=0, column=0, sticky="w")
    # Selected file label
    labelSelected = Label(insImgFrame, text="Belum ada yang dipilih.").grid(row=0, column=1, sticky="w")

    # Button Frame
    frame2 = LabelFrame(dframe, borderwidth=0)
    frame2.grid(columnspan=2, column=0, row=10, pady=10)

    # Submit Button
    btn_submit = Button(frame2, text="Submit Data", anchor="s", command=lambda:[insertData(top, input1, input2, input3, jurusanVar, v, perangkat, foto_file), top.withdraw()])
    btn_submit.grid(row=5, column=0, padx=10)

    # Cancel Button
    btn_cancel = Button(frame2, text="Gak jadi / Kembali", anchor="s", command=lambda:[top.destroy(), root.deiconify()])
    btn_cancel.grid(row=5, column=1, padx=10)

def browseFiles(parent):
    global foto_file
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Pilih Fotonya ngab",
                                          filetypes = (("Image files",
                                                        "*.jpg *.jpeg *.png *.gif"),
                                                       ("all files",
                                                        "*.*")))  
    labelSelected = Label(parent, text=filename).grid(row=0, column=1, sticky="w")
    foto_file = filename

def insertData(parent, nama, nim, alamat, jurusan, gender, perangkats, foto):
    top = Toplevel()
    # Get data
    nama = nama.get()
    nim = nim.get()
    alamat = alamat.get()
    jurusan = jurusan.get()
    gender = gender.get()
    perangkat = []
    if(perangkats[0].get() == 1): 
        perangkat.append("PC")
    if(perangkats[1].get() == 1): 
        perangkat.append("Laptop")
    if(perangkats[2].get() == 1): 
        perangkat.append("HP")

    if(nama != "" and nim != "" and alamat != "" and gender != "") :
        # Append to array
        mahasiswa.append(Mahasiswa(nama, nim, alamat, jurusan, gender, perangkat, foto))

        top.title("Berhasil gan")
        lbl = Label(top, text="Data Berhasil ditambahkan", fg="green")
        lbl.pack(padx=40, pady=20)

        btn_ok = Button(top, text="Siap ngab", anchor="s", command=lambda:[top.destroy(), parent.deiconify()])
        btn_ok.pack(padx=10, pady=10)

    else :
        top.title("Gaboleh gitu gan")
        lbl = Label(top, text="Nama, NIM, Alamat, dan Gender harus diisi", fg="red")
        lbl.pack(padx=40, pady=20)

        btn_ok = Button(top, text="Siap ngab", anchor="s", command=lambda:[top.destroy(), parent.deiconify()])
        btn_ok.pack(padx=10, pady=10)
      
def about():
    top = Toplevel()
    top.title("About")

    d_frame = LabelFrame(top, text="Deskripsi Aplikasi", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    label = Label(d_frame, text="Aplikasi Database Mahasiswa", anchor="w").grid(row=0, column=0, sticky="w")
    label = Label(d_frame, text="Ceritanya sih buat nyimpen data mahasiswa seperti database gitu. Database Mahasiswa DIY.", anchor="w").grid(row=1, column=0, sticky="w")
    label = Label(d_frame, text="Creator : Muhammad Fajar Yusuf Firdaus", anchor="w").grid(row=2, column=0, sticky="w")

    b_exit = Button(d_frame, text="Back", command=top.destroy)
    b_exit.grid(row=4, column=1)

def viewAll():
    global root
    root.withdraw()

    top = Toplevel()
    top.title("Semua Mahasiswa")
    frame = LabelFrame(top, borderwidth=0)
    frame.pack()
    # Cancel Button
    btn_cancel = Button(frame, text="Kembali", anchor="w", command=lambda:[top.destroy(), root.deiconify()])
    btn_cancel.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    # Head title
    head = Label(frame, text="Data Mahasiswa")
    head.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    tableFrame = LabelFrame(frame)
    tableFrame.grid(row=1, column = 0, columnspan=2)

    # Title
    title1 = Label(tableFrame, text="No.", borderwidth=1, relief="solid", width=3, padx=5).grid(row=0, column=0)
    title2 = Label(tableFrame, text="Nama", borderwidth=1, relief="solid", width=20, padx=5).grid(row=0, column=1)
    title3 = Label(tableFrame, text="NIM", borderwidth=1, relief="solid", width=15, padx=5).grid(row=0, column=2)
    title4 = Label(tableFrame, text="Alamat", borderwidth=1, relief="solid", width=25, padx=5).grid(row=0, column=3)
    title5 = Label(tableFrame, text="Jurusan", borderwidth=1, relief="solid", width=10, padx=5).grid(row=0, column=4)
    title6 = Label(tableFrame, text="Gender", borderwidth=1, relief="solid", width=10, padx=5).grid(row=0, column=5)
    title7 = Label(tableFrame, text="Perangkat", borderwidth=1, relief="solid", width=10, padx=5).grid(row=0, column=6)
    title8 = Label(tableFrame, text="Foto", borderwidth=1, relief="solid", width=10, padx=5).grid(row=0, column=7)

    # Print content
    i = 0
    for data in mahasiswa:
        label1 = Label(tableFrame, text=str(i+1), borderwidth=1, relief="solid", height=2, width=3, padx=5).grid(row=i+1, column=0)
        label2 = Label(tableFrame, text=data.get_nama(), borderwidth=1, relief="solid", height=2, width=20, padx=5).grid(row=i+1, column=1)
        label3 = Label(tableFrame, text=data.get_nim(), borderwidth=1, relief="solid", height=2, width=15, padx=5).grid(row=i+1, column=2)
        label4 = Label(tableFrame, text=data.get_alamat(), borderwidth=1, relief="solid", height=2, width=25, padx=5).grid(row=i+1, column=3)
        label5 = Label(tableFrame, text=data.get_jurusan(), borderwidth=1, relief="solid", height=2, width=10, padx=5).grid(row=i+1, column=4)
        label6 = Label(tableFrame, text=data.get_gender(), borderwidth=1, relief="solid", height=2, width=10, padx=5).grid(row=i+1, column=5)
        label7 = Label(tableFrame, text=data.get_perangkat(), borderwidth=1, relief="solid", height=2, width=10, padx=5).grid(row=i+1, column=6)
        view = Button(tableFrame, text="Lihat Foto", height=1, width=7, padx=5, command=lambda index=i: viewPic(index)).grid(row=i+1, column=7)
        i += 1

def viewPic(i):
    top = Toplevel()
    top.title("Lihat Gambar")
    # Get path
    path = mahasiswa[i].get_foto()

    canvas = Canvas(top, width = 300, height = 300)  
    canvas.grid(columnspan=3)
    if(path != "") :
        img = Image.open(path)
        img = ImageTk.PhotoImage(img)
        img_lbl = Label(canvas, image=img)
        img_lbl.image = img
        img_lbl.grid(column=1, row=0)
    else :
        lbl = Label(canvas, text="Gaada gambarnya ngab")
        lbl.grid(column=1, row=0, padx=30, pady=30)

def clearAll():
    top = Toplevel()
    lbl = Label(top, text="Yakin mau hapus semua data?")
    lbl.pack(padx=20, pady=20)
    btnframe = LabelFrame(top, borderwidth=0)
    btnframe.pack(padx=20, pady=20)
    # Yes
    btn_yes = Button(btnframe, text="Gass", bg="green", fg="white", command=lambda:[top.destroy(), delAll()])
    btn_yes.grid(row=0, column=0, padx=10)
    # No
    btn_no = Button(btnframe, text="Tapi boong", bg="red", fg="white", command=top.destroy)
    btn_no.grid(row=0, column=1, padx=10)

def exitDialog():
    global root
    root.withdraw()
    top = Toplevel()
    lbl = Label(top, text="Yakin mau keluar?")
    lbl.pack(padx=20, pady=20)
    btnframe = LabelFrame(top, borderwidth=0)
    btnframe.pack(padx=20, pady=20)
    # Yes
    btn_yes = Button(btnframe, text="Gass", bg="green", fg="white", command=lambda:[top.destroy(), root.destroy()])
    btn_yes.grid(row=0, column=0, padx=10)
    # No
    btn_no = Button(btnframe, text="Tapi boong", bg="red", fg="white", command=lambda:[top.destroy(), root.deiconify()])
    btn_no.grid(row=0, column=1, padx=10)

def delAll():
    mahasiswa.clear()

    top = Toplevel()
    top.title("Berhasil")
    lbl = Label(top, text="Datanya sudah dihapus semua ngab")
    lbl.pack(padx=30, pady=10)
    btn_no = Button(top, text="Zeeb", command=top.destroy)
    btn_no.pack(pady=20)

# Title Frame
frame = LabelFrame(root, text="TP3", padx=10, pady=10)
frame.pack(padx=10, pady=10)

# ButtonGroup Frame
buttonGroup = LabelFrame(root, padx=10, pady=10)
buttonGroup.pack(padx=10, pady=10)

# Title
label1 = Label(frame, text="Data Mahasiswa", font=(30))
label1.pack()

# Description
label2 = Label(frame, text="Ceritanya ini database mahasiswa ngab")
label2.pack()

# Input btn
b_add = Button(buttonGroup, text="Input Data Mahasiswa", command=inputs, width=30)
b_add.grid(row=0, column=0, pady=5)

# All data btn
b_add = Button(buttonGroup, text="Semua Data Mahasiswa", command=viewAll, width=30)
b_add.grid(row=1, column=0, pady=5)

# Clear all btn
b_clear = Button(buttonGroup, text="Hapus Semua Data Mahasiswa", command=clearAll, width=30)
b_clear.grid(row=2, column=0, pady=5)

# About btn
b_about = Button(buttonGroup, text="About", command=about, width=30)
b_about.grid(row=3, column=0, pady=5)

# Exit btn
b_exit = Button(buttonGroup, text="Exit", command=exitDialog, width=30)
b_exit.grid(row=4, column=0, pady=5)

root.mainloop()