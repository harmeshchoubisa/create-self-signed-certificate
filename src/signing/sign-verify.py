from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.x509 import load_pem_x509_certificate
import base64
import json

# Client side signing of data

# Sample JSON payload to sign
payload_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4"
}

# Convert the dictionary to a JSON string
payload = json.dumps(payload_dict).encode('utf-8')


# Load the private key
with open("/Users/harmeshchoubisa/PycharmProjects/create-self-signed-certificate/src/certs/client-key.pem", "rb") as key_file:
    private_key = load_pem_private_key(key_file.read(), password=None)

# Sign the payload
signature = private_key.sign(
    payload,
    padding.PKCS1v15(),
    hashes.SHA256()
)

# Encode signature in base64 for easy storage or transmission
encoded_signature = base64.b64encode(signature)
print(f"Encoded Signature: {encoded_signature.decode()}")


# Server side verifications, client can supply encoded signature and public certificates to server in the call.

# Load the public certificate and extract the public key
with open("/Users/harmeshchoubisa/PycharmProjects/create-self-signed-certificate/src/certs/client-cert.pem", "rb") as cert_file:
    cert = load_pem_x509_certificate(cert_file.read())
    public_key = cert.public_key()

# Verify the signature
try:
    public_key.verify(
        signature,
        payload,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    print("Verification succeeded: The payload and signature are valid.")
except Exception as e:
    print(f"Verification failed: {e}")
