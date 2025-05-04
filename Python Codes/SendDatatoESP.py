import paho.mqtt.client as mqtt
import json
import ssl
import time
import _thread


# Defining on_connect function
##### On Connect
def on_connect(client, userdata, flags, rc):
    print("Connected to AWS IoT:" + str(rc))
    client.subscribe(TOPIC)

### on Subscribe message
def on_message(client, userdata, msg):
    # print(f"Message received on topic {msg.topic}")
    payload = json.loads(msg.payload.decode('utf-8'))
    print(f"Payload: {payload}")
# Defining client

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


# cerificate
ca_certs_path = 'D:\linux\IoT AWS\python_certificate\AmazonRootCA1.pem'
cert_path = 'D:\linux\IoT AWS\python_certificate\certificate.pem.crt'
privateKey_path  = 'D:\linux\IoT AWS\python_certificate\private_key.pem.key'
TOPIC = 'esp_test/pub'
client.tls_set(ca_certs=ca_certs_path, certfile=cert_path, keyfile=privateKey_path, tls_version=ssl.PROTOCOL_SSLv23)
client.tls_insecure_set(True)
client.connect("ak40v1wcytj5n-ats.iot.ap-southeast-2.amazonaws.com",8883,60)

def publishData(txt):
    while (True):
        # if lamp1 == True:
        #     msg = "ON1"
        #     lamp1 = False
        # else:
        #     msg = "OFF1"
        #     lamp1 = True
        # print(msg)
        msg = input()
        client.publish("py/pub", payload=msg, qos=0, retain=False)
        time.sleep(2)   

# Create a new thread to publish data
_thread.start_new_thread(publishData,("Spin-up new Thread...",))

# loop publishing data forever and you can not stop it, Just terminate the running
client.loop_forever()