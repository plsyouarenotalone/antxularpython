from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return
        # Kalkulator Penghitung Luas Lingkaran

# Deklarasi Variabel phi
phi = 3.14 # Dini Ga Bisa Pake tanda koma harus pake titik

# Header/Judul
print("Kalkulator Menghitung Luas Lingkaran")
print()

# Input Dari User
r = float(input("Masukkan Jari-jari: ")) # User Input

# Penghitungan
luas = phi * r * r # Rumus Luas Lingkaran
luas_bulat = round(luas, 2) # Pembulatan Angka

# Output Ke User
print("Luas Lingkaran Adalah: ", luas_bulat)



