from flask import Flask,render_template,url_for,redirect,request
import mariadb
import pymysql
import datetime
app = Flask(__name__)

conexionbd = pymysql.connect(
    host="195.179.238.52",
    user="u744565899_rodolfo",
    password="LLatoomali12",
    database="u744565899_smile_design"
)

cursor = conexionbd.cursor()

@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/contacto')
def contacto():
    return render_template("Contacto.html")

@app.route("/servicios")
def servicios():
    return render_template("Servicios.html")

@app.route('/citahecha', methods=['POST'])
def hacer_cita():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']
        fecha = datetime.date.today()
        cursor.execute("INSERT INTO contacto(nombre,correo,mensaje,fecha) VALUES(%s,%s,%s,%s)",(nombre,correo,mensaje,fecha))
        conexionbd.commit()
        #cursor.close()
        return render_template("Contacto.html")
    

if __name__ == '__main__':
    app.run(port=3000, debug=True)