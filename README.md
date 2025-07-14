# scraper

If you want to use TSL you can generate a self signed cert by running

sudo openssl req -x509 -nodes -days 365 \
  -newkey rsa:2048 \
  -keyout ./apache/files/apache-selfsigned.key \
  -out ./apache/files/apache-selfsigned.crt

in this directory 

You'll be prompted for info. You can enter dummy values. Use the address of the target host when asked for Common Name (CN)

You need to add the certificate to your system trusted certificates if you're doing this

Current bugs:
  The playbook fails with no root access if the sudo cache has been emptied on the host machine, quickfix: run any sudo command as user ansible on host machine


My setup (nothing to do with the repo just here temporarily)

sudo apt install keychain -y
sudo apt install starship -y

./bashrch
	eval "$(starship init bash)"
	alias run='./run'
	eval "$(keychain --eval id_ed25519)"


keychain



