package net.rozukke.elci;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.KeyFactory;
import java.security.PrivateKey;
import java.security.spec.PKCS8EncodedKeySpec;
import java.util.Arrays;
import java.util.Base64;
import javax.crypto.Cipher;

import org.bukkit.plugin.Plugin; 

public class RSADecryption {
    public static ELCIPlugin plugin;
    
    public static String messageDecryption(byte[] lineBytes) {
        // Get private key
        String privateKeyFilePath = "/Users/evelynlie/github-classroom/rmit-computing-technologies/cosc2804-apr-23-assignment-3-team-01-cosc2804-apr23/private_key.pem";
        //String privateKeyFilePath = "private_key.pem";

        String plaintext = null;
        try {
            // Read the private key from the PEM file
            byte[] keyContentsBytes = readKeyFile(privateKeyFilePath);
            PrivateKey privateKey = getPrivateKeyFromBytes(keyContentsBytes);
            
            // Create a copy of the args array and store it in a new byte array called encryptedData
            byte[] encryptedMessage = Arrays.copyOfRange(lineBytes, 0, lineBytes.length);

            // Decrypt the data using the privateKey
            String decryptedMessage = decrypt(privateKey, encryptedMessage);
            
            // Save decrypted data as a String in decrypted Message variable
            plaintext = new String(decryptedMessage);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return plaintext;
    }

    // Reads private key file as a sequence of bytes, converts it into a String, and returns the String
    private static byte[] readKeyFile(String filePath) throws IOException {
        //File privatekeyFile = new File(filePath);
        Path path = Paths.get(filePath);
        byte[] bytes = Files.readAllBytes(path);
        return bytes;
    }

    private static PrivateKey getPrivateKeyFromBytes(byte[] keyContentsBytes) throws Exception {
        // // Remove PEM file header and footer lines, and whitespace
        // String privateKeyBytes = new String(keyContentsBytes);
        // String privateKeyPEM = privateKeyBytes
        //         .replace("-----BEGIN PRIVATE KEY-----", "")
        //         .replace("-----END PRIVATE KEY-----", "")
        //         .replaceAll("\\s+", "") 
        //         .replaceAll("-", ""); // Remove hyphens

        // // // Add padding if base64 has incorrect length
        // // int paddingLength = 4 - (privateKeyPEM.length() % 4);
        // // if (paddingLength < 4) {
        // //     privateKeyPEM = privateKeyPEM + "=".repeat(paddingLength);
        // // }

        // // Decode base64 encoded key contents
        // byte[] KeyBytes = Base64.getDecoder().decode(privateKeyPEM);

        // Generate a private key object that is a copy of the private_key.pem
        PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(Base64.getDecoder().decode(keyContentsBytes));
        KeyFactory keyFactory = KeyFactory.getInstance("RSA");
        return keyFactory.generatePrivate(keySpec);
    }

    // Decrypt function using RSA
    private static String decrypt(PrivateKey privateKey, byte[] encryptedData){
        String decryptedBytes = "";
        try{
            Cipher cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding");
            cipher.init(Cipher.DECRYPT_MODE, privateKey);
            //Decrypting the text
            decryptedBytes = new String(cipher.doFinal(encryptedData));
        }
        catch (Exception e){
            plugin.getLogger().warning("Unable to decrpyt the message.");
        }
        return decryptedBytes;
    }
}
