#twitter post

# Beckett Nikitas

from twython import Twython

consumer_key = 'VD9uUIdeYYaAfhiEVFL1185DZ'
consumer_secret = 'kofk91vXJkFlsqbNLh3s7GUbuTOzqd1JpNpFA9qX2mDQTR6rhG'
access_token = '1141880993487495173-g1WOpZ4yrC8dco40AhLGnouj4fqNjW'
access_token_secret = 'tyuG1Nm3VNCQrJYv3HsmslYBIysZ0ibJCNTPqYsJsuoA1'


twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)


message = "hello this was code a second a go ,Beck"
twitter.update_status(status=message)
print("tweeted: %s" % message)


