from cryptography.fernet import Fernet
from datetime import datetime, timedelta

class TicketGrantingServer:
    def __init__(self, auth_server_key):
        # Utilise la même clé que l'Authentication Server pour le TGT
        self.fernet = Fernet(auth_server_key)

    def issue_service_ticket(self, tgt_encrypted, service_id):
        # Décrypter le TGT
        try:
            tgt_data = self.fernet.decrypt(tgt_encrypted).decode()
            tgt_data = eval(tgt_data)

            # Vérifier la validité du TGT
            if self._is_tgt_valid(tgt_data):
                # Si le TGT est valide, générer un ticket de service
                return self._generate_service_ticket(tgt_data['user_id'], service_id)
            else:
                return None
        except:
            return None

    def _is_tgt_valid(self, tgt_data):
        # Vérifie si le TGT est encore valide
        valid_until = datetime.strptime(tgt_data['valid_until'], "%Y-%m-%d %H:%M:%S")
        return datetime.now() < valid_until

    def _generate_service_ticket(self, user_id, service_id):
        # Générer un ticket de service
        timestamp = datetime.now()
        validity = timedelta(hours=1)  # Durée de validité de 1 heure
        service_ticket_data = {
            "user_id": user_id,
            "service_id": service_id,
            "issued_at": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "valid_until": (timestamp + validity).strftime("%Y-%m-%d %H:%M:%S")
        }
        # Crypter le ticket de service
        service_ticket_encrypted = self.fernet.encrypt(str(service_ticket_data).encode())
        return service_ticket_encrypted

    # Autres méthodes nécessaires
