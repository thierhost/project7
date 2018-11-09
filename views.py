#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask,request,url_for, redirect, render_template, abort
import module
import json
import logging as lg
import os

#lg.basicConfig(level=lg.DEBUG)

app = Flask(__name__)




@app.route('/GrandPy', methods=['GET', 'POST'])

def message():
    if request.method == 'POST':

        msg = request.form['msg']#get msg from the POST

        question = module.parsing(msg)

        print("la quest est : " + msg)
        #below question with stopwords removed.
        print(question.new_sentence)

        url_google = question.google()
        print(url_google)
        url_wiki = question.wiki()
        print(url_wiki)
        #lg.warning(url_wiki)
        wikiblabla = module.wikipedia(url_wiki)
        print(wikiblabla.Pageid)


        dico = {"google": url_google, "wiki": wikiblabla.wikiword()}
        json_data = json.dumps(dico)

        return json_data



@app.route('/')
def ajax():
    return render_template('accueil.html', titre="Bienvenue chez GrandPy !")



#############################


@app.route('/')
def index():
    return "Hello !" + request.path


@app.route('/contact/')
def contact():
    mail = "jean@bon.fr"
    tel = "01 23 45 67 89"
    return "Mail: {} --- Tel: {}".format(mail, tel) + request.path


@app.route('/request/', methods=['GET', 'POST'])
def requete():
    return request.method

@app.route('/contact/<nom>')
def route_perso(nom='truc'):
    return "votre nom est " + nom

    return "Mail: {} --- Tel: {}".format(mail, tel) + request.path

@app.route('/url_for/', methods=['GET', 'POST'])
def urlfor():
    return url_for('route_perso', nom = 'bidule')

@app.route('/google')
def redirection_google():
    #abort(401) display error page (ici non autorise)
    return redirect('http://www.google.fr')



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
