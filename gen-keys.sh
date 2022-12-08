# CA key and cert
openssl req  -nodes -new -x509 -subj "/O=WMO/OU=WIS2/CN=registry" -keyout wisca.key -out wisca.crt

openssl req  -nodes -new -x509 -subj "/O=WMO/OU=WIS2/CN=registry" -keyout rouguewisca.key -out rouguewisca.crt

# clients
openssl req  -nodes -new  -subj "/C=CH/O=Meteo Suisse/CN=node-ch.wis2.wmo.int"  -addext "subjectAltName = DNS:node-ch.wis2.wmo.int" -addext "certificatePolicies = 1.2.3.4" -keyout node_ch.key -out node_ch.csr

openssl req  -nodes -new  -subj "/C=FR/O=Meteo France/CN=gb-fr.wis2.wmo.int" -addext "subjectAltName = DNS:gb-fr.wis2.wmo.int" -addext "certificatePolicies = 1.2.3.4" -keyout gb_fr.key -out gb_fr.csr

openssl req  -nodes -new  -subj "/C=CH/O=Direction Nationale de la Meteorologie/CN=gb-ma.wis2.wmo.int"  -addext "subjectAltName = DNS:gb-ma.wis2.wmo.int"  -addext "certificatePolicies = 1.2.3.4" -keyout gb_ma.key -out gb_ma.csr

openssl x509 -req -days 365 -extfile <(printf "subjectAltName=DNS:node-ch.wis2.wmo.int") -in node_ch.csr -CA wisca.crt -CAkey wisca.key -set_serial 01 -out node_ch.crt

openssl x509 -req -days 365 -extfile <(printf "subjectAltName=DNS:gb-fr.wis2.wmo.int") -in gb_fr.csr -CA wisca.crt -CAkey wisca.key -set_serial 01 -out gb_fr.crt

openssl x509 -req -days 365 -extfile <(printf "subjectAltName=DNS:gb-ma.wis2.wmo.int") -in gb_ma.csr -CA wisca.crt -CAkey wisca.key -set_serial 01 -out gb_ma.crt


openssl x509 -req -days 365 -extfile <(printf "subjectAltName=DNS:gb-fr.wis2.wmo.int") -in gb_fr.csr -CA rouguewisca.crt -CAkey rouguewisca.key -set_serial 01 -out gb_fr_fake.crt
