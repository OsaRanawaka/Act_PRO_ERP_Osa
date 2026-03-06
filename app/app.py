from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Database එක හදන function එක
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory 
                      (id INTEGER PRIMARY KEY, item TEXT, qty INTEGER, price REAL)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    items = cursor.fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form['item']
    qty = request.form['qty']
    price = request.form['price']
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO inventory (item, qty, price) VALUES (?, ?, ?)", (item, qty, price))
    conn.commit()
    conn.close()
    return redirect('/')

i# අන්තිමට තියෙන app.run() එක අයින් කරලා මේක විතරක් තියන්න
app = Flask(__name__)

# ... (ඔයාගේ අනිත් codes) ...

# අන්තිමට මේක විතරක් දාන්න (Vercel එකට මේක ඕනේ)
app = app