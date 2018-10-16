This page contains instructions to create a self-signed certificate. I used `openssl` on Mac OS. I am sure it will work on *nix and Windows OS.

### Steps

#### Create private key

`openssl genrsa -des3 -out server.key 1024`

#### Remove pass phrase from private key

`openssl rsa -in server.key -out server.pem`

#### Generate Certificate Signing Request (CSR)

`openssl req -new -key server.key -out server.csr`

The fields required in CSR is specified in `/etc/ssl/openssl.cnf`. The `opnssl.cnf` contains questioned asked during CSR creation.

> The location of `openssl.cnf` depends on OS.)

Following questions are asked during CSR creation.
  
> Enter pass phrase for server.key:

> You are about to be asked to enter information that will be incorporated into your certificate request.

> What you are about to enter is what is called a Distinguished Name or a DN.

> There are quite a few fields but you can leave some blank

> For some fields there will be a default value,
  
> If you enter '.', the field will be left blank.

>    Country Name (2 letter code) []:US

>    State or Province Name (full name) []:Virginia

>    Locality Name (eg, city) []:McLean

>    Organization Name (eg, company) []:MyCompany

>    Organizational Unit Name (eg, section) []:

>    Common Name (eg, fully qualified host name) []:localhost

>    Email Address []:suheel.s.hussain@uscis.dhs.gov

>    Please enter the following 'extra' attributes to be sent with your certificate request

>    A challenge password []:challenge

#### Generate Self-signed cert from CSR

The self-signed cert is used only for testing. This cert should not be used in production system. To get an official cert, CSR is sent to certifying authority, like Verisign. It takes approximately a week for certifying authority to approve CSR, and respond with a valid certificate. 

`openssl x509 -req -days 60 -in server.csr -signkey server.key -out server.crt`

Now, private key and self-signed certificate is created.
