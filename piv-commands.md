This page contains instructions to interact with PIV card.

See https://piv.idmanagement.gov/engineering/ssh/ for more information.

I installed *OpenSC* open-source tool on Mac. There may be similar tools for Linux and Windows OS.

### Install OpenSC

`brew install opensc`

### Test OpnSC Installation

Insert PIV card in Smart card reader. Run the following command. The command will go through all keys on PIV card; and it
will prompt for PIN for each key.

`pkcs11-tool -login --test`

### List all PIV keys

`pkcs15-tool --list-public-keys`

### Display Smart card PIV Auth public key

`pkcs15-tool --read-ssh-key  01`

### SSH using PIV card

`ssh -I /usr/local/lib/opensc-pkcs11.so <user>@<remote_host>`


## Using MacOS utilities

MacOS provides native tools to read PIV card.

### Read Public key from PIV card

1. Insert PIV card into reader and login

2. Run the following command in your terminal program

     `security find-certificate | grep keychain | cut -d : -f2`

3. Take the output of the previous command (including the quotes) and replace $KEYCHAIN in the next command

     `ssh-keygen -i -m pkcs8 -f <(security find-certificate -p $KEYCHAIN | openssl x509 -noout -pubkey)`
     
Output of this command (including the ssh-rsa part) is your PIV SSH public key.
