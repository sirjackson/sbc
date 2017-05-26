#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import tweepy
import json
import MySQLdb

consumer_key="FGSXHe947cqCTM5FXU2LNREMA"
consumer_secret="HR1hgjTUn8gpjwIjF6wtOIpodl4qJtmBhFrb68D0JHyIanroFY"
access_token="356349488-Knapgfw83adaXsZj9z1SpkE81nW2gtSwJrPqTkaF"
access_token_secret="q4xa5HqKRCP1JsFcgGgq1HKxNp9SKijVyYYAwoaUMlo9a"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


DB_HOST='localhost'
DB_USER='root'
DB_PASS='080066917'
DB_NAME='sbc_tweets_diaros'


def query_db(query=''): 
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
 
    conn = MySQLdb.connect(*datos,charset='utf8mb4',use_unicode=True) 
    cursor = conn.cursor()         
    cursor.execute(query)          
 
    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()    
    else: 
        conn.commit()              
        data = None 
 
    cursor.close()                 
    conn.close()                   
    return data







def extrator (diarios):
    dato= api.user_timeline(screen_name=diarios, count=100, incude_rts=False)
    for d in dato:
        d.text.encode('utf-8')
        twext= d.text.replace("'","")
        print ("tweet: "+ twext)
        print ('Retweet: '+ str(d.retweet_count))
        print('Favoritos: '+ str(d.favorite_count))
        print('Fecha: '+str( d.created_at))
        print ("descrpition: "+d.user.description)
        print ("Lacacion: "+ d.user.location)
        print ("Url page usuario: "+ d.user.url)
        print ("Nombre: "+ d.user.name)
        print ("Nick: "+ d.user.screen_name)
        tokens= d.text.split(" ")
        posiciones=len(tokens) 
        unot=tokens[posiciones-1]
        print("url noticia: " + tokens[posiciones-1])
        #insert tweets
        insert=("INSERT INTO publicaciones" 
        "(TWEET, RETWEET, FAVORITOS, FECHA, URLNOTICIA, USERNICK)"
        "VALUES ('%s','%s','%s','%s','%s','%s')"%(twext, d.retweet_count, d.favorite_count, d.created_at, unot, d.user.screen_name))
        query_db(insert)

        # insert usuarios
        usuario=d.user.screen_name
        #comprobarUsuario(usuario)
        if comprobarUsuario(usuario)==False:
            print "Usuario nuevo insertado"
            insert_user=("INSERT INTO diarios"
            "(USERNICK,NOMBRE, UBICACION, URL)"
            "VALUES('%s','%s','%s','%s')"%(d.user.screen_name,d.user.name,d.user.location,d.user.url))
            query_db(insert_user)
        else:
            print "El usuario ya existe"
        
        print "operacion exitosa"

def comprobarUsuario(user):
    consulta="SELECT USERNICK, NOMBRE FROM diarios WHERE USERNICK='%s'"%user
    res=query_db(consulta)
    r_use=str(res)
    if (r_use=="()"):
        return False
    else:
        for r in res:
            nick=r[0]
            print ("user base:" + nick)
        if (user==nick):
        # print "el usuario ya existe"
            return True
        else:
            print "el usuario no existe"
            return False

api = tweepy.API(auth)

diarios=["LaVanguardia","el_pais","MailOnline","abc_es","LANACION","nytimes"]
#diarios=["LANACION","nytimes"]


for i in range(len(diarios)):
    extrator(diarios[i])
    print "-=-=-=-=-=-="