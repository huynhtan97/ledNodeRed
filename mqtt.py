import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))
    
def on_message(client, data, message):
    print("Message topic: ", message.topic)
    
def on_log(client, data, level, buf):
    print("Debug: ", bug)

print("Creating a new client")
client = mqtt.Client("safetyNet")

brokerAddress = "broker.hivemq.com"
brokerPort = 1883

client.on_connect = on_connect
client.on_message = on_message
client.on_log = on_log

client.connect(brokerAddress, brokerPort)

client.subscribe("ledStatus", qos=2)
client.publish("ledStatus", "On")
