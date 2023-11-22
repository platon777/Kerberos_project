from cryptography.fernet import Fernet
from datetime import datetime, timedelta
from supabase import create_client, Client

class AuthenticationServer:
    def __init__(self, supabase_url, supabase_key):
        self.supabase: Client = create_client(supabase_url, supabase_key)
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def authenticate(self, user_id, password):
        # Vérifier les identifiants de l'utilisateur dans Supabase
        user_data = self._get_user_data(user_id)
        if user_data and user_data['password'] == password:
            # Si les identifiants sont valides, générer et retourner un TGT
            return self._generate_tgt(user_id)
        else:
            return None

    def _get_user_data(self, user_id):
        # Interroger Supabase pour obtenir les données de l'utilisateur
        query = self.supabase.table("users").select("*").eq("user_id", user_id).execute()
        user_data = query.data
        return user_data[0] if user_data else None

    def _generate_tgt(self, user_id):
        # Créer un TGT avec des informations utilisateur et une durée de validité
        timestamp = datetime.now()
        validity = timedelta(hours=1)  # Durée de validité de 1 heure
        tgt_data = {
            "user_id": user_id,
            "issued_at": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "valid_until": (timestamp + validity).strftime("%Y-%m-%d %H:%M:%S")
        }
        # Crypter le TGT
        tgt_encrypted = self.fernet.encrypt(str(tgt_data).encode())
        return tgt_encrypted

    # Autres méthodes nécessaires
