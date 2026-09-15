import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.documents import CarteScolaire
from app.schemas.documents import CarteScolaireCreate


def get_cartes(db: Session, id_inscription: int = None):
    query = db.query(CarteScolaire)
    if id_inscription:
        query = query.filter(CarteScolaire.id_inscription == id_inscription)
    return query.all()


def get_carte(db: Session, id_carte: int):
    return db.query(CarteScolaire).filter(CarteScolaire.id_carte == id_carte).first()


def create_carte(db: Session, data: CarteScolaireCreate):
    numero_carte = f"CARTE-{uuid.uuid4().hex[:8].upper()}"
    qr_token = uuid.uuid4().hex

    db_obj = CarteScolaire(
        **data.model_dump(),
        numero_carte=numero_carte,
        qr_token=qr_token
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def reimprimer_carte(db: Session, id_carte: int):
    db_obj = get_carte(db, id_carte)
    if not db_obj:
        return None
    db_obj.nombre_reeditions = (db_obj.nombre_reeditions or 0) + 1
    db_obj.derniere_impression = datetime.utcnow()
    db.commit()
    db.refresh(db_obj)
    return db_obj