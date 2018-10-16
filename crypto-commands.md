The page contains often used crypto commands. I have tested these commands on Mac and *nix OS.

## OpenSSL

### Create private-public key pair

```shell
openssl genrsa -out private_key.pem 2048
openssl rsa -pubout -in private_key.pem -out public_key.pem
```

### Convert private key from PEM to pk12 format
```shell
openssl pkcs12 -nocerts -out private_key.p12 -in private_key.pem
```

### Convert certificate PEM file to CRT format
```shell
openssl x509 -outform der -in ca.pem -out ca.crt
```

## ssh-keygen

### Create private-public key pair for SSH

`ssh-keygen`

### Extract public key from given private key

`ssh-keygen -y -f mykey.pem > mykey-ssh.pub`


## NOTES

Key Formats: 

- *PEM* is plain text

- *CRT* is binary

Private key __cannot__ be generated from a private key.

Public key can be generated from a private key. This is possible as private key has enough data (modulus and public exponent), to compute public key.



