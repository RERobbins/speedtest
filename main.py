"""My test module."""

import pprint
import speedtest
st = speedtest.Speedtest()
download = st.download() / 1000000
upload = st.upload() / 1000000
ping = st.results.dict()['ping']

print (f"Download: {download:.3f} Mb/s  Upload: {upload:.3f} Mb/s Ping: {ping} ms")
