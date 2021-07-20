# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 11:16:45 2021

@author: alessia
"""


'''
GATEWAY
'''


import socket as sk
import time
import sys

#Utilizzo questa funzione per stabilire una connessione UDP
# con i Client (Devices)
def UDPconnessioneClient(server_address, msg, buffer_size):
    
    #Creo il socket
    sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

    # associamo il socket alla porta
    print ('\n\r Inizio  %s sulla porta %s' % server_address)
    sock.bind(server_address)

    for i in range(NUMDEVICE):
        #Attendo di ricevere il messaggio
        print('\n\r In attesa di ricevere il messaggio...')
        data, indirizzo = sock.recvfrom(buffer_size)
        #Ricevo i dati
        print('Ricevuti %s bytes da %s' % (len(data), indirizzo))
        msg = msg + data.decode('utf-8') + "\n"
        #Stampo il messaggio con i sondaggi
        print (data.decode('utf-8'))
        #Aspetto 2 secondi poi rispondo
        time.sleep(2)
        
        sent = sock.sendto("Messaggio arrivato".encode(), indirizzo)
        print ('Inviati %s bytes al Device' % (sent))
    
    #Chiudo il socket
    print ('\nChiusura del socket\n')
    sock.close()
    return msg      


#Utilizzo questa funzione per connettere il Gateway al Cloud
#con una connessione TCP
def TCPconnessioneServer(server_address, msg, buffer_size):
    #Creo il socket
    clientsocket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    
    #Provo a connettermi al Cloud
    try:
        clientsocket.connect(server_address)
        print("Connessione con il Cloud... ")
        print("... Invio i sondaggi al Cloud... ")
        #Attendo 2 secondi prima di inviare la richiesta
        time.sleep(2)
        time_in = time.time()
    #Se la connessione fallisce invio un messaggio di errore
    except Exception as data:
        print (Exception,":",data)
        print ("Connessione fallita. Ritenta\r\n")
        sys.exit(0)
        
    #Invio i dati al Cloud
    clientsocket.send(msg.encode())
    #Stampo il messaggio
    print(msg.encode())   
    print("In attesa di risposta dal Cloud...")
    response = clientsocket.recv(buffer_size)
    #Prendo il tempo corrente
    time_fine = time.time()
    #Calcolo il tempo necessario ad inviare il messaggio al Cloud
    time_tot = time_fine - time_in
    
    print("Messaggio ricevuto: {}" .format(response.decode("utf8")))
    print ("La dimensione del buffer è: ",buffer_size)
    print ("Il tempo impiegato per trasmettere il messaggio TCP è: ",time_tot)
    
    #Chiudo la connessione
    print("\nChiusura connessione\n")    
    clientsocket.close()
    
    

NUMDEVICE = 4
#Indirizzo server Gateway
gateway_address = ('localhost', 10005)
#Dimensione del buffer
buffer_size = 4096
messaggio = ""
#Utilizzo la funzione UDPconnessioneClient per ricevere i messaggi dai Device
messaggio = UDPconnessioneClient(gateway_address, messaggio, buffer_size)
cloud_address = ('localhost', 8001)
#Trasferisco i messaggi dal Gateway al Cloud
TCPconnessioneServer(cloud_address, messaggio, buffer_size)
    


