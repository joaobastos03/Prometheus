from flask import Flask, request, render_template
import pandas as pandas
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method =='POST':
        usuario = request.form['usuario']
        numero = request.form['numero']
        email = request.form['email']

        dados = {
            'Usuário': [usuario],
            'Numero': [numero],
            'Email': [email]
        }

        df = pd.DataFrame(dados)
        df.to_csv('dados_usuario.csv', index=False)

        return 'Dados exportados como CSV'

        return render_template('index.html')

if __name__ == '__main__':
    app.run()
