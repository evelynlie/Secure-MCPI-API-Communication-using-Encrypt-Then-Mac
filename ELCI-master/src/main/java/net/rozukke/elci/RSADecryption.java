package net.rozukke.elci;

import java.io.FileReader;
import java.security.KeyPair;
import java.security.PrivateKey;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.KeyFactory;
import java.security.spec.PKCS8EncodedKeySpec;
import java.util.Arrays;
import java.util.Base64;
import javax.crypto.Cipher;

public class RSADecryption {
    public static ELCIPlugin plugin;
    
    public static String messageDecryption(PrivateKey privKey, byte[] lineBytes) {
        String plaintext = null;
        try {
            PrivateKey privateKey = privKey;

            System.out.println("Private Key: " + privateKey.toString());

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
    private static PrivateKey readKeyFile(String filePath) throws IOException {
        String pemFilePath = filePath;

        try (BufferedReader reader = new BufferedReader(new FileReader(pemFilePath))) {
            StringBuilder sb = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                if (!line.startsWith("-----")) {
                    sb.append(line.trim());
                }
            }
            
            // byte[] keyBytes = Base64.getDecoder().decode(sb.toString());

            System.out.println(sb.toString());
            KeyFactory keyFactory = KeyFactory.getInstance("RSA");

            byte[] derData = Base64.getDecoder().decode(sb.toString().getBytes());

            PKCS8EncodedKeySpec keySpec = new PKCS8EncodedKeySpec(derData);
            System.out.println(keySpec.toString());

            return keyFactory.generatePrivate(keySpec);

        } catch (Exception e) {
            throw new IOException("Failed to read private key from file: " + filePath, e);
        }
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
