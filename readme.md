## Steps to create a self-signed certificate using OpenSSL

### Creating the Certificate Authority's Certificate and Keys

Step1. Generate a private key for the CA:
openssl genrsa 2048 > ca-key.pem


Step2. Generate the X509 certificate for the CA:
openssl req -new -x509 -nodes -days 365000 \
   -key ca-key.pem \
   -out ca-cert.pem

Fill all the details

### Creating the Server's Certificate and Keys

Step1. Generate the private key and certificate request:
openssl req -newkey rsa:2048 -nodes -days 365000 \
   -keyout server-key.pem \
   -out server-req.pem

Step2. Generate the X509 certificate for the server:
openssl x509 -req -days 365000 -set_serial 01 \
   -in server-req.pem \
   -out server-cert.pem \
   -CA ca-cert.pem \
   -CAkey ca-key.pem

### Creating the Client's Certificate and Keys

Step1. Generate the private key and certificate request:
openssl req -newkey rsa:2048 -nodes -days 365000 \
   -keyout client-key.pem \
   -out client-req.pem

Step2. Generate the X509 certificate for the client:
openssl x509 -req -days 365000 -set_serial 01 \
   -in client-req.pem \
   -out client-cert.pem \
   -CA ca-cert.pem \
   -CAkey ca-key.pem

### Verifying the Certificates

Step1. Verify the server certificate:
openssl verify -CAfile ca-cert.pem \
   ca-cert.pem \
   server-cert.pem

Step2. Verify the client certificate:
openssl verify -CAfile ca-cert.pem \
   ca-cert.pem \
   client-cert.pem







