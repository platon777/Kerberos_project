from cryptography.fernet import Fernet
from datetime import datetime, timedelta


class Client:
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password
        # Autres attributs

    def request_tgt(self, as_server):
        # Demande un TGT à l'AS
        pass

    def request_service(self, tgs, service_id):
        # Demande un ticket de service au TGS
        pass

    def access_service(self, ss, service_ticket):
        # Tente d'accéder à un service avec le ticket
        pass
