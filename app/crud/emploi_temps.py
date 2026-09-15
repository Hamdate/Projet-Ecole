from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.emploi_temps import EmploiTemps
from app.schemas.emploi_temps import EmploiTempsCreate, EmploiTempsUpdate


def get_emplois(db: Session, id_classe: int = None, id_enseignant: int = None, id_annee: int = None):
    query = db.query(EmploiTemps)
    if id_classe:
        query = query.filter(EmploiTemps.id_classe == id_classe)
    if id_enseignant:
        query = query.filter(EmploiTemps.id_enseignant == id_enseignant)
    if id_annee:
        query = query.filter(EmploiTemps.id_annee == id_annee)
    return query.all()


def get_emploi(db: Session, id_emploi: int):
    return db.query(EmploiTemps).filter(EmploiTemps.id_emploi == id_emploi).first()


def _check_chevauchement(db: Session, data, exclude_id: int = None):
    query = db.query(EmploiTemps).filter(
        EmploiTemps.jour_semaine == data.jour_semaine,
        EmploiTemps.id_annee == data.id_annee,
        (EmploiTemps.id_enseignant == data.id_enseignant) | (EmploiTemps.id_classe == data.id_classe)
    )
    if exclude_id:
        query = query.filter(EmploiTemps.id_emploi != exclude_id)

    for cours in query.all():
        chevauche = data.heure_debut < cours.heure_fin and data.heure_fin > cours.heure_debut
        if chevauche:
            if cours.id_enseignant == data.id_enseignant:
                raise HTTPException(status_code=400, detail="Cet enseignant a déjà un cours sur ce créneau")
            if cours.id_classe == data.id_classe:
                raise HTTPException(status_code=400, detail="Cette classe a déjà un cours sur ce créneau")


def create_emploi(db: Session, data: EmploiTempsCreate):
    _check_chevauchement(db, data)
    db_obj = EmploiTemps(**data.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_emploi(db: Session, id_emploi: int, data: EmploiTempsUpdate):
    db_obj = get_emploi(db, id_emploi)
    if not db_obj:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_emploi(db: Session, id_emploi: int):
    db_obj = get_emploi(db, id_emploi)
    if not db_obj:
        return None
    db.delete(db_obj)
    db.commit()
    return db_obj