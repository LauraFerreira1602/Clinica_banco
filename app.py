from flask import Flask, render_template, redirect, url_for, request, session, flash
from sqlalchemy import select

from models import *
from models import Consultas

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route('/')
def index():
    return render_template('base.html')


@app.route('/lista_clientes')
def lista_clientes():
    sql_lista_clientes = select(Cliente)
    resultado_clientes = db_session.execute(sql_lista_clientes).scalars().all()
    lista_clientes = []
    for n in resultado_clientes:
        lista_clientes.append(n.serialize_cliente())
        print(lista_clientes[-1])
    return render_template("lista_clientes.html",
                           lista_clientes=lista_clientes)


@app.route('/novo_cliente', methods=['POST', 'GET'])
def novo_cliente():

    if request.method == 'POST':

        if not request.form['form_Nome1'] or not request.form['form_CPF'] or not request.form['form_telefone'] or not request.form['form_id_cliente']:
            flash("Preencha todos os campos", "error")
        else:
            Nome1 = request.form['form_Nome1']
            CPF = request.form['form_CPF']
            telefone = request.form['form_telefone']
            id_cliente = request.form['form_id_cliente']

            animal = Animal(Nome1=Nome1, CPF=CPF, telefone=telefone, idCliente1=int(id_cliente))

            animal.save()
            db_session.close()
            flash("Novo Cliente cadastrado com sucesso!", "success")
            return redirect(url_for('lista_clientes'))
    return render_template('novo_cliente.html')



@app.route('/lista_animais')
def lista_animais():
    sql_lista_animais = select(Animal)
    resultado_animais = db_session.execute(sql_lista_animais).scalars().all()
    lista_animais = []
    for n in resultado_animais:
        lista_animais.append(n.serialize_animal())
        print(lista_consultas[-1])
    return render_template("lista_animais.html",
                           lista_animais=lista_animais)


@app.route('/novo_animal', methods=['POST', 'GET'])
def novo_animal():

    if request.method == 'POST':

        if (not request.form['form_nome_animal'] or not request.form['form_raca1'] or not request.form['form_anoNasci1']
                or not request.form['form_idcliente']):
            flash("Preencha todos os campos", "error")
        else:
            nome_animal = request.form['form_nome_animal']
            raca1 = request.form['form_raca1']
            anoNasci1 = request.form['form_anoNasci1']
            idCliente1 = request.form['form_idcliente']

            animal = Animal(nome_animal=nome_animal, raca1=raca1, anoNasci1=int(anoNasci1), idCliente1=int(idCliente1))

            animal.save()
            db_session.close()
            flash("Animal cadastrado com sucesso!", "success")
            return redirect(url_for('lista_animais'))
    return render_template('novo_animal.html')



@app.route('/lista_consultas')
def lista_consultas():
    sql_lista_consultas = select(Consultas)
    resultado_consultas = db_session.execute(sql_lista_consultas).scalars().all()
    lista_consultas = []
    for n in resultado_consultas:
        lista_consultas.append(n.serialize_consulta())
        print(lista_consultas[-1])
    return render_template("lista_consultas.html",
                           lista_consultas=lista_consultas)


@app.route('/nova_consulta', methods=['POST', 'GET'])
def nova_consulta():

    if request.method == 'POST':

        if not request.form['form_motivo_id1'] or not request.form['form_hora1'] or not request.form['form_minuto'] or not request.form['form_data1'] or not request.form['form_idAnimal1'] or not request.form['form_idVeterinario']:
            flash("Preencha todos os campos", "error")
        else:
            motivo_id1 = request.form['form_motivo_id1']
            hora1 = request.form['form_hora1']
            minuto = request.form['form_minuto']
            data1 = request.form['form_data1']
            idAnimal1 = request.form['form_idAnimal1']
            idVeterinario1 = request.form['form_idVeterinario1']

            consulta = Consultas(motivo_id1=int(motivo_id1), hora1=int(hora1), minuto=int(minuto), data1=data1, idAnimal1=int(idAnimal1), idVeterinario1=int(idVeterinario1))

            consulta.save()
            db_session.close()
            flash("Consulta cadastrada com sucesso!", "success")
            return redirect(url_for('lista_consultas'))
    return render_template('nova_consulta.html')

app.run(debug=True)
