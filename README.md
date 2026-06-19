# 🛡️ Türkiye İçin İmei Oluşturma Pro — Mnk's V4 (Anti-Crack Pro)

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-Unlicense-green?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-Anti--Tamper%20Enforced-red?style=for-the-badge)

An advanced, secure, and production-grade **Turkish (BTK) Network Compatible IMEI Generation Tool** designed for hardware testing and simulation environment validation. Built with a robust cryptographic **Anti-Tamper Layer** to prevent unauthorized source code modification and cracking attempts.

---

## 🚀 Key Features

* **📦 Zero Configuration:** Instantly runs and generates mathematically flawless, structurally valid IMEIs.
* **⚡ Multi-Brand TAC Pools:** Features authentic Type Allocation Code (TAC) databases for top brands like Apple, Samsung, Xiaomi, Huawei, Oppo, Realme, and POCO.
* **🌐 Dynamic BTK Status Simulator:** Analyzes and predicts real-time Turkish Telecommunication Authority (BTK) network registry cycles, tax bands, and cloning risk vectors.
* **🔏 Anti-Tamper & Self-Locking System:** Constantly monitors its own code signature hash. If tampering or cracking is detected, the script permanently locks itself down.
* **💾 Timestamped Batch Exporting:** Safely writes unique generated lists into dynamic `.txt` formats without including visual telemetry strings.

---

## 📸 Application Workflow & Interface

### 1. Security Authentication & Handshake
When initialized, the software challenges the user with a cryptographic handshake request requiring the signature key.

![Initial Security Authentication Sequence](ss1)  
*Figure 1: Initial Security Authentication Sequence (ss1)*

### 2. Batch Generation & Live Network Telemetry
Upon entering valid criteria, the application multi-threads unique Luhn-validated structures and maps them directly to their corresponding network behaviors.

![Real-time Output Matrix & Risk Allocation Mapping](ss3)  
*Figure 2: Real-time Output Matrix & Risk Allocation Mapping (ss3)*

### 3. Timestamped Persistent Storage Export
After generation, the software handles system I/O routines to output filtered results seamlessly into isolated workspace files.

![Structured Batch Output and File Persistence](ss2)  
*Figure 3: Structured Batch Output and File Persistence (ss2)*

---

## 🛠️ Code Architecture & Deep Dive

The architecture is written entirely natively in Python, keeping internal performance high without sacrificing security boundaries.

### 🔒 Cryptographic Anti-Tamper Layer
The foundation relies on an integrated execution monitor using runtime reflective verification:
* **AES-XOR Static Salting:** The core authorization variable `ENCRYPTED_LIC_KEY` is obscured at rest via a standard bitwise sequence shift (`SECRET_SALT = 0x5A`) combined with Base64 layout nesting.
* **Self-File Fingerprinting:** The `verify_code_integrity()` block opens its own local memory allocation `__file__` on initialization. It inspects strings to ensure absolute structure equality.
* **Hard Lock State:** If a single character or byte in the file hash is tampered with, the logic breaks containment, drops a hidden persistent binary payload `.sys_lock_dat`, and blocks future operations indefinitely.

### 📐 Luhn Mathematical Compliance
Every mobile station equipment identifier requires strict execution of the **Luhn Algorithm (Mod 10 Checksum)** to pass cellular tower handshakes:

$$\text{Checksum} \equiv \sum_{i=1}^{n} d_i \pmod{10}$$

The tool maps strings into integers, isolates every secondary index position, multiplies it by 2, resolves digit sums, and derives the necessary 15th character boundary via `calc_check_digit()` dynamically.

### 📊 Cellular Allocation Data Map
* **TAC (Type Allocation Code):** The first 8 digits representing targeted hardware models.
* **SNR (Serial Number Range):** Isolated middle 6 digits randomized to eliminate repetitive collisions via unique internal set hashing (`set()`).

---

## 💻 Installation & Quick Start

Ensure your operating system environment includes Python 3.8+ and standard dependencies:

```bash
# Clone or move your script into the workspace directory
cd tr-imei

# Install essential color-mapping terminal utilities
pip install colorama

# Run the secure binary application
python imei.py
