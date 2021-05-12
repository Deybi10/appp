from flask import Flask,render_template,request,url_for
import pymysql.cursors
app = Flask(__name__)
app.secret_key = '1111'
db = pymysql.connect(host="localhost",user="root",passwd="1111",db="aaa")
@app.route('/')
def conexion():
#db = pymysql.connect(host="localhost",user="root",passwd="1111",db="tkinter_mysql")
# cd pflask
# git add -A
# git config --global user.name "Nombre Usuario"
# git config --global user.email "Email Usuario"
# git conmit -m "versiom1.0"
# git remote add origin https://github.com/Deybi10/appp
# git push origin master
##### --------- consola bash pythonanywhere
# git clone 
# ls
# virtualenv --python=python3.9

    ini=db.cursor()
    try:
        ini.execute('''CREATE TABLE datos(
                                            nombre VARCHAR(50),
                                            usuario VARCHAR(50),
                                            password VARCHAR(50),
                                            email VARCHAR(50))''')
    except:
            return render_template('index.html')
    
@app.route('/registrar', methods=['GET','POST'])
def registrar():
    ini=db.cursor()
    if request.method == 'POST' and 'usuario' in request.form and 'password' in request.form and 'email' in request.form:
        nombre = request.form['nombre']
        usuario = request.form['usuario']
        password = request.form['password']
        email = request.form['email']
        ini.execute('INSERT INTO datos VALUES (%s, %s, %s, %s)',(nombre,usuario,password,email))
        db.commit()
    return render_template('register-login.html')
#if __name__ == "__main__":
#    app.run(port=8000, debug=True)

