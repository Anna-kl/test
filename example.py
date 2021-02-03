from client import ClickHouseClient
from errors import Error as ClickHouseError

def on_progress(total, read, progress):
    print(total,read,progress)

try:
    client = ClickHouseClient('clh.datalight.me:8123/', on_progress=on_progress, user='default', password='YzM4Y2EyN2Q3MDAwMWZkNDc5ZGYyMTVj')
    query = 'SELECT 1'
    result = client.select(query, send_progress_in_http_headers=1)
    print(result.data)
except ClickHouseError as e:
    print(e)
except Exception as e:
    print(e)
