# Dashboard

A highly customisable dashboard for your homelab needs.

Fully automated and fully containerised deployment on most Linux machines using Ansible Galaxy and Docker Compose.

# Current features:
- homarr dashboard
- postgreSQL database
- redis for caching
- dash for casual system monitoring
- apache HTTPS proxy
- openobserve for more serious monitoring
- mobile push notifications from openobserve alerts
- fail2ban for banning unwanted traffic

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


## TLS

If you dont have certs for tls you can generate self-signed keys by running

```bash
sudo openssl req -x509 -nodes -days 365 \
  -newkey rsa:2048 \
  -keyout ./roles/docker/files/apache-selfsigned.key \
  -out ./roles/docker/files/apache-selfsigned.crt
```

in this directory.

You'll be prompted for info. You can enter dummy values.  
Use the address of the target host when asked for **Common Name (CN)**.

You need to add the certificate to your system's trusted certificates if you're doing this.

Remember to change the values in apache configurations accordingly. Check out "000-default.site" for more

## Fail2Ban

you need to set up your fail2ban jails manually at the moment. 

The configuration files can be found in /opt/fail2ban/config/fail2ban/jail.d and filter.d, after the service has been started at least once


## Current bugs

- On some machines, the playbook fails with no root access as the sudo cache has been emptied on the host machine.  
  **Quick fix**: run any `sudo` command as user `ansible` on the host machine.

- Dashboard web search only works if you configure DuckDuckGo as the default search engine

## TODO

- Fix the sudo cache bug
