import paho.mqtt.client as mqtt
import json
import ssl
import time
import _thread


# Defining on_connect function

def on_connect(client, userdata, flags, rc):
    print("Connected to AWS IoT:" + str(rc))
# Defining client

client = mqtt.Client()
client.on_connect = on_connect

# cerificate
client.tls_set(ca_certs='D:\linux\IoT AWS\python_certificate\AmazonRootCA1.pem', certfile='D:\linux\IoT AWS\python_certificate\certificate.pem.crt', keyfile='D:\linux\IoT AWS\python_certificate\private_key.pem.key', tls_version=ssl.PROTOCOL_SSLv23)
client.tls_insecure_set(True)
client.connect("ak40v1wcytj5n-ats.iot.ap-southeast-2.amazonaws.com",8883,60)

def publishData(txt):
    print(txt)
    ctr = 1
    while (True):
        msg = "Testing" + str(ctr)
        print(msg)
        client.publish("py/pub", payload=json.dumps({"msg": msg}), qos=0, retain=False)
        ctr = ctr + 1

        time.sleep(5)
        
_thread.start_new_thread(publishData,("Spin-up new Thread...",))
client.loop_forever()
print("end of publishing")
