# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 11:10:38 2021

@author: alessia
"""

'''
DEVICE 2
'''


import interfacciaDevice as iD

#Setto l'IP del Device2
client_IP = "192.168.1.4"
#Prendo l'indiizzo del server (Gateway)
server_address = ("localhost", 10005)
#Imposto la dimensione del buffer
buffer_size = 4096
#Leggo dal file 'SondaggiDevice2' i sondaggi effettuati
file_name = "SondaggiDevice2.txt"
messaggio = iD.sondaggi(file_name, client_IP)
#Richiamo la funzione per la connessione con il Server
iD.UDPconnessioneServer(server_address, messaggio, buffer_size)

