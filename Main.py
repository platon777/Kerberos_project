from authentication_server import AuthenticationServer
from ticket_granting_server import TicketGrantingServer
from service_server import ServiceServer
from client import Client
from ticket import Ticket

from flask import Flask, request, jsonify


def main():
    # Création des instances des composants Kerberos
    # auth_server = AuthenticationServer()
    # tgs = TicketGrantingServer()
    #service_server = ServiceServer()
    #client = Client()

    print("Hello world!!!")

    # Logique pour simuler le processus d'authentification Kerberos
    # ...

if __name__ == "__main__":
    main()
