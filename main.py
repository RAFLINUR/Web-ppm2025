from flask import Flask, render_template, request, redirect, flash

# Inisialisasi aplikasi Flask
app = Flask(__name__)
app.secret_key = 'PPM'

# Route untuk halaman utama
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

# Route untuk menampilkan daftar produk
# Route neng kontak
@app.route('/kontak')
def kontak():
    return render_template('kontak.html')

# route neng layanan
@app.route('/layanan')
def layanan():
    return render_template('layanan.html')

if __name__ == '__main__':
    app.run(debug=True)
