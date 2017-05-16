import tweepy
import json

consumer_key="FGSXHe947cqCTM5FXU2LNREMA"
consumer_secret="HR1hgjTUn8gpjwIjF6wtOIpodl4qJtmBhFrb68D0JHyIanroFY"
access_token="356349488-Knapgfw83adaXsZj9z1SpkE81nW2gtSwJrPqTkaF"
access_token_secret="q4xa5HqKRCP1JsFcgGgq1HKxNp9SKijVyYYAwoaUMlo9a"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

documento = open('/home/jackson/Documentos/Sbc/datos.txt', 'a')

dato= api.user_timeline(screen_name='LaVanguardia', count=5, incude_rts=False)
# print dato
print "================="
for d in dato:
  print ("tweet: "+ d.text)
  print ('Retweet: '+ str(d.retweet_count))
  print('Favoritos: '+ str(d.favorite_count))
  print('Fecha: '+str( d.created_at))
  print ("descrpition: "+d.user.description)
  print ("Lacacion: "+ d.user.location)
  print ("Url usuario: "+ d.user.url)



#print dato
print "---------" 

# data= tweepy.Cursor(api.search,q='@eluniversocom').items(10)

# documento = open('/home/jackson/Documentos/Sbc/datos.txt', 'a')

# for tweet in data:
#     twt=tweet.text
#     twt.encode('utf-8')
#     print('Tweet por: @' + tweet.user.screen_name)
#     print('Tweet: '+ twt )
#     print ('Retweet: '+ str(tweet.retweet_count))
#     print('Favoritos: '+ str(tweet.favorite_count))
#     documento.write('Tweet por: '+tweet.user.screen_name + '\n')
#     documento.write('Tweet: '+twt.encode("utf-8")+'\n')
#     documento.write('Retweet: '+str(tweet.retweet_count)+'\n')
#     documento.write('Favorito: '+str(tweet.favorite_count)+'\n')

documento.close()
