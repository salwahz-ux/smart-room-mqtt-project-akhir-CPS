import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "smartroom/livingroom/temperature"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Subscriber terhubung ke broker!")
        client.subscribe(TOPIC, qos=0)
        print(f"Subscribe ke topik: {TOPIC}")
    else:
        print(f"Gagal terhubung, kode: {rc}")

def on_message(client, userdata, msg):
    print(f"[PESAN DITERIMA] Topik: {msg.topic} | Data: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)
client.loop_forever()