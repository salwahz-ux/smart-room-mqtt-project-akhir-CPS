import paho.mqtt.client as mqtt
import random
import time

BROKER = "localhost"
PORT = 1883
TOPIC = "smartroom/livingroom/temperature"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Publisher terhubung ke broker!")
    else:
        print(f"Gagal terhubung, kode: {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.connect(BROKER, PORT)
client.loop_start()

print("Mulai mengirim data suhu ruang tamu...")
try:
    while True:
        suhu = round(random.uniform(20.0, 35.0), 2)
        pesan = f"Suhu: {suhu} °C"
        client.publish(TOPIC, pesan, qos=0)
        print(f"[TERKIRIM] {pesan}")
        time.sleep(2)
except KeyboardInterrupt:
    print("Publisher dihentikan.")
    client.loop_stop()
    client.disconnect()