# Linux Server Administration & Deployment Assessment

## 📌 Project Overview
End-to-end implementation of Linux system management, network security hardening, and a secure cloud deployment pipeline.

---

## 🛠️ Phase 1: Linux Essentials & System Management
- **CLI & File Management:** Handled file permissions (`chmod 600`), ownership, and log monitoring via `tail -f`.
- **Users & Groups:** Created non-root administrative users and configured sudo privileges.
- **Process Management:** Monitored system daemons and managed services using `systemd`.
- **SSH Hardening:** Configured key-based authentication (`ssh-keygen`) and disabled password login in `/etc/ssh/sshd_config`.

---

## 🔒 Phase 2: Networking & Security Essentials
- **Firewall Setup (`ufw`):**
  ```bash
  sudo ufw default deny incoming
  sudo ufw allow OpenSSH
  sudo ufw allow 80/tcp
  sudo ufw allow 443/tcp
  sudo ufw enable
