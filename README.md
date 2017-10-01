# Filecrypter
### A generic command line application used to encrypt files.

Encryption/Decryption is done using a key which is bitwise XOR'ed with the text of the file in a round-robin.
Multiple passes ensure high cryptoghraphic strength, randomly generated keys add to the complexity of the encryption

#### Usage: 

    python filecrypter.py -i <input_file> -o <output_file> -k <key_for_encryption>
   -default action without -i : takes input in the terminal
   
   -default action without -o : displays output in terminal
   
   -default action without -k : generates random key, which has to be an input at the time of decryption
