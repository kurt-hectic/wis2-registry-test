import pytest
import requests
import ssl
import time


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
