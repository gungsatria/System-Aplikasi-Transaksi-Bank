import tkinter as tk
from tkinter import font
import random
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk  


mydb = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="",
    database="sistem_atm"
)
mycursor = mydb.cursor()

def cek_pin():
    pin = pin_entry.get()
    query = "SELECT * FROM nasabah WHERE  pin =%s "
    val = (pin,)
    mycursor.execute(query, val)
    result = mycursor.fetchone()
    return result

def cek_rekeningDanPin():
    pin = pin_entry.get()
    norekening = norekening_entry.get()
    query = "SELECT * FROM nasabah WHERE  no_rek=%s and pin =%s "
    val = (norekening,pin,)
    mycursor.execute(query, val)
    hasil= mycursor.fetchone()
    return hasil


def login_nasabah():
    global datanasabah
    datanasabah = cek_rekeningDanPin()
    if datanasabah:
        login_menu()
    else: 
        messagebox.showerror(
            "Login Failed", "pin is incorrect")

def pin_NominalTransfer(SATbank):
    result = cek_pin()
    if result:
        transaksi(SATbank)
    else:
        messagebox.showerror(
            "EROR!!! ", "pin is incorrect")

def pin_transaksi(SATbank):
    result = cek_pin()
    if result:
        Data_transaksi(SATbank)
    else:
        messagebox.showerror(
            "TRANSAKSI GAGAL ", "pin is incorrect")

def pin_setortunai():
    result = cek_pin()
    if result:
        aftersetor()
    else:
        messagebox.showerror(
            "SETOR TUNAI GAGAL!!! ", "pin is incorrect")       

def pin_tariktunai():
    result = cek_pin()
    if result:
        aftertarikTunai()
    else:
        messagebox.showerror(
            "TARIK TUNAI GAGAL!!! ", "pin is incorrect")

color_frame_bg  ="#E0FFFF" 
color_label_fg  ="#333333"
color_label_bg  ="#E0FFFF"
color_button_bg ="#3377FF"
color_button_fg ="#FFFFFF"
#belum dimasukan ke fungsi 

def resize_image(image, new_width, new_height):
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    return resized_image

def loginapps():
    global root
    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root_width = 550
    root_height = 650

    x_screen = (screen_width - root_width) // 2
    y_screen = (screen_height - root_height) // 2

    root.resizable(False, False)
    root.geometry(f"{root_width}x{root_height}+{x_screen}+{y_screen}")

    root.configure(bg = color_frame_bg)
   
    global tampilan_frame
    tampilan_frame = tk.LabelFrame(root, bg=color_frame_bg, bd=0)
    tampilan_frame.pack(pady=30)
    
    global custom_font
    custom_font = font.Font(family='Bookman Old Style', size=12)

    root.title('System Aplikasi & Transaksi Bank ')

    tampilan = tk.Label(
        tampilan_frame, text='Selamat Datang! \n Silahkan Masukkan No Rekening dan PIN Anda', font=custom_font, bg=color_label_bg,fg=color_label_fg)
    tampilan.pack(padx=10, pady=5, anchor='center')

    logo_image = Image.open("logo.png")
    logo_resized = resize_image(logo_image, 280, 300)  # Ubah ukuran logo sesuai kebutuhan
    # Konversi menjadi PhotoImage
    logo_photo = ImageTk.PhotoImage(logo_resized)

    # Tampilkan logo dalam label
    logo_label = tk.Label(tampilan_frame, image=logo_photo, bg=color_label_bg)
    logo_label.image = logo_photo
    logo_label.pack(padx=35, anchor='center')

    global label_login
    label_login = tk.Label(
        tampilan_frame, text='Masukkan NoRekening dan PIN:', font=custom_font, fg=color_label_fg, bg=color_label_bg)
    label_login.pack(padx=60, pady=10, anchor='center')

    global norekening_entry
    norekening_entry = tk.Entry(tampilan_frame, font=custom_font)
    norekening_entry.pack(padx=60,pady=10, anchor='center')

    global pin_entry
    pin_entry = tk.Entry(tampilan_frame, font=custom_font, show='*', width=10)
    pin_entry.pack(padx=60,pady=10, anchor='center')

    button_login = tk.Button(
        tampilan_frame, text='  Login  ', font=custom_font,bg=color_button_bg, fg=color_button_fg, bd=0,command=login_nasabah)
    button_login.pack(padx=60,pady=10, anchor='center')

    reset_button = tk.Button(
        tampilan_frame, text='  Daftar Rekening  ', font=custom_font,bg=color_button_bg, fg=color_button_fg, bd=0,command=daftarRekening)
    reset_button.pack(padx=60,pady=10, anchor='center')

    root.mainloop()

def daftarRekening():
    tampilan_frame.pack_forget()

    global daftar_labelframe
    daftar_labelframe = tk.LabelFrame(root,bg=color_frame_bg, bd=0)
    daftar_labelframe.pack(pady=30)

    daftar_label = tk.Label(
        daftar_labelframe, text='Silahkan isi Data diri anda ', font=custom_font, bg=color_label_bg, fg=color_label_fg)
    daftar_label.pack(padx=120, pady=10)

    nama = tk.Label(daftar_labelframe,
                    text='Nama Lengkap : ', font=custom_font, bg=color_label_bg, fg=color_label_fg)
    nama.pack(padx=10, pady=10)
    global nama1_entry
    nama1_entry = tk.Entry(daftar_labelframe)
    nama1_entry.pack(padx=20, pady=20)

    nama = tk.Label(daftar_labelframe, text='NIK : ', font=custom_font,bg=color_label_bg, fg=color_label_fg)
    nama.pack(padx=10, pady=10)
    global nik1_entry
    nik1_entry = tk.Entry(daftar_labelframe)
    nik1_entry.pack(padx=30, pady=30)

    global pin1_entry
    nama1 = tk.Label(daftar_labelframe, text='PIN : ', font=custom_font, bg=color_label_bg, fg=color_label_fg)
    nama1.pack(padx=10, pady=0)
    pin1_entry = tk.Entry(daftar_labelframe)
    pin1_entry.pack(padx=40, pady=40)

    global simpan1_button
    simpan1_button = tk.Button(
        daftar_labelframe, text='Simpan Data',font=custom_font,bg=color_button_bg, fg=color_button_fg,command=kartuDigital)
    simpan1_button.pack(padx=50, pady=50)

def kartuDigital():
    daftar_labelframe.pack_forget()

    global kartu_labelframe
    kartu_labelframe = tk.LabelFrame(root,bg=color_frame_bg, bd=0)
    kartu_labelframe.pack(pady=30)

    berhasil_label = tk.Label(
        kartu_labelframe, text='Anda Berhasil Daftar!', font=custom_font, bg=color_label_bg, fg=color_label_fg)
    berhasil_label.pack(padx=10, pady=10)

    no_kartu = str(random.randint(100000000000, 999999999999))
    no_kartu = ' '.join([no_kartu[i:i+4] for i in range(0, len(no_kartu), 4)])

    nokartu = tk.Label(
        kartu_labelframe, text='No Kartu Anda: ' + no_kartu, font=custom_font, bg=color_label_bg, fg=color_label_fg)
    nokartu.pack(padx=30, pady=10)

    global no_rekening
    no_rekening = str(random.randint(10000000, 99999999))
    no_rekening = '333'+no_rekening
    noRekening = tk.Label(
        kartu_labelframe, text='No Rekening Anda: ' + no_rekening, font=custom_font, bg=color_label_bg, fg=color_label_fg)
    noRekening.pack(padx=30, pady=20)

    kartu1_label = tk.Label(
        kartu_labelframe, text=f'Nama Lengkap: {nama1_entry.get()}', font=custom_font, bg=color_label_bg, fg=color_label_fg)
    kartu1_label.pack(padx=10, pady=30)

    kartu2_label = tk.Label(
        kartu_labelframe, text=f'NIK: {nik1_entry.get()}', font=custom_font, bg=color_label_bg, fg=color_label_fg)
    kartu2_label.pack(padx=30, pady=40)

    global kartu3_label
    kartu3_label = tk.Label(
        kartu_labelframe, text=f'PIN: {pin1_entry.get()}', font=custom_font, bg=color_label_bg, fg=color_label_fg)
    kartu3_label.pack(padx=30, pady=40)

    button_kartu = tk.Button(
        kartu_labelframe, text=' Selesai ', font=custom_font,bg=color_button_bg, fg=color_button_fg,command=backtologin)
    button_kartu.pack(padx=30, pady=30)

    # kode untuk insert ke database
    query = "INSERT INTO nasabah VALUES (%s, %s, %s, %s, %s,%s)"
    data = (no_rekening, no_kartu, nama1_entry.get(),
            nik1_entry.get(), pin1_entry.get(),0)
    mycursor.execute(query, data)
    mydb.commit()
    

def backtologin():
    kartu_labelframe.pack_forget()
    tampilan_frame.pack()


def login_menu():
    tampilan_frame.pack_forget()  # Menghilangkan frame lama
    # Membuat frame baru  halaman selanjutnya
    global new_labelframe
    new_labelframe = tk.LabelFrame(root,bg=color_frame_bg, bd=0)
    new_labelframe.pack(pady=30)

    # Menambahkan isi halaman selanjutnya
    new_label1 = tk.Label(
        new_labelframe, text='Pilih Transaksi yang anda inginkan !!\n Tekan Cancel untuk pembatalan', font=custom_font, bg=color_label_bg, fg=color_label_fg)
    new_label1.pack(padx=10, pady=10)

    button_transfer = tk.Button(
        new_labelframe, text='  <-- Transfer -->  ', font=custom_font,bg= color_button_bg, fg = color_button_fg, command=transfer_window)
    button_transfer.pack(padx=60, pady=35)

    button_penarikantunai = tk.Button(
        new_labelframe, text='  <-- Tarik/Setor Tunai -->  ', font=custom_font,bg= color_button_bg, fg = color_button_fg,command=tariksetorTunai)
    button_penarikantunai.pack(padx=60, pady=35)

    button_Informasisaldo = tk.Button(
        new_labelframe, text='  <-- Informasi Saldo -->  ', font=custom_font,bg= color_button_bg, fg = color_button_fg,command=informasi_saldo)
    button_Informasisaldo.pack(padx=60, pady=35)

    button_Cancel = tk.Button(
        new_labelframe, text='  Cancel  ', font=custom_font,bg=color_button_bg, fg=color_button_fg, command=closeProgram)
    button_Cancel.pack(padx=60, pady=50)

    #tampilan menekan tramsfer dan menjalankan windwow baru 
def transfer_window():
    new_labelframe.pack_forget()  

    global transfer_labelframe
    transfer_labelframe = tk.LabelFrame(root,bg = color_frame_bg, bd=0)
    transfer_labelframe.pack(pady=30)

    transfer_label = tk.Label(
        transfer_labelframe, text='ATM Transfer Pilih Bank Tujuan Transfer', font=custom_font, bg= color_label_bg, fg = color_label_fg)
    transfer_label.pack(padx=10, pady=10)

    button_SATbank = tk.Button(
        transfer_labelframe, text='   <-- SATBANK -->  ', font=custom_font,bg=color_button_bg, fg=color_button_fg, command=lambda: SATbank(True))
    button_SATbank.pack(padx=110, pady=60)

    button_Banklain = tk.Button(
        transfer_labelframe, text='  <-- BANK LAIN -->  ', font=custom_font,bg=color_button_bg, fg=color_button_fg, command=banklain)
    button_Banklain.pack(padx=110, pady=60)

    button_DaftarKontak = tk.Button(
        transfer_labelframe, text='  <-- DAFTAR KODE BANK -->  ', font=custom_font,bg=color_button_bg, fg=color_button_fg,command=daftarKodeBank)
    button_DaftarKontak.pack(padx=110, pady=60)

    button_kembali = tk.Button(
        transfer_labelframe, text='  Kembali  ', font=custom_font,bg=color_button_bg, fg=color_button_fg,command=lambda:backtoMenu('backtomenufromtranserwindow'))
    button_kembali.pack(padx=110, pady=10)

#tampilan menekan SATBank dan membuka window baru di halaman SATBank
def SATbank(SATbank=False):
    transfer_labelframe.pack_forget() 
    
    global SATbank_labelframe
    SATbank_labelframe = tk.LabelFrame(root,bg = color_frame_bg, bd=0)
    SATbank_labelframe.pack(pady=30)

    SATbank_label = tk.Label(
        SATbank_labelframe, text='Silahkan Isi No Rekening Bank Yang Dituju', font=custom_font, bg= color_label_bg, fg = color_label_fg)
    SATbank_label.pack(padx=10, pady=10)

    global norekening_entry
    norekening_label = tk.Label(
        SATbank_labelframe, text='Masukan No Rekening : ', font=custom_font, anchor='center', bg= color_label_bg, fg = color_label_fg)
    norekening_label.pack(padx=120, pady=120)

    norekening_entry = tk.Entry(SATbank_labelframe)
    norekening_entry.place(x=220, y=240,anchor='center')

    if SATbank:
        button_enter = tk.Button(
            SATbank_labelframe, text='  Enter  ', font=custom_font, bg=color_button_bg, fg=color_button_fg,command=cekrekeningtujuan)
        button_enter.pack(padx=110, pady=60)
    else:
        button_enter = tk.Button(
            SATbank_labelframe, text='  Enter  ', font=custom_font, bg=color_button_bg, fg=color_button_fg,command=lambda: nominalTransfer(False))
        button_enter.pack(padx=110, pady=60)
    
    button_kembali = tk.Button(
            SATbank_labelframe, text='  Kembali  ', font=custom_font, bg=color_button_bg, fg=color_button_fg,command=lambda:backtobanklain('backtomenufromSatbank'))
    button_kembali.pack(padx=110, pady=5,anchor='s')

def backtobanklain(backmenu):
    if backmenu == 'backtomenu':
        daftarKodeframe.pack_forget()
    elif backmenu == 'backtomenufromSatbank':
        SATbank_labelframe.pack_forget()
    elif backmenu ==  'backtomenufrombanklain':
        banklainframe.pack_forget()
    transfer_window()

    # menambahkan rekening tujuan dan beralih ke nominal transfer 
def cekrekeningtujuan():
    query = "SELECT no_rek FROM nasabah WHERE no_rek=%s "
    val = (norekening_entry.get(),)
    mycursor.execute(query, val)
    result = mycursor.fetchone()
    if result:
        nominalTransfer(True)
    else:
        messagebox.showwarning('WARNING!!!','No Rekening Tujuan Tidak Terdaftar!\n Silahkan Masukan No Rekening Yang Benar ')

def nominalTransfer(SATbank):
    SATbank_labelframe.pack_forget()

    global nominal_labelframe
    nominal_labelframe = tk.LabelFrame(root,bg=color_frame_bg, bd=0)
    nominal_labelframe.pack(pady=30)

    nominalframe = tk.Label(
        nominal_labelframe, text='Masukan Jumlah Nominal yang akan di transfer', font=custom_font,bg=color_label_bg, fg=color_label_fg)
    nominalframe.pack(padx=10, pady=10)

    nominalframeRp = tk.Label(
        nominal_labelframe, text='Rp', font=custom_font, anchor='center',bg=color_label_bg, fg=color_label_fg)
    nominalframeRp.pack(padx=120, pady=40)
    global nominal_entry
    nominal_entry = tk.Entry(nominal_labelframe)
    nominal_entry.pack(padx=120, pady=20)

    label_login = tk.Label(
        nominal_labelframe, text='Masukkan PIN:', font=custom_font, anchor='s',bg=color_label_bg, fg=color_label_fg)
    label_login.pack(padx=110, pady=120)
    global pin_entry
    pin_entry = tk.Entry(nominal_labelframe, show='*')
    pin_entry.place(x=120, y=360)

    button_benar = tk.Button(
        nominal_labelframe, text='  <-- Tekan jika benar -->  ', font=custom_font,bg=color_button_bg, fg=color_button_fg, command=lambda: pin_NominalTransfer(SATbank) )
    button_benar.place(x=90, y=390)

    button_salah = tk.Button(
        nominal_labelframe, text='  <-- Reset -->  ', font=custom_font,bg=color_button_bg, fg=color_button_fg, command=reset_Pin)
    button_salah.place(x=130, y=430)

def reset_Pin():
    pin_entry.delete(0, tk.END)

    #beralih ke detail  transaksi 
def transaksi (SATbank):
    nominal_labelframe.pack_forget()

    global benar_labelframe
    benar_labelframe = tk.LabelFrame(root,bg=color_frame_bg, bd=0)
    benar_labelframe.pack(pady=30)

    benarlframe = tk.Label(
        benar_labelframe, text='Masukan Pin Anda Jika data transaksi sudah benar', font=custom_font, bg = color_label_bg, fg = color_label_fg)
    benarlframe.pack(padx=10, pady=10)
    
    rekeningSayaframe = tk.Label(
        benar_labelframe, text=f'No Rekening Anda: {datanasabah[0]}', font=custom_font, anchor='center',bg= color_label_bg, fg = color_label_fg)
    rekeningSayaframe.pack(padx=10, pady=20)

    rekeningTujuanframe = tk.Label(
        benar_labelframe, text=f'No Rekening Tujuan: {norekening_entry.get()}', font=custom_font, anchor='center',bg= color_label_bg, fg = color_label_fg)
    rekeningTujuanframe.pack(padx=10, pady=20, )

    jumlahtransaksiframe = tk.Label(
        benar_labelframe, text=f'Jumlah Transaksi: Rp.{nominal_entry.get()}', font=custom_font, anchor='center',bg= color_label_bg, fg = color_label_fg)
    jumlahtransaksiframe.pack(padx=10, pady=20, )

    masukanpinframe = tk.Label(
        benar_labelframe, text='Masukan Pin : ', font=custom_font,bg= color_label_bg, fg = color_label_fg)
    masukanpinframe.pack(padx=10, pady=40)
    
    pin_entry = tk.Entry(benar_labelframe, font=custom_font, show='*')
    pin_entry.pack(padx=10, pady=30)

    button_enter = tk.Button(
        benar_labelframe, text='  Enter  ', font=custom_font, anchor='s',bg= color_button_bg, fg = color_button_fg, command=lambda: pin_transaksi(SATbank))
    button_enter.pack(padx=10, pady=15)


    # kode untuk insert ke database
    queryku = "INSERT INTO data_transaksi (nama, noRekening, noRekening_tujuan, jumlah_transaksi) VALUES (%s, %s, %s,%s)"
    val = (datanasabah[2],datanasabah[0],
                    norekening_entry.get(),nominal_entry.get())
    mycursor.execute(queryku, val)
    mydb.commit()

#beralih ke data transaksi dan transaksi berhasil di lakukan pada halaman SATbank  
def Data_transaksi(SATbank):
    benar_labelframe.pack_forget()

    query = "SELECT saldo FROM nasabah WHERE no_rek=%s and pin =%s "
    val = (datanasabah[0],pin_entry.get(),)
    mycursor.execute(query, val)
    saldo = mycursor.fetchone()[0]

    total_saldo = int(saldo) - int(nominal_entry.get())

    # query kurang saldo
    query = "UPDATE nasabah SET saldo = %s WHERE no_rek = %s"
    data = (total_saldo, datanasabah[0])
    mycursor.execute(query, data)
    mydb.commit()

    # kondisi untuk memeriksa apakah tujuan nya ke SATbank atau bukan
    if SATbank:

        query = "SELECT saldo FROM nasabah WHERE no_rek=%s "
        val = (norekening_entry.get(),)
        mycursor.execute(query, val)
        saldo = mycursor.fetchone()[0]

        total_saldo = int(saldo) + int(nominal_entry.get())

        # query Tambah saldo
        query = "UPDATE nasabah SET saldo = %s WHERE no_rek = %s"
        data = (total_saldo, norekening_entry.get())
        mycursor.execute(query, data)
        mydb.commit() 

    global enter_labelframe
    enter_labelframe = tk.LabelFrame(root,bg = color_frame_bg, bd=0)
    enter_labelframe.pack(pady=30)

    enterframe = tk.Label(enter_labelframe, text='ATM',
                          font=custom_font, anchor='w',bg= color_label_bg, fg = color_label_fg)
    enterframe.pack(padx=10, pady=10)

    enterframe2 = tk.Label(
        enter_labelframe, text='Transaksi Anda Berhasil Dilaksanakan', font=custom_font, anchor='center',bg= color_label_bg, fg = color_label_fg)
    enterframe2.pack(padx=10, pady=20)
    enterframe3 = tk.Label(
        enter_labelframe, text='Terimakasi Atas Kepercayaan Anda', font=custom_font,bg= color_label_bg, fg = color_label_fg)
    enterframe3.pack(padx=10, pady=20)
    enterframe3 = tk.Label(
        enter_labelframe, text='Transaksi Lagi ? ', font=custom_font,bg= color_label_bg, fg = color_label_fg)
    enterframe3.pack(padx=10, pady=20)

    global buttonenter1
    buttonenter1 = tk.Button(enter_labelframe, text='ya',
                             font=custom_font, anchor='s',bg= color_button_bg, fg = color_button_fg,  command=lambda: backtoMenu('transaksi'))
    buttonenter1.pack(padx=50, pady=50)

    buttonenter2 = tk.Button(enter_labelframe, text='tidak',
                             font=custom_font, anchor='s',bg= color_button_bg, fg = color_button_fg, command=closeProgram)
    buttonenter2.pack(padx=50, pady=40)

#kembali ke tampilan menu login 
def backtoMenu(frame):
    if frame == 'transaksi':
        enter_labelframe.pack_forget()

    elif frame == 'Menu Bank' :
        banklainframe.pack_forget()
        
    elif frame == 'MenuSetortunai' :
        setorTunaiframe.pack_forget()
    
    elif frame == 'SetorTunai' :
        aftersetor_frame.pack_forget()
        
    elif frame == 'MenuTariktunai' :
        tarik_Tunaiframe.pack_forget()
    
    elif frame == 'TarikTunai' :
        aftertariktunai_frame.pack_forget()
    
    elif frame == 'InformasiSaldo' :
        informasisaldo_frame.pack_forget()
    elif frame == 'backtomenufromtranserwindow':
        transfer_labelframe.pack_forget()
    login_menu()

#menutup program
def closeProgram():
    root.destroy()

def banklain():
    transfer_labelframe.pack_forget()

    global banklainframe
    banklainframe = tk.LabelFrame(root,bg = color_frame_bg, bd=0)
    banklainframe.pack(pady=30)

    banklain_label = tk.Label(
        banklainframe, text=' Pilih Kode Bank Tujuan \n Sebelum Melakukan Transaksi', font=custom_font, anchor='w',bg= color_label_bg, fg = color_label_fg)
    banklain_label.pack(padx=30, pady=10)

    button_Bni = tk.Button(
        banklainframe, text='<-- BNI -->', font=custom_font,bg= color_button_bg, fg = color_button_fg, command= MenuBank)
    button_Bni.pack(padx=80, pady=10)

    button_mandiri = tk.Button(
        banklainframe, text='<-- MANDIRI -->', font=custom_font,bg= color_button_bg, fg = color_button_fg, command= MenuBank)
    button_mandiri.pack(padx=80, pady=15)

    button_syariah = tk.Button(
        banklainframe, text='<-- SYARIAH -->', font=custom_font,bg= color_button_bg, fg = color_button_fg, command= MenuBank)
    button_syariah.pack(padx=80, pady=20)

    button_danamon = tk.Button(
        banklainframe, text='<-- DANAMON -->', font=custom_font,bg= color_button_bg, fg = color_button_fg, command= MenuBank)
    button_danamon.pack(padx=80, pady=25)

    button_permata = tk.Button(
        banklainframe, text='<-- PERMATA BANK -->', font=custom_font,bg= color_button_bg, fg = color_button_fg, command= MenuBank)
    button_permata.pack(padx=80, pady=30)

    button_kembali = tk.Button(
        banklainframe, text='<-- KEMBALI -->', font=custom_font,bg= color_button_bg, fg = color_button_fg, command=lambda: backtobanklain('backtomenufrombanklain'))
    button_kembali.pack(padx=80, pady=35)

def MenuBank():
    banklainframe.pack_forget()
    SATbank()

def daftarKodeBank():
    transfer_labelframe.pack_forget()

    global daftarKodeframe 
    daftarKodeframe=tk.LabelFrame(root,bg = color_frame_bg, bd=0)
    daftarKodeframe.pack(pady=30)
    
    daftarKode_label = tk.Label(
        daftarKodeframe, text=' Pilih Kode Bank Tujuan anda ', font=custom_font, anchor='w',bg= color_label_bg, fg = color_label_fg)
    daftarKode_label.pack(padx=30, pady=10)

    daftarKodeSATbank_label = tk.Label(
        daftarKodeframe, text=' SATbank  : 333', font=custom_font, anchor='w',bg= color_label_bg, fg = color_label_fg)
    daftarKodeSATbank_label.pack(padx=80, pady=10)
    
    daftarKodeBNI_label = tk.Label(
        daftarKodeframe, text=' BNI  : 444', font=custom_font, anchor='w',bg= color_label_bg, fg = color_label_fg)
    daftarKodeBNI_label.pack(padx=80, pady=15)

    daftarKodeMANDIRI_label = tk.Label(
        daftarKodeframe, text=' MANDRI  : 555', font=custom_font, anchor='w',bg= color_label_bg, fg = color_label_fg)
    daftarKodeMANDIRI_label.pack(padx=80, pady=20)

    daftarKodeSYARIAH_label = tk.Label(
        daftarKodeframe, text=' SYARIAH  : 666', font=custom_font, anchor='w',bg= color_label_bg, fg = color_label_fg)
    daftarKodeSYARIAH_label.pack(padx=80, pady=20)

    daftarKodeDANAMON_label = tk.Label(
        daftarKodeframe, text=' DANAMON  : 777', font=custom_font, anchor='w',bg= color_label_bg, fg = color_label_fg)
    daftarKodeDANAMON_label.pack(padx=80, pady=20)

    daftarKodePERMATA_label = tk.Label(
        daftarKodeframe, text=' PERMATA BANK  : 888', font=custom_font, anchor='w',bg= color_label_bg, fg = color_label_fg)
    daftarKodePERMATA_label.pack(padx=80, pady=20)

    button_kembalikebanklain = tk.Button(
        daftarKodeframe, text='<-- KEMBALI -->', font=custom_font,bg= color_button_bg, fg = color_button_fg, command=lambda:backtobanklain('backtomenu'))
    button_kembalikebanklain.pack(padx=80, pady=25)

def tariksetorTunai():
    new_labelframe.pack_forget()

    global tarikTunaitampilan_frame
    tarikTunaitampilan_frame = tk.LabelFrame(root,bg = color_frame_bg, bd=0)
    tarikTunaitampilan_frame.pack(pady=30)

    tariktunaiframe = tk.Label(
        tarikTunaitampilan_frame, text='Silahkan Memilih Transaksi ', font=custom_font, anchor='w',bg= color_label_bg, fg = color_label_fg)
    tariktunaiframe.pack(padx=10, pady=10)
    tariktunaiframe = tk.Label(
        tarikTunaitampilan_frame, text='Tekan cancel untuk membatalkan transaksi', font=custom_font,bg= color_label_bg, fg = color_label_fg)
    tariktunaiframe.pack(padx=10, pady=10)

    button_tariktunai = tk.Button(
        tarikTunaitampilan_frame, text=' <-- Setor Tunai --> ', font=custom_font,bg= color_button_bg, fg = color_button_fg,command=setorTunai)
    button_tariktunai.place(x=100, y=150)

    button_tariktunai1 = tk.Button(
        tarikTunaitampilan_frame, text=' <-- Tarik Tunai --> ', font=custom_font,bg= color_button_bg, fg = color_button_fg,anchor='center',command=tarikTunai)
    button_tariktunai1.pack(padx=10, pady=150)

    button_canceltariktunai = tk.Button(
        tarikTunaitampilan_frame, text='Cancel', font=custom_font,bg= color_button_bg, fg = color_button_fg,command=closeProgram)
    button_canceltariktunai.pack(padx=10, pady=40)

def setorTunai():
    tarikTunaitampilan_frame.pack_forget()

    global setorTunaiframe
    setorTunaiframe = tk.LabelFrame(root,bg = color_frame_bg, bd=0)
    setorTunaiframe.pack(pady=30)

    setortunailabel = tk.Label(
                setorTunaiframe, text='Silahkan Masukan Nominal Yang Ingin di Setor! ', font=custom_font,bg= color_label_bg, fg = color_label_fg)
    setortunailabel.pack(padx=10, pady=10)
    global setor_entry
    setor_entry = tk.Entry(setorTunaiframe)
    setor_entry.pack(padx=40, pady=70)

    setortunaiPinlabel = tk.Label(
        setorTunaiframe, text='Masukan Pin : ', font=custom_font,bg= color_label_bg, fg = color_label_fg)
    setortunaiPinlabel.pack(padx=30, pady=60)
    global pin_entry
    pin_entry = tk.Entry(setorTunaiframe,show='*')
    pin_entry.pack(padx=10, pady=10)

    setor_button = tk.Button(setorTunaiframe, text=' Ya ', font=custom_font,bg= color_button_bg, fg = color_button_fg,command=pin_setortunai)

    setor_button.pack(padx=10, pady=10)

    global setor1_button
    setor1_button = tk.Button(
        setorTunaiframe, text='reset', font=custom_font,bg= color_button_bg, fg = color_button_fg,command=resetsetortunai)
    setor1_button.pack(padx=10, pady=10)

    setor2_button = tk.Button(
        setorTunaiframe, text='cancel', font=custom_font,bg= color_button_bg, fg = color_button_fg,command=lambda:backtoMenu('MenuSetortunai'))
    setor2_button.pack(padx=10, pady=10)

def resetsetortunai():
    pin_entry.delete(0, tk.END)

def aftersetor():
    setorTunaiframe.pack_forget()

    global aftersetor_frame
    aftersetor_frame=tk.LabelFrame(root,bg = color_frame_bg, bd=0)
    aftersetor_frame.pack(pady=30)

    aftersetr_labelframe=tk.Label(aftersetor_frame,text=f'Setor Success Setor senilai {setor_entry.get()} Berhasil !',font=custom_font,bg= color_label_bg, fg = color_label_fg)
    aftersetr_labelframe.pack(padx=40,pady=180,anchor='center')
    # Ambil saldo dari database
    query = "SELECT saldo FROM nasabah WHERE  no_rek=%s and pin =%s "
    val = (datanasabah[0],pin_entry.get())
    mycursor.execute(query, val)
    saldo = mycursor.fetchone()[0]

    total_saldo = int(saldo) + int(setor_entry.get())
    
    # query Tambah saldo
    query = "UPDATE nasabah SET saldo = %s WHERE no_rek = %s"
    data = (total_saldo, datanasabah[0])
    mycursor.execute(query, data)
    mydb.commit()

    button_aftersetor =tk.Button(aftersetor_frame,text='Kembali',font=custom_font,bg= color_button_bg, fg = color_button_fg,command=lambda:backtoMenu('SetorTunai'))
    button_aftersetor.pack(padx=40,pady=40)

def tarikTunai():
    tarikTunaitampilan_frame.pack_forget()

    global tarik_Tunaiframe
    tarik_Tunaiframe = tk.LabelFrame(root, bg = color_frame_bg, bd=0)
    tarik_Tunaiframe.pack(pady=30)

    tarik_tunailabel= tk.Label(
                        tarik_Tunaiframe, text='Silahkan Masukan Nominal Yang Ingin di tarik! ',font=custom_font,bg= color_label_bg, fg = color_label_fg)
    tarik_tunailabel.pack(padx=10, pady=10)

    
    nominaltarikframeRp = tk.Label(
        tarik_Tunaiframe, text='Rp', font=custom_font, anchor='center',bg= color_label_bg, fg = color_label_fg)
    nominaltarikframeRp.pack(padx=10, pady=20)

    global tarik_entry
    tarik_entry = tk.Entry(tarik_Tunaiframe)
    tarik_entry.pack(padx=40, pady=70)

    tarik_tunaiPinlabel = tk.Label(
                        tarik_Tunaiframe, text='Masukan Pin : ', font=custom_font,bg= color_label_bg, fg = color_label_fg)
    tarik_tunaiPinlabel.pack(padx=30, pady=40)
    global pin_entry
    pin_entry = tk.Entry(tarik_Tunaiframe,show='*')
    pin_entry.pack(padx=10, pady=10)

    tarik_button = tk.Button(tarik_Tunaiframe, text=' Ya ', font=custom_font,bg= color_button_bg, fg = color_button_fg,command=pin_tariktunai)
    tarik_button.pack(padx=10, pady=10)

    tarik2_button = tk.Button(
        tarik_Tunaiframe, text='cancel',font=custom_font,bg= color_button_bg, fg = color_button_fg,command=lambda:backtoMenu('MenuTariktunai'))
    tarik2_button.pack(padx=10, pady=10)

def aftertarikTunai():
    tarik_Tunaiframe.pack_forget()

    global aftertariktunai_frame
    aftertariktunai_frame=tk.LabelFrame(root, bg = color_frame_bg, bd=0)
    aftertariktunai_frame.pack(pady=30)

    aftertariktunai_label= tk.Label(aftertariktunai_frame,text=f'Tarik Tunai Success senilai {tarik_entry.get()} Berhasil !',font=custom_font,bg= color_label_bg, fg = color_label_fg)
    aftertariktunai_label.pack(padx=40,pady=180,anchor='center')

    query = "SELECT saldo FROM nasabah WHERE no_rek=%s and pin =%s "
    val = (datanasabah[0],pin_entry.get(),)
    mycursor.execute(query, val)
    saldo = mycursor.fetchone()[0]

    total_saldo = int(saldo) - int(tarik_entry.get())
    
    # query Tambah saldo
    query = "UPDATE nasabah SET saldo = %s WHERE no_rek = %s"
    data = (total_saldo, datanasabah[0])
    mycursor.execute(query, data)
    mydb.commit() 

    button_aftertarik =tk.Button(aftertariktunai_frame,text='Kembali',font=custom_font,bg= color_button_bg, fg = color_button_fg,command=lambda:backtoMenu('TarikTunai'))
    button_aftertarik.pack(padx=40,pady=40)

def informasi_saldo ():
    new_labelframe.pack_forget()

    global informasisaldo_frame
    informasisaldo_frame =tk.LabelFrame(root,bg = color_frame_bg, bd=0)
    informasisaldo_frame.pack(pady=30)

    query = "SELECT saldo FROM nasabah WHERE no_rek=%s and pin =%s "
    val = (datanasabah[0],pin_entry.get(),)
    mycursor.execute(query, val)
    saldo = mycursor.fetchone()[0]
    
    informasisaldo_label=tk.Label(informasisaldo_frame,text= f'Saldo Anda Saat Ini tersisa Rp.{saldo}',font=custom_font,bg= color_label_bg, fg = color_label_fg)
    informasisaldo_label.pack(padx=80,pady=60) 

    button_informasisaldo=tk.Button(informasisaldo_frame,text='kembali',font=custom_font,bg= color_button_bg, fg = color_button_fg,command=lambda:backtoMenu('InformasiSaldo'))
    button_informasisaldo.pack(padx=80,pady=100)