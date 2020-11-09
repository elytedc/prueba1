  
from flask import Flask, render_template, request, redirect, url_for, flash, current_app
from flask import Markup 
import csv
from reportlab.pdfgen import canvas


name=""
contraseña=""
app = Flask(__name__)
global cliente
cliente=[]
global aplicaciones
aplicaciones=[]
global adm
adm=[]

global reseñas
reseñas=[]




# --------------------------------------------------------------------------------principales-------------

@app.route('/')
def main_page():
    adm.append(["Usuario","Maestro","admin","admin"])
    return render_template('principal.html')

@app.route('/insertar',methods=["GET", "POST"])
def add_contact():
    estado=False
    if request.method=='POST':
        a=request.form['u1']
        b=request.form['u2']
        c=request.form['u3']
        d=request.form['p1']
        for i in range(len(cliente)):
            if cliente[i][2]==str(c):
                estado=True

        if(estado==False):
            cliente.append([str(a),str(b),str(c),str(d)])
            flash("REGISTRADO") 
            return render_template('principal.html') 
        else:
            flash("REGISTRO YA EXISTE") 
            return render_template('registro.html')

@app.route('/guardar_admo',methods=["GET", "POST"])
def agregaradmo():
    estado=False
    if request.method=='POST':
        a=request.form['u1']
        b=request.form['u2']
        c=request.form['u3']
        d=request.form['u4']
        for i in range(len(adm)):
            if adm[i][2]==str(c):
                estado=True

        if(estado==False):
            adm.append([str(a),str(b),str(c),str(d)])
            flash("REGISTRADO") 
            return render_template('admo.html') 
        else:
            flash("REGISTRO YA EXISTE") 
            return render_template('admo.html')


@app.route('/leer',methods=["GET", "POST"])
def ver_login():
    estado=False
    estado1=False
    print("mama")
    if request.method=='POST':
        a=request.form['u1']
        b=request.form['p1']
        z=request.form['op']
        print(z)
        
        if(z=="ADMO"):
            for i in range(len(adm)):
                if adm[i][2]==a and adm[i][3]==b:
                    estado1=True

            if(estado1==False):
                flash("USUARIO NO EXISTE") 
                return render_template('principal.html') 
            else:
                flash("BIENVENIDO ADMO") 
                return render_template('admo.html')
        
        else:
            for i in range(len(cliente)):
                if cliente[i][2]==a and cliente[i][3]==b:
                    estado=True

            if(estado==False):
                flash("USUARIO NO EXISTE") 
                return render_template('principal.html') 
            else:
                flash("BIENVENIDO") 
                return render_template('cliente1.html',contacts = aplicaciones) 

@app.route('/recuperar',methods=["GET", "POST"])
def recuperar():
    if request.method=='POST':
        a=request.form['u1']
        for i in range(len(cliente)):
            if cliente[i][2]==a:
                flash("su contraseña es: "+cliente[i][3]) 
                return render_template('login.html') 
 
            else:
                flash("USUARIO NO EXISTE") 
                return render_template('principal.html') 

# --------------------------------------------------------------------------------funciones admo-------------
# --------------------------------------------------------------------------------funciones admo-------------
# --------------------------------------------------------------------------------funciones admo-------------
# --------------------------------------------------------------------------------funciones admo-------------
@app.route('/carga',methods=["GET", "POST"])
def carga():
    if request.method=='POST':
        a=request.form['file']
        with open(""+a) as File:
            reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                aplicaciones.append(row)  

    flash("CARGA EXITOSA")
    print(aplicaciones)
    return render_template('admo.html')

@app.route('/cargacliente',methods=["GET", "POST"])
def cargacliente():
    if request.method=='POST':
        a=request.form['file']
        with open(""+a) as File:
            reader = csv.reader(File, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                cliente.append(row)  

    flash("CARGA EXITOSA")
    return render_template('admo.html')


@app.route('/pdf1',methods=["GET", "POST"])
def pdf1():
    if request.method=='POST':
        p = canvas.Canvas("inicio.pdf")
        mama=0
        for i in range(len(aplicaciones)):
            p.drawString(5, mama, ""+str(aplicaciones[i]))
            mama=mama+30
        p.showPage()
        p.save()
    return render_template('admo.html') 

@app.route('/pdf2',methods=["GET", "POST"])
def pdf2():
    if request.method=='POST':
        p = canvas.Canvas("clientes.pdf")
        mama=0
        for i in range(len(cliente)):
            p.drawString(5, mama, ""+str(cliente[i]))
            mama=mama+30
        p.showPage()
        p.save()
    return render_template('admo.html') 

@app.route('/eliminar_apli/<string:id>', methods = ['POST','GET'])
def delete_contact(id):
    for i in range(len(aplicaciones)):
        if aplicaciones[i][0]==str(id):
            aplicaciones.pop(i)
            break
        
    flash('DATO ELIMINADO')
    return render_template('admo.html')


@app.route('/modificar_apli/<string:id>', methods = ['POST','GET'])
def modificar_contact(id):
    y=0
    for i in range(len(aplicaciones)):
        if aplicaciones[i][0]==str(id):
            y=i
            break

    return render_template('admo2.html', contacts = aplicaciones[y])


@app.route('/modificar',methods=["GET", "POST"])
def modificar_aplicacion():
    if request.method=='POST':
        ax=request.form['u']
        a=request.form['u1']
        b=request.form['u2']
        c=request.form['u3']
        d=request.form['u4']
        e=request.form['u5']
        f=request.form['u6']
        g=request.form['u7']
        h=request.form['u8']
        for i in range(len(aplicaciones)):
            if aplicaciones[i][0]==ax:
                aplicaciones.pop(i)
                break
    aplicaciones.append([str(a),str(b),str(c),str(d),str(e),str(f),str(g),str(h)])
    flash('DATO MODIFICADO')
    return render_template('admo.html')


@app.route('/reseña/<string:id>', methods = ['POST','GET'])
def rese(id):
    y=0
    for i in range(len(aplicaciones)):
        if aplicaciones[i][0]==str(id):
            y=i
            break

    return render_template('cliente2.html', contact = aplicaciones[y])


@app.route('/insertar_reseña',methods=["GET", "POST"])
def insereseña():
    if request.method=='POST':
        a=request.form['u1']
    reseñas.append([str(a)])
    flash('RESEÑA AGREGADA')
    return render_template('cliente1.html')



@app.route('/likes/<string:id>', methods = ['POST','GET'])
def likes(id):
    for i in range(len(aplicaciones)):
        if aplicaciones[i][0]==str(id):
            a=int(aplicaciones[i][7])+1
            aplicaciones.append([aplicaciones[i][0],aplicaciones[i][1],aplicaciones[i][2],aplicaciones[i][3],aplicaciones[i][4],aplicaciones[i][5],aplicaciones[i][6],str(a)])
            aplicaciones.pop(i)
            break
        
    return render_template('cliente1.html',contacts = aplicaciones)



# --------------------------------------------------------------------------------ir a paginas-------------
# --------------------------------------------------------------------------------ir a paginas-------------
# --------------------------------------------------------------------------------ir a paginas-------------
# --------------------------------------------------------------------------------ir a paginas-------------

@app.route('/ir_registro',methods=["GET", "POST"])
def ir_registro():
    if request.method=='POST':
        return render_template('registro.html') 

@app.route('/ir_login',methods=["GET", "POST"])
def ir_login():
    if request.method=='POST':
        return render_template('login.html') 

@app.route('/ir_recuperar',methods=["GET", "POST"])
def ir_recuperar():
    if request.method=='POST':
        return render_template('recuperar.html') 


@app.route('/ir_admo',methods=["GET", "POST"])
def ir_admo():
    if request.method=='POST':
        return render_template('admo.html') 

@app.route('/ir_tabla1',methods=["GET", "POST"])
def ir_admo1():
    if request.method=='POST':
        return render_template('admo1.html',contacts=aplicaciones)

    if request.method=='GET':
        return render_template('admo1.html',contacts=cliente) 

@app.route('/ir_tabla2',methods=["GET", "POST"])
def ir_admo3():
    if request.method=='POST':
        return render_template('admo3.html',contacts=cliente) 

@app.route('/iradmo4',methods=["GET", "POST"])
def ir_admo4():
    if request.method=='POST':
        return render_template('admo4.html') 

@app.route('/irinicio',methods=["GET", "POST"])
def cerrar():
    if request.method=='POST':
        return render_template('principal.html') 




 

if __name__ == '__main__':
    app.secret_key = 'super secret key' 
    app.config['SESSION_TYPE'] = 'filesystem' 
    app.run()
        



