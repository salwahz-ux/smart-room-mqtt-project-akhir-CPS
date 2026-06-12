import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "smartroom/#"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Subscriber terhubung ke broker!")
        client.subscribe(TOPIC, qos=1)
        print(f"Subscribe ke topik: {TOPIC}")
        print("Menunggu SEMUA data dari semua sensor dan ruangan...")
    else:
        print(f"Gagal terhubung, kode: {rc}")

def on_message(client, userdata, msg):
    print(f"[PESAN DITERIMA] Topik: {msg.topic} | Data: {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)
client.loop_forever()