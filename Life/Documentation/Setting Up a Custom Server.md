# Project Wildspace

### Set Up OVH
- Do not use EN servers
- Buy and log in - do not disable ssh obviously
- Install packages
- If using debian, sudo install nodejs and npm before running
- npm install
- Run development and navigate to the IP:3000 to test

### Server Stuff
- Set an A Record to the IP and a sub domain of WWW
- Put the server file in there and replace all of the domains where they belong
```js
const next = require('next');
const https = require('https');
const { parse } = require('url');
const fs = require('fs');


const port = 443;
const dev = false;
const app = next({ dev });
const handle = app.getRequestHandler();

const redirectToWWW = (req, res) => {
    const redirectUrl = `https://www.lootcode.dev${req.url}`;
    res.writeHead(301, { 'Location': redirectUrl });
    return redirectUrl;
};

let options = {
    key: fs.readFileSync('/etc/letsencrypt/live/www.lootcode.dev/privkey.pem', 'utf8'),
    cert: fs.readFileSync('/etc/letsencrypt/live/www.lootcode.dev/cert.pem', 'utf8'),
    ca: fs.readFileSync('/etc/letsencrypt/live/www.lootcode.dev/chain.pem', 'utf8')
};

app.prepare().then(() => {
    https.createServer(options, (req, res) => {
        const parsedURL = parse(req.url);
        if (req.headers.host != 'www.lootcode.dev') {
            redirectToWWW(req, res); // Redirect to www.lootcode.dev
        } else {
            handle(req, res, parsedURL); // Handle request with Next.js
        }
    }).listen(port, err => {
        if (err) throw err
        console.log(`> Ready on localhost:${port}`)
    })
});
```
- Download Certbot and run the commands
```
sudo apt install certbot
sudo certbot certonly --standalone -d {domain}
```
- Add in the Build Script in UpdateServer.sh
- Run Sudo Chmod 777 UpdateServer.sh
```
#!/bin/bash 
git pull 
mv server.cjs ../server.cjs 
sudo npm run build 
mv ../server.cjs server.cjs 
sudo pm2 restart server
```
- Install pm2 with sudo npm install pm2@latest -g and run sudo pm2 start server.cjs

### MariaDB
```
sudo apt install mariadb-server
sudo mysql_secure_installation
sudo mariadb -u root -p
create database db;
create user 'access'@'%' identified by 'SR8DZWVqWKDb';
grant all on * to 'access'@'%';


# edit /etc/mysql/mariadb.conf.d/50-server.cnf to set bind_address = **

sudo systemctl restart mariadb

```

Use localhost with the db?


### SQL
```
sudo wget https://dev.mysql.com/get/mysql-apt-config_0.8.24-1_all.deb
sudo chmod 777 mysql-apt-config_0.8.24-1_all.deb
sudo apt install ./mysql-apt-config_0.8.24-1_all.deb

sudo wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1-1ubuntu2.1~18.04.23_amd64.deb

sudo dpkg - i libssl + TAB
sudo apt install mysql-server

mysql -u root -p


```
- https://tecadmin.net/mysql-allow-remote-connections/#google_vignette
- Modify the config at /etc/mysql/my.cnf and change bind-address to *
- Create user 'access'@'%' identified by '{password}';
- grant all on * to 'access'@'%';
- Create database db;
- Put in the env DATABASE_URL='mysql://access:48DxhTEqwfGt@15.204.288.101:3306/wildspace'