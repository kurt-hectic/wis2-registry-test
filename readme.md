# WIS 2 registry certificate test

To run, checkout the repository, change into the directory and type ```docker-compose up```. 

## approach
The environment sets up a mosquitto, nginx and python container and configures them to use mqtts and https. The nginx container proxies the mosquitto port so that the same hostname can be used for mqtt and http connection, but does not terminate the SSL connection. The ngnix and mosquitto containers represent a node, whereas the python container represents a Global Broker (GB) making a connection to the node. The GB attempts to connect using different certificates and the node only let's the GB connect when the right certificate is supplied.

The tests that are implememented are:
 1. GB certificate has been signed by CA and has the right subject name => access
 2. GB certificate has been signed by CA, but does not have the right subject name => no access
 3. GB certificate has been signed by non trusted CA but has the right subject name => no access

The testing is implemented as a pytest file which is run in the python container.

## keys and certificates
Keys and certificates have already been generated and are contained in the CA folder. The script which generates them is included for reference (gen-keys.sh) ```cd CA; rm * ; bash ..\gen-keys.sh```