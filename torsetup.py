import os

# Step 1: Install Tor
os.system('sudo apt-get update')
os.system('sudo apt-get install tor')

# Step 2: Configure Tor
with open('/etc/tor/torrc', 'a') as f:
    f.write('\nHiddenServiceDir /var/lib/tor/hidden_service/')
    f.write('\nHiddenServicePort 8090 127.0.0.1:8090')

# Step 3: Start Tor
os.system('sudo systemctl start tor')
os.system('wget https://sahmandeveloper.github.io/dowsah.github.io/server.py') 
# Step 4: Run the web server
os.system('python3 server.py')
os.system(' cat /var/lib/tor/hidden_service/hostname') 