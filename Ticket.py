from cryptography.fernet import Fernet
from datetime import datetime, timedelta

class Ticket:
    def __init__(self, user_id, service_id=None, issuer=None, validity_duration_hours=1):
        self.user_id = user_id
        self.service_id = service_id
        self.issuer = issuer  # 'AS' pour TGT, 'TGS' pour les tickets de service
        self.issued_at = datetime.now()
        self.valid_until = self.issued_at + timedelta(hours=validity_duration_hours)

    def serialize(self):
        # Convertir les données du ticket en une chaîne pour le cryptage
        ticket_data = {
            "user_id": self.user_id,
            "service_id": self.service_id,
            "issuer": self.issuer,
            "issued_at": self.issued_at.strftime("%Y-%m-%d %H:%M:%S"),
            "valid_until": self.valid_until.strftime("%Y-%m-%d %H:%M:%S")
        }
        return str(ticket_data)

    @staticmethod
    def deserialize(encrypted_ticket, fernet_key):
        # Décrypter et convertir la chaîne cryptée en un objet Ticket
        fernet = Fernet(fernet_key)
        decrypted_data = fernet.decrypt(encrypted_ticket).decode()
        ticket_data = eval(decrypted_data)

        ticket = Ticket(ticket_data["user_id"],
                        ticket_data.get("service_id"),
                        ticket_data["issuer"])
        ticket.issued_at = datetime.strptime(ticket_data["issued_at"], "%Y-%m-%d %H:%M:%S")
        ticket.valid_until = datetime.strptime(ticket_data["valid_until"], "%Y-%m-%d %H:%M:%S")
        return ticket

    def encrypt(self, fernet_key):
        # Crypter les données du ticket
        fernet = Fernet(fernet_key)
        return fernet.encrypt(self.serialize().encode())
