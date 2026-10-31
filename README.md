1. LINUX CLI COREA. 

File System & Permissions:

[ pwd, ls -la, cd, mkdir -p, touch, cp, mv, rm -rf
cat, less, grep -r, find / -name, chmod, chown
# Permissions: r=4, w=2, x=1
chmod 755 file.sh      # owner rwx, others rx
chown user:group file
ls -l  # -rw-r--r-- = 644 ]

B. Users, Groups:

[sudo adduser devuser
sudo usermod -aG sudo devuser
sudo groupadd developers
sudo usermod -aG developers devuser
id devuser
cat /etc/passwd]

C. Process & Service Management:

[ps aux | grep nginx
top / htop
kill -9 <PID>
systemctl status nginx
systemctl enable --now nginx
journalctl -u nginx -f]

D. SSH Keys - Secure Access:

[# On YOUR laptop:
ssh-keygen -t ed25519 -C "my-laptop"
# Copy public key to server
ssh-copy-id ubuntu@<SERVER_IP>
# Or manually: cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
# On server: disable password auth
sudo nano /etc/ssh/sshd_config
# Set: PasswordAuthentication no, PermitRootLogin no
sudo systemctl restart sshd]

2. NETWORKING & SECURITY:

A. IP Addressing:

[ip addr show
ip route
ping 8.8.8.8
traceroute google.com]

B. DNS:

[cat /etc/resolv.conf
nslookup google.com
dig google.com
# Setup local hostname
sudo hostnamectl set-hostname web-server-01]

C. Ports & Connectivity:

[ss -tulpn | grep LISTEN
netstat -tulpn
curl -v http://localhost:80
telnet <IP> 22]

D. Firewalls:

[# UFW (Ubuntu)
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable

# Security Group Concept (Cloud):
# In AWS/Azure Console - this is your cloud firewall
# Allow: 22 (SSH) only from YOUR IP, 80/443 from 0.0.0.0/0]

3. DEPLOY A LINUX SERVER - End to End Project:

Step 1: Create VMOS: Ubuntu 22.04 LTSType: t2.micro / B1sCreate new Key Pair -> download .pemSecurity Group: Open 22, 80, 443

Step 2: Configure Linux:

[ssh -i key.pem ubuntu@<PUBLIC_IP>
sudo apt update && sudo apt upgrade -y
sudo adduser appuser
sudo usermod -aG sudo appuser]

Step 3: Secure Access:

[# Setup SSH key auth for appuser as shown above
sudo ufw allow OpenSSH
sudo ufw enable
# Setup fail2ban
sudo apt install fail2ban -y]

Step 4: Deploy a Service - Nginx Web Server:

[sudo apt install nginx -y
echo "<h1>Server Deployed by $(hostname)</h1>" | sudo tee /var/www/html/index.html
sudo systemctl enable --now nginx]

Step 5: Test Connectivity:

[# From server
curl localhost
ss -tlnp | grep 80

# From your laptop
curl http://<PUBLIC_IP>
nmap <PUBLIC_IP> -p 22,80,443
# Check in browser: http://<PUBLIC_IP>]
