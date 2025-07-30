from flask import Flask, render_template, request, redirect, url_for
import matplotlib
matplotlib.use('Agg')  # ✅ Esto evita errores de "main loop"
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
STATIC_FOLDER = 'static'
GRAFICO_PATH = os.path.join(STATIC_FOLDER, 'grafico.png')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graficar', methods=['POST'])
def graficar():
    etiquetas = request.form.get('etiquetas').split(',')
    valores = list(map(float, request.form.get('valores').split(',')))
    tipo = request.form.get('tipo')

    if len(etiquetas) != len(valores):
        return "Error: El número de etiquetas y valores debe ser el mismo."

    plt.clf()  # Limpia gráfico anterior

    if tipo == 'barras':
        plt.bar(etiquetas, valores, color='skyblue')
    elif tipo == 'linea':
        plt.plot(etiquetas, valores, marker='o', color='green')
    elif tipo == 'pastel':
        plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')

    plt.title("Gráfico generado")
    plt.tight_layout()
    plt.savefig(GRAFICO_PATH)

    return render_template('resultado.html')

if __name__ == '__main__':
    app.run(debug=True)
