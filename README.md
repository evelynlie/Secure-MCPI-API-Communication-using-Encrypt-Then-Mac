# Minecraft Secure API using Encrypt Then Mac Approach

A report detailing our research on the four CCA secure techniques is in the repository under Group 1 Report - CCA Protection.

### Group 01 Video Presentation: https://www.youtube.com/watch?v=AbIlN36BoHU

# Instruction
### Required Installation
Since we are using RSA for our encryption method, please install the RSA Python library by running the code below on your terminal. 
```
pip install rsa
```

### How to Run the Program
1) Run KaliLinux with Oracle VM VirtualBox (Windows) or UTM (MacOS).
2) Start Minecraft Server on KaliLinux.
3) Run NoPE in Burp Suite Community Edition (Listener: 4712, Server Port: 4711).
4) Run ```python3 mcpi_sec_demo.py``` in KaliLinux terminal.

# Mandatory: Student contributions
- Evelyn Lie: 30%
- Go Chee Kin: 27%
- Nicholas Sito: 20%
- Edward Lim Padmajaya: 23%

### Evelyn Lie
- Phase 1: 
    - Wrote a brief overview of the Encrypt-and-MAC technique along with its pros and cons.
    - Provide a simple and straightforward explanation and the pros and cons of Asymmetric Encryption and Message Authentication Code (MAC).
- Phase 2:
    - Create an RSA and HMAC key generation in Java to be sent into Python. 
    - Complete Implementation of RSA encryption in Python and decryption in Java using several functions, assisted by Kent in dealing with minor bugs.
    - Implement HMAC calculation in Java to be compared with the one generated in Python. If the HMAC value from Python and Java is different, the message will not be decrypted since the authenticity and integrity of the message have been corrupted.
- Phase 3:
    - Demonstrate the secure plugin we have implemented in Kali Linux with Burpsuite.

### Go Chee Kin (Github Username: rmit-kent-go)
- Phase 1:
    - Written summary of the MAC-then-encrypt technique's pros and cons
    - Written report on the RSA algorithm's security features, efficiency, security draw-backs and underlying technical details
- Phase 2:
    - Implement HMAC authentication generation in Python
    - Assist Evelyn in fixing minor bugs for RSA encryption in Python
- Phase 3:
    - Demonstrate an unsecured network between the client and the server on Kali Linux with Burpsuite.
    - Provide an explanation about the changes made to the Java and Python files.

### Edward Lim Padmajaya (Github Username: EdwardLimPadmajaya)
- Phase 1: 
    - Wrote a brief introduction to CCA and basic terminologies.
    - Wrote a brief overview of the Hash-then-Encrypt technique along with its pros and cons.
    - Provide a report on the HMAC's security features, efficiency, security draw-backs and underlying technical details.
    - Provide a comparison report on HMAC-SHA256 compared to other types of HMAC.

### Nicholas Sito (Github Username: nicholassitoRMIT)
- Phase 1:
    - Wrote a summary on the Encrypt-then-MAC method as well as its pros and cons.
    - Wrote a short justification on why we chose this method to be implemented in our project.
- Phase 3:
    - Responsible for editing the video for the assignment.
