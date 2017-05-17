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
 
    conn = MySQLdb.connect(*datos,charset='utf8',use_unicode=True) 
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



api = tweepy.API(auth)
dato= api.user_timeline(screen_name='LaVanguardia', count=1, incude_rts=False)
#print dato
for d in dato:
  d.text.encode('utf-8')
  print ("tweet: "+ d.text)
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
  utweet=tokens[posiciones-1]
  unot=tokens[posiciones-2]
  print("url tweet: "+ tokens[posiciones-1])
  print("url noticia: " + tokens[posiciones-2])
  print "---------" 
  insert=("INSERT INTO publicaciones" 
  "(TWEET, RETWEET, FAVORITOS, FECHA, URLTWEET,URLNOTICIA, USERNICK)"
  "VALUES ('%s','%s','%s','%s','%s','%s','%s') "%(d.text, d.retweet_count, d.favorite_count, d.created_at, utweet, unot, d.user.screen_name))

  query_db(insert)

