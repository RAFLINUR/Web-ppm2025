from flask import Flask, render_template, request, redirect, flash

# Inisialisasi aplikasi Flask
app = Flask(__name__)
app.secret_key = 'PPM'

# # Konfigurasi MySQL
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'gucheez'

# mysql = MySQL(app)

# # Route untuk cek koneksi ke database
# @app.route('/cek_koneksi')
# def cek_koneksi():
#     try:
#         cur = mysql.connection.cursor()
#         cur.execute("SELECT 1")
#         cur.close()
#         return "Koneksi berhasil!"
#     except Exception as e:
#         return f"Koneksi gagal: {e}"

# # Route untuk menampilkan dan mengelola produk
# @app.route('/admin_produk', methods=['GET', 'POST'])
# def admin_produk():
#     if request.method == 'POST':
#         try:
#             operation = request.form.get('operation')
#             cur = mysql.connection.cursor()

#             if operation == 'add':
#                 name_product = request.form['name_product']
#                 image_url = request.form.get('image_url', '')
#                 price = float(request.form['price'])
#                 category = request.form['category']
#                 in_stock = int(request.form['in_stock'])

#                 cur.execute("INSERT INTO products (name_product, image_url, price, category, in_stock) VALUES (%s, %s, %s, %s, %s)",
#                             (name_product, image_url, price, category, in_stock))
#                 mysql.connection.commit()
#                 flash('Produk berhasil ditambahkan!', 'success')

#             elif operation == 'edit':
#                 product_id = request.form['product_id']
#                 name_product = request.form['name_product']
#                 image_url = request.form.get('image_url', '')
#                 price = float(request.form['price'])
#                 category = request.form['category']
#                 in_stock = int(request.form['in_stock'])

#                 cur.execute("UPDATE products SET name_product = %s, image_url = %s, price = %s, category = %s, in_stock = %s WHERE id = %s",
#                             (name_product, image_url, price, category, in_stock, product_id))
#                 mysql.connection.commit()
#                 flash('Produk berhasil diperbarui!', 'success')

#             elif operation == 'delete':
#                 product_id = request.form['product_id']
#                 cur.execute("DELETE FROM products WHERE id = %s", (product_id,))
#                 mysql.connection.commit()
#                 flash('Produk berhasil dihapus!', 'success')

#             cur.close()
#             return redirect('/admin_produk')

#         except Exception as e:
#             flash(f'Operasi gagal: {e}', 'danger')
#             return redirect('/admin_produk')

#     try:
#         cur = mysql.connection.cursor()
#         # Mengambil data produk dengan relasi kategori
#         query = """
#             SELECT p.id, p.name_product, p.image_url, p.price, c.name AS category_name, p.in_stock
#             FROM products p
#             LEFT JOIN categories c ON p.category = c.id
#         """
#         cur.execute(query)
#         produk_data = cur.fetchall()
#         cur.close()
#         return render_template('admin_produk.html', produk=produk_data)
#     except Exception as e:
        
#         return render_template('admin_produk.html', produk=[])


# Route untuk halaman utama
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

# Route untuk menampilkan daftar produk
@app.route('/produk', methods=['GET'])
def produk():
    try:
        # Ambil data dari database
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM products")
        produk_data = cur.fetchall()
        cur.close()

        return render_template('produk.html', produk=produk_data)
    except Exception as e:
        flash(f'Gagal memuat data produk: {e}', 'danger')
        return render_template('produk.html', produk=[])

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
