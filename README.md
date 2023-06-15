[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11232936&assignment_repo_type=AssignmentRepo)
# Minecraft Secure API
This is the README file for Assignment 3 in Programming Studio 2 (COSC2804).

Please find the attached report in the repo: Group 1 Report - CCA Protection

### Group 01 Video Presentation: https://www.youtube.com/watch?v=AbIlN36BoHU

# Instruction

### Required Installation
```
pip install rsa
```
1) Run Kali-Linux with Oracle VM VirtualBox
2) Start Linux Minecraft Server
3) Run NoPE in Burp Suite Community Edition (Listener: 4712, Server Port: 4711)
4) Run ```mcpi_sec_demo.py``` in Kali terminal

# Mandatory: Student contributions
- Go Chee Kin: 27%
- Evelyn Lie: 30%
- Nicholas Sito: 20%
- Edward Lim Padmajaya: 23%

### Go Chee Kin, s3955624 (Github Username: rmit-kent-go)
- Phase 1:
    - Written summary on the MAC-then-encrypt technique's pros and cons
    - Written report on the RSA algorithm's security features, efficiency, security draw-backs and underlying technical details
- Phase 2:
    - Implement HMAC authentication generation in Python
    - Assist Evelyn in fixing minor bugs for RSA encryption in Python
- Phase 3:
    - Demonstrate an unsecure network between the client and the server on Kali Linux with Burpsuite.
    - Provide an explanation about the changes made into the Java and Python files.

### Evelyn Lie, s3951140 (Github Username: eve-s3951140)
- Phase 1: 
    - Wrote a brief overview of the Encrypt-and-MAC technique along with its pros and cons.
    - Provide a simple and straight-forward explanation and the pros and cons about Asymmetric Encryption and Message Authentication Code (MAC).
- Phase 2:
    - Create a RSA and HMAC key generation in Java to be sent into Python. 
    - Complete Implementation of RSA encryption in Python and decryption in Java using several functions, assisted by Kent in dealing minor bugs.
    - Implement HMAC calculation in Java to be compared with the one generated in Python. If the HMAC value from Python and Java is different, the message will not be decrypted since the authenticity and integrity of the message has been corupted.
- Phase 3:
    - Demonstrate the secure plugin we have implemented in Kali Linux with Burpsuite.

### Edward Lim Padmajaya, s3951140 (Github Username: EdwardLimPadmajaya)
- Phase 1: 
    - Wrote a brief introduction to CCA and basic terminologies.
    - Wrote a brief overview of the Hash-then-Encrypt technique along with its pros and cons.
    - Provide a report on the HMAC's security features, efficiency, security draw-backs and underlying technical details.
    - Provide a comparision report on HMAC-SHA256 compared to other types of HMAC.

### Nicholas Sito, s3951974 (Github Username: nicholassitoRMIT)
- Phase 1:
    - Wrote a summary on the Encrypt-then-MAC method as well as its pros and cons.
    - Wrote a short justification on why we chose this method to be implemented in our project.
- Phase 3:
    - Responsible for editing the video for the assignment.
