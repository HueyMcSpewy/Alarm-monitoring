import ujson

 # Yes, I do know this is not very neat but i am lazy
 
data = ujson.loads(config) 
# Wifi 
ssid = data["wifi"]["ssid"] 
password = data["wifi"]["password"] 
# Pushover 
pushoverenbl = data ["pushover"]["enable"] 
userkey = data ["pushover"]["userkey"] 
token = data["pushover"]["token"] 
# pins 
alarmpin = data["pins"]["alarm"] 
armpin = data["pins"]["arm"] 
# mqtt 
mserver = data["mqtt"]["server"] 
mclientid = data["mqtt"]["client_id"] 
armtopic = data["mqtt"]["state_topics"]["arm"] 
alarmtopic = data["mqtt"]["state_topics"]["alarm"]