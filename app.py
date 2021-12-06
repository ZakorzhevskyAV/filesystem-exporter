from flask import Flask
from  prometheus_client import Gauge
import os

app = Flask(__name__)
labels = os.environ.get('MONITORING_LABELS')
labels = labels.split(';')
labels_list = list()
for item in labels:
    if '=' in item:
        label = item.split('=')
        labels_list.append(label[1])

g = Gauge(str(labels_list[0]), 'Catalog metrics')
g.set(os.path.getsize(os.environ.get('MONITORING_PATH')))

@app.route('/metrics')
@g.track_inprogress()
def metrics():
    pass
