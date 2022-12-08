import pytest
import requests
import ssl
import time

import paho.mqtt.client as mqtt

data_received = False

def test_certificate_and_subject():

    r = requests.get("https://node-ch.wis2.wmo.int", 
        verify="/usr/local/share/ca-certificates/wisca.crt", 
        cert=('./gb_fr.crt', './gb_fr.key')
    )
    assert r.status_code == 200

def test_fake_certificate_fails():

    r = requests.get("https://node-ch.wis2.wmo.int", 
        verify="/usr/local/share/ca-certificates/wisca.crt", 
        cert=('./gb_fr_fake.crt', './gb_fr.key')
    )
    assert r.status_code == 400

def test_certificate_and_wrong_subject():

    r = requests.get("https://node-ch.wis2.wmo.int", 
        verify="/usr/local/share/ca-certificates/wisca.crt", 
        cert=('./gb_ma.crt', './gb_ma.key')
    )
    assert r.status_code == 401

def setup_mqtt_client(certfile,keyfile):

    client = mqtt.Client()
    client.tls_set(certfile=certfile,
               keyfile=keyfile,
               ca_certs="./wisca.crt",
               cert_reqs=ssl.CERT_REQUIRED,
               tls_version=ssl.PROTOCOL_TLS_CLIENT)
    client.on_message = on_message
    client.connect("node-ch.wis2.wmo.int", 8883)
    client.subscribe("test", qos=1)
    
    client.loop_start()

    time.sleep(2)
    
    client.loop_stop()


def on_message(client, userdata, message):
    global data_received
    
    print("%s %s" % (message.topic, message.payload))
    data_received = message.payload


def test_sub_certificate_and_subject():
    global data_received
    data_received = False

    setup_mqtt_client("./gb_fr.crt","./gb_fr.key")
    
    assert data_received
    
@pytest.mark.filterwarnings("ignore")
def test_sub_fake_certificate():
    global data_received
    data_received = False

    setup_mqtt_client("./gb_fr_fake.crt","./gb_fr.key")
    
    assert not data_received
   


def test_sub_certificate_and_wrong_subject():
    global data_received
    data_received = False

    setup_mqtt_client("./gb_ma.crt","./gb_ma.key")
    
    assert not data_received
   