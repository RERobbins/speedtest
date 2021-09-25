"""My main speedtest module."""
import subprocess
import json

response = subprocess.Popen('speedtest -f json', shell=True, stdout=subprocess.PIPE).stdout.read()

response_dict = json.loads(response)

print (f"Timestamp: {response_dict['timestamp']}")
print (f"Ping: jitter: {response_dict['ping']['jitter']} latency: {response_dict['ping']['latency']}")
print (f"Download: bandwidth: {response_dict['download']['bandwidth']}")
print (f"Download: bytes: {response_dict['download']['bytes']}")
print (f"Download: elapsed: {response_dict['download']['elapsed']}")
print (f"Upload: bandwidth: {response_dict['upload']['bandwidth']}")
print (f"Upload: bytes: {response_dict['upload']['bytes']}")
print (f"Upload: elapsed: {response_dict['upload']['elapsed']}")



