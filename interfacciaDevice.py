# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:05:36 2021

@author: alessia
"""

'''
INTERFACCIA DEVICE
'''

import socket as sk
import time



#Utilizzo questa funzione per connettere un qualsiasi device al server 
def UDPconnessioneServer(server_address, msg, buffer_size):
    #Creo il socket
    sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

    #Provo ad inviare il messaggio del device al gateway
    try:
        #Invio il messaggio
        print ('Invio del sondaggio al Gateway...')
        #attende 2 secondi prima di inviare la richiesta
        time.sleep(2) 
        time_in = time.time()
        sock.sendto(msg.encode(), server_address)

        #Ricevo la risposta dal Gateway
        print('In attesa di risposta...')
        data, server = sock.recvfrom(buffer_size)
        #Prendo il tempo attuale
        time_fine = time.time()
        #Calcolo il tempo totale
        time_tot = time_fine - time_in
        #Aspetto 2 secondi poi stampo 'Mesaggio ricevuto'
        time.sleep(2)
        print ('Messaggio ricevuto: "%s"' % data.decode('utf8'))
        print ("La dimensione del buffer è: ",buffer_size)
        print ("Il tempo impiegato per trasmettere il messaggio UDP è: ",time_tot)
        
    except Exception as info:
        print(info)
    finally:
        print ('Chiusura del socket')
        sock.close()

#Utilizzo questa funzione per estrapolare il messaggio dal file contenente i messaggi
def sondaggi (file_name, client_IP):
    
    #Cerco il file nella cartella Sondaggi e lo apro
    filePath = "Sondaggi/" + file_name
    file = open(filePath, "r")
    print("Lettura dati...")
    #Aspetto 2 secondi prima di leggere
    time.sleep(2)
    messaggio = ""
    
    while True:
        #Leggo le righe del file
        riga = file.readline()
        #Controllo se sono arrivata alla fine del file ed in tal caso esco
        if (riga == ""):
            break;
        #Se non sono arrivata alla fine del file formatto il messaggio
        else:
            messaggio =  messaggio + client_IP + " " + riga + "\n"
    
    #Chiudo il file
    file.close();
    print("Lettura sondaggi completata")
    
    return messaggio
