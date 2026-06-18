from flask import Flask
from markupsafe import escape
from flask import render_template
import procesos as crear
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def inicio(name=None):
	return render_template('index.html', person=name)
	
@app.route("/menu_inicio")
def menu_inicio():
    datos = crear.menu_inicio()
    return(datos)

@app.route("/menu_temp1")
def menu_temp1():
    datos = crear.menu_temp1()
    return(datos)

@app.route("/menu_temp2")
def menu_temp2():
    datos = crear.menu_temp2()
    return(datos)

@app.route("/menu_temp3")
def menu_temp3():
    datos = crear.menu_temp3()
    return(datos)

@app.route("/menu_pelis")
def menu_pelis():
    datos = crear.menu_pelis()
    return(datos)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)    
    