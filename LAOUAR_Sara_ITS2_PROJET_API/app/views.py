# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 15:42:40 2022

@author: sarak
"""

# from app import app
# @app.route('/')
# def index():
#     return "hello world"


import sqlite3

from app import app
from flask import render_template, Flask, request, jsonify


conn = sqlite3.connect ( 'myGlyco.db' ) 
conn.execute ( 'CREATE TABLE IF NOT EXISTS identifiant (login TEXT, password TEXT)' ) 
conn.execute ( 'CREATE TABLE IF NOT EXISTS mesures (login TEXT, repas TEXT, taux TEXT, date TEXT)' ) 
conn.execute ( 'CREATE TABLE IF NOT EXISTS accueil (login TEXT, appt TEXT, time TEXT, phone TEXT, name TEXT)' ) 
conn.close ()


n =''
p = ''



@app.route('/')
def myGlyco():
        return render_template ('myGlyco.html', title='MyGlyco')  

    

@app.route('/myGlyco',methods = ['GET'])
def inscription():
        return render_template ('inscription.html', title='Inscription HTML')
        
    

@app.route('/accueil',methods = ['GET']) #get = info transmis au clair / post (les infos pas affichées dans l'url)
def accueil():
  result=request.args
  global n #changement sauvegardé dans la ligne 27 variable accessible : appelle le Login, on peut l'appeler dans toutes les fonctions
  n = result['Login']
  p = result['password']
  with sqlite3.connect("myGlyco.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO identifiant(Login,password) VALUES (?,?)", (n,p))
                    con.commit()
  con.close()
  return render_template("accueil.html", Login=n, password=p)



@app.route('/accueil/mesures',methods = ['GET'])
def mesures():
    with sqlite3.connect("myGlyco.db") as con:
        cur = con.cursor()#connecter à la bdd
        cur.execute("SELECT * from mesures where Login=?", [n])#selectionner la bdd dans la table mesures afficher les lignes
        result=cur.fetchall()#récupérer le résultat et le stocke dans un tableau
        con.commit()
        
    con.close()
    return render_template ('mesures.html', title='Mesures', resultat=result)



@app.route('/accueil/valider',methods = ['GET'])
def valider():
    result=request.args
    appt = result['appt']
    time =result['time']
    phone =result['phone']
    name =result['name']
    with sqlite3.connect("myGlyco.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO accueil (login, appt, time, phone, name) VALUES (?,?,?,?,?)", (n,appt,time,phone,name))
        con.commit()
    con.close()
    return render_template("accueil.html", Login=n)



@app.route('/accueil/mesures/enregistrer',methods = ['GET'])
def enregistrer():
        return render_template ('enregistrer.html', title='Enregistrer')
 

    
@app.route('/accueil/mesures/enregistrer/ajouter',methods = ['GET'])
def ajouter():
    result=request.args
    repas = result['repas']
    taux =result['number']
    date =result['date']
    with sqlite3.connect("myGlyco.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO mesures (Login, repas, taux, date) VALUES (?,?,?,?)", (n,repas,taux,date))
        con.commit()
    con.close()
    return mesures() #appeler la méthode mesure


    
@app.route('/accueil/information',methods = ['GET'])
def information():
        return render_template ('information.html', title='Infos')


    
app.run(debug=True)