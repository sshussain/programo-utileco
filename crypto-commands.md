The page contains often used crypto commands. I have tested these commands on Mac and *nix OS.

## NOTES

Key Formats: 

- *PEM* is plain text

- *CRT* is binary

Private key __cannot__ be generated from a private key.

Public key can be generated from a private key. This is possible as private key has enough data (modulus and public exponent), to compute public key.

## OpenSSL

#### Create private-public key pair

```shell
openssl genrsa -out private_key.pem 2048
openssl rsa -pubout -in private_key.pem -out public_key.pem
```

#### Convert private key from PEM to pk12 format
```shell
openssl pkcs12 -nocerts -out private_key.p12 -in private_key.pem
```

#### Convert certificate PEM file to CRT format
```shell
openssl x509 -outform der -in ca.pem -out ca.crt
```

#### Decode PEM formatted certificate

```shell
openssl x509 -in my-cert.crt -text -noout
```

#### Decode DER formatted certificate

```shell
openssl x509 -in my-cert.der -inform der -text -noout
```

#### Verify certificate matches key

To quickly make sure the files match, display the modulus value of each file:

```shell
openssl rsa -noout -modulus -in FILE.key
openssl req -noout -modulus -in FILE.csr
openssl x509 -noout -modulus -in FILE.cer
```
If everything matches (same modulus), the files are compatible (but this does not guaranty the private key is valid). If not, one of the file is not related to the others.
 
## ssh-keygen

#### Create private-public key pair for SSH

`ssh-keygen`

#### Extract public key from given private key

`ssh-keygen -y -f mykey.pem > mykey-ssh.pub`
