import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPICS = [
    ("smartroom/livingroom/temperature", 1),
    ("smartroom/livingroom/humidity", 1),
    ("smartroom/livingroom/light", 1)
]

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Subscriber terhubung ke broker!")
        client.subscribe(TOPICS)
        print("Subscribe ke topik:")
        for topic, qos in TOPICS:
            print(f"  - {topic} | QoS: {qos}")
    else:
        print(f"Gagal terhubung, kode: {rc}")

def on_message(client, userdata, msg):
    print(f"[PESAN DITERIMA] Topik: {msg.topic} | Data: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)
client.loop_forever()