# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 15:08:59 2021

@author: alessia
"""

'''
CLOUD
'''

import socket as sk

#Utilizzo questa funzione per stabilire una connessione TCP
#con il Client (Gateway)
def TCPconnessioneClient(server_address, buffer_size):
    
    #Creo il socket e lo associo con il server_address
    serverSocket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    serverSocket.bind(server_address)

    #Definisce la lunghezza della coda di backlog
    serverSocket.listen(1)
    #Avviso che il socket è pronto
    print ('Il Cloud è pronto...')
    connessioneGateway, indirizzo = serverSocket.accept()
    print('Connessione con il Gateway avvenuta con succeso!')

    #Provo a ricevere il messaggio
    try:

        print("Caricamento sondaggi...")
        messaggio = connessioneGateway.recv(buffer_size)
        #Stampo il messaggio 
        print(messaggio.decode('utf8'))
        print("Messaggio ricevuto")
        #Avviso il Gateway che ho ricevuto il messaggio
        connessioneGateway.send("Messaggio ricevuto".encode())
        #Chiudo la connessione
        print("\nChiusura connessione\n")
        connessioneGateway.close()
                    
    #Se non riesco a ricevere il massaggio lancio un eccezione
    except IOError:
        #Invia messaggio di risposta per file non trovato
        connessioneGateway.send(bytes("Errore","UTF-8"))
        #•Chiudo la connessione
        print("\nChiusura connessione\n")
        connessioneGateway.close()


server_address = ('localhost',8001)
print ('Il server è sulla porta: ',8001)
#IP server
server_IP = '10.10.10.4'
#Dimensione del buffer
buffer_size = 4096
TCPconnessioneClient(server_address,buffer_size)