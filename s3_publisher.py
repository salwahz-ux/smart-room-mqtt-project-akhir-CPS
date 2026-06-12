import paho.mqtt.client as mqtt
import random
import time

BROKER = "localhost"
PORT = 1883

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Publisher terhubung ke broker!")
    else:
        print(f"Gagal terhubung, kode: {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.connect(BROKER, PORT)
client.loop_start()

print("Mulai mengirim data sensor ruang tamu...")
try:
    while True:
        suhu = round(random.uniform(20.0, 35.0), 2)
        kelembapan = round(random.uniform(40.0, 90.0), 2)
        cahaya = round(random.uniform(100.0, 1000.0), 2)

        client.publish("smartroom/livingroom/temperature", f"Suhu: {suhu} °C", qos=1)
        print(f"[TERKIRIM] Suhu: {suhu} °C")

        client.publish("smartroom/livingroom/humidity", f"Kelembapan: {kelembapan}%", qos=1)
        print(f"[TERKIRIM] Kelembapan: {kelembapan}%")

        client.publish("smartroom/livingroom/light", f"Cahaya: {cahaya} lux", qos=1)
        print(f"[TERKIRIM] Cahaya: {cahaya} lux")

        print("---")
        time.sleep(2)
except KeyboardInterrupt:
    print("Publisher dihentikan.")
finally:
    client.loop_stop()
    client.disconnect()