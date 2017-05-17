import tweepy
import json

consumer_key="FGSXHe947cqCTM5FXU2LNREMA"
consumer_secret="HR1hgjTUn8gpjwIjF6wtOIpodl4qJtmBhFrb68D0JHyIanroFY"
access_token="356349488-Knapgfw83adaXsZj9z1SpkE81nW2gtSwJrPqTkaF"
access_token_secret="q4xa5HqKRCP1JsFcgGgq1HKxNp9SKijVyYYAwoaUMlo9a"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # retorno en formato json
        decoded = json.loads(data)
        print data
        print"--------------"

        # informacion transformada
        print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        print ''
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print "Todos los tweets:"

    stream = tweepy.Stream(auth, l)
    stream.filter(follow=[5],track=['Venezuela'])
    informacion= open('/home/jackson/Documentos/Sbc/','a')
    informacion.write(data)