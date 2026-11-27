from flask import Flask, render_template, request, abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            edad = int(request.form['edad'])
            cantidad = int(request.form['cantidad'])

            if edad < 0 or cantidad < 0:
                abort(400, description="La edad y la cantidad no pueden ser valores negativos.")

            precio_tarro = 9000
            total_sin_descuento = cantidad * precio_tarro
            descuento = 0

            if 18 <= edad <= 30:
                descuento = total_sin_descuento * 0.15
            elif edad > 30:
                descuento = total_sin_descuento * 0.25

            total_pagar = total_sin_descuento - descuento

            return render_template('ejercicio1.html', 
                                   nombre=nombre, 
                                   total_sin_descuento=total_sin_descuento, 
                                   descuento=descuento, 
                                   total_pagar=total_pagar)
        except ValueError:
            abort(400, description="Por favor, ingrese números válidos.")
            
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario'].lower()
        contrasena = request.form['contrasena']
        
        mensaje = "Usuario o contraseña incorrectos"
        exito = False

        # Validación de usuarios pre-registrados
        if usuario == 'juan' and contrasena == 'admin':
            mensaje = "Bienvenido administrador juan"
            exito = True
        elif usuario == 'pepe' and contrasena == 'user':
            mensaje = "Bienvenido usuario pepe"
            exito = True

        return render_template('ejercicio2.html', mensaje=mensaje, exito=exito)

    return render_template('ejercicio2.html')

@app.errorhandler(400)
def bad_request(error):
    return render_template('index.html', error=error.description), 400

if __name__ == '__main__':
    app.run(debug=True)