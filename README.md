# Dashboard

A customisable dashboard for your homelab needs.

Fully automated and fully containerised deployment on most Linux machines using Ansible Galaxy and Docker Compose.

# Current features:
- homarr dashboard
- postgreSQL database
- redis for caching
- dash for casual system monitoring
- apache HTTPS proxy
- openobserve for more serious monitoring
- mobile push notifications from openobserve alerts

## To run

```bash
chmod -x requirements
./requirements
```

After installation is finished:
```bash
./run
```

*(Note: Right now the autostart module is commented out. Check `site.yml` for more info.)*

## Processor module

The `processor` module is just a basic boilerplate Flask app example of how to add your own stuff to the setup.

## TLS

If you want to use TLS, you can generate a self-signed cert by running:

```bash
sudo openssl req -x509 -nodes -days 365 \
  -newkey rsa:2048 \
  -keyout ./docker/files/apache-selfsigned.key \
  -out ./docker/files/apache-selfsigned.crt
```

in this directory.

You'll be prompted for info. You can enter dummy values.  
Use the address of the target host when asked for **Common Name (CN)**.

You need to add the certificate to your system's trusted certificates if you're doing this.

## Current bugs

- The playbook fails with no root access if the sudo cache has been emptied on the host machine.  
  **Quick fix**: run any `sudo` command as user `ansible` on the host machine.

- Dashboard web search only works if you configure DuckDuckGo as the default search engine

## TODO

- Make TLS optional
- Fix the sudo cache bug
