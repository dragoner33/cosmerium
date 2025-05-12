from flask import Flask, render_template

app = Flask(__name__)

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

# Página del Vigilante
@app.route('/vigilante')
def vigilante():
    return render_template('vigilante.html')

# Página del Armero
@app.route('/armero')
def armero():
    return render_template('armero.html')

# Página del Sastre
@app.route('/sastre')
def sastre():
    return render_template('sastre.html')

# Página del Cirujano
@app.route('/cirujano')
def cirujano():
    return render_template('cirujano.html')

# Página del Tabernero
@app.route('/tabernero')
def tabernero():
    return render_template('tabernero.html')

# Página del Meretriz
@app.route('/meretriz')
def meretriz():
    return render_template('meretriz.html')

# Página del Cazador
@app.route('/cazador')
def cazador():
    return render_template('cazador.html')

# Página del Herborista
@app.route('/herborista')
def herborista():
    return render_template('herborista.html')

# Página del Cazarrecompensas
@app.route('/cazarrecompensas')
def cazarrecompensas():
    return render_template('cazarrecompensas.html')

# Página del Minero
@app.route('/minero')
def minero():
    return render_template('minero.html')
          
# Página del Humano Meridional
@app.route('/humano_meridional')
def humano_meridional():
    return render_template('dominio_meridional.html')
    
# Página del Humano Oriental
@app.route('/humano_oriental')
def humano_oriental():
    return render_template('dominio_oriental.html')
    
# Página del Humano Septentrional
@app.route('/humano_septentrional')
def humano_septentrional():
    return render_template('dominio_septentrional.html')
    
# Página del Humano Occidental
@app.route('/humano_occidental')
def humano_occidental():
    return render_template('dominio_occidental.html')
    
# Página del Humano Central
@app.route('/humano_central')
def humano_central():
    return render_template('dominio_central.html')
    
# Página del Terrisano
@app.route('/terrisano')
def terrisano():
    return render_template('terrisano.html')
    
# Página del Koloss nacidos sin clavo
@app.route('/koloss_sin')
def koloss_sin():
    return render_template('koloss_sin.html')
    
# Página del Koloss
@app.route('/koloss')
def koloss():
    return render_template('koloss.html')
    
# Página del Kandra
@app.route('/kandra')
def kandra():
    return render_template('Kandra.html')
    
# Página del Rastreador
@app.route('/rastreador')
def rastreador():
    return render_template('rastreador.html')
 
# Página del Actor
@app.route('/actor')
def actor():
    return render_template('actor.html')
    
# Página del Medico
@app.route('/medico')
def medico():
    return render_template('medico.html')
    
# Página del Comerciante
@app.route('/comerciante')
def comerciante():
    return render_template('comerciante.html')
    
# Página del Guardia
@app.route('/guardia')
def guardia():
    return render_template('guardia.html')
    
# Página del Lore primera
@app.route('/lore1')
def lore1():
    return render_template('lore.html')
    
# Página del Lore segunda
@app.route('/lore2')
def lore2():
    return render_template('lore2.html')
    
    


if __name__ == '__main__':
    app.run(debug=True)
