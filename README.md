[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11232936&assignment_repo_type=AssignmentRepo)
# Minecraft Scure API
This is the README file for Assignment 3 in Programming Studio 2 (COSC2804).

Please indicate where to find your video demo. You can include it in this repo if it's small enough, or alternatively use a video sharing platform, such as YouTube. Any widely supported video format is fine (.mp4, .avi, .mkv, etc.)

# Mandatory: Student contributions
- Go Chee Kin: 25%
- Evelyn Lie: 30%
- Nicholas Sito: 20%
- Edward Lim Padmajaya: 25%

### Go Chee Kin, s3955624 (Github Username: rmit-kent-go)
- Phase 1:
    - Written summary on the MAC-then-encrypt technique's pros and cons
    - Written report on the RSA algorithm's security features, efficiency, security draw-backs and underlying technical details
- Phase 2:
    - Implement HMAC authentication generation in Python
    - Assist Evelyn in fixing minor bugs for RSA encryption in Python
    - Note that Go Chee Kin have request assistances from Mr. Alessio Bonti and Roman Artemis to solve Maven packaging issues (not generating required files to run ELCI) and no success has yet to achieve. Hence there's failure in running modified RemoteServer.java and elci.jar files in Minecraft server. So, my contributions/commits are created on Evelyn's laptop and submitted using Evelyn's Github Username due to failure in running modified changes in my own Minecraft server. Hope you understand.

### Evelyn Lie, s3951140 (Github Username: eve-s3951140)
- Phase 1: 
    - Wrote a brief overview of the Encrypt-and-MAC technique along with its pros and cons.
    - Provide a simple and straight-forward explanation about Asymmetric Encryption and Message Authentication Code (MAC), with references.
- Phase 2:
    - Create a RSA and HMAC key generation in Java to be sent into Python. 
        - The RSA key size is specified in 2048 bits and HMAC key size is 256 bits.
    - Complete Implementation of RSA encryption in Python and decryption in Java using several functions, assisted by Kent in dealing minor bugs.
    - Implement HMAC calculation in Java to be compared with the one generated in Python. If the HMAC value from Python and Java is different, the message will not be decrypted since the authenticity and integrity of the message has been corupted.