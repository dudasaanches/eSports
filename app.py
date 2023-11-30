from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class cadsport:
    def __init__(self, nome, jogo, posicao, ranking):

        self.nome = nome
        self.jogo = jogo
        self.posicao = posicao
        self.ranking = ranking

lista = []
@app.route('/')
def sport():
    return render_template('Sport.html', Titulo="Os competidores: ", ListaSport=lista)

@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo = "Cadastro dos jogadores")


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    jogo = request.form['jogo']
    posicao = request.form['posicao']
    ranking = request.form['ranking']
    obj = cadsport(nome,jogo,posicao,ranking)

    #o append ta colocando as informações na lista
    lista.append(obj)
    return redirect('/')

@app.route('/excluir/<nomesport>', methods=['GET', 'DELETE'])
def excluir(nomesport):
    for i, spt in enumerate(lista):
        #o enumerate está vendo quando itens tem na minha lista
        #se tiver o numero
        if spt.nome == nomesport:
            #apaga ele da lista
            lista.pop(i)
            break

    return redirect('/')

@app.route('/editar/<nomesport>', methods=['GET'])
def editar(nomesport):
    for i, spt in enumerate(lista):
        if spt.nome == nomesport:
            return render_template("Editar.html", sport=spt, Titulo="Alterar")

@app.route('/alterar', methods=['POST', 'PUT'])
def alterar():
    nome = request.form['nome']
    for i, spt in enumerate(lista):
        if spt.nome == nome:
            spt.nome = request.form['nome']
            spt.jogo = request.form['jogo']
            spt.posicao = request.form['posicao']
            spt.ranking = request.form['ranking']
    return redirect('/')


if __name__ == '__main__':
    app.run()
