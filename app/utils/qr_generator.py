import uuid


def generer_token() -> str:
    """
    Génère un token unique aléatoire, utilisé notamment pour l'authenticité
    des cartes scolaires (champ qr_token).
    """
    return uuid.uuid4().hex


def generer_reference(prefixe: str, identifiant: int, longueur: int = 6) -> str:
    """
    Génère une référence lisible du type PREFIXE-000123 (paiements, reçus...).
    """
    return f"{prefixe}-{identifiant:0{longueur}d}"


def generer_image_qr(contenu: str, chemin_sortie: str) -> str:
    """
    Génère une image QR code (PNG) à partir d'un texte (ex: qr_token d'une
    carte scolaire) et l'enregistre sur disque.
    Nécessite : pip install qrcode[pil] --break-system-packages
    """
    import qrcode
    img = qrcode.make(contenu)
    img.save(chemin_sortie)
    return chemin_sortie