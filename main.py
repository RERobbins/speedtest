"""My main speedtest module."""

from speedtest import Speedtest
from pprint import pprint

def internet_speed ():
    """Return speed test results as a dictionary."""
    st = Speedtest()  
    download=st.download()
    upload=st.upload()
    results=st.results.dict()

    return ({'timestamp': results['timestamp'], 'download_bps': download, 'upload_bps': upload, 'ping_ms': results['ping']})

pprint (internet_speed())
