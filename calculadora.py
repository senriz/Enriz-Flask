from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def calcular():
    tie=''
    acel=''
    dist2=''
    if request.method == 'POST' and 'velocidad' in request.form and 'distancia' in request.form and 'frenado' in request.form:
        Velocidad=float(request.form.get('velocidad'))
        Distancia=float(request.form.get('distancia'))
        Frenado=float(request.form.get('frenado'))
        calc = 0-Velocidad
        tie = round(calc/Frenado,2)
        dist = round(0+Velocidad*tie+0.5*Frenado*(tie+tie),2)

        if dist > Distancia:
            c = Velocidad + (1/2)*(0-Velocidad)
            c2 = Distancia/c
            acel = (0-Velocidad)/c2

        if dist<=Distancia:
            dist2= Distancia-dist

 
    return render_template('index.html', acel = acel, tie = tie,dist2 = dist2)

if (__name__) == ('__main__'):
    app.run(debug=True, port=5000)