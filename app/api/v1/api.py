from fastapi import APIRouter
from app.api.v1.endpoints import (
    auth,
    etablissements, roles, utilisateurs,
    annees_scolaires, periodes, classes, matieres,
    eleves, parents, inscriptions,
    enseignants,
    evaluations, notes, presences_eleves, bulletins,
    emploi_temps,
    presences_enseignants, cours_effectues,
    honoraires,
    frais_scolaires, paiements, recus, depenses,
    cartes_scolaires,
    communication,
    parametres,
    dashboard,
    journal
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Authentification"])
api_router.include_router(etablissements.router, prefix="/etablissements", tags=["Établissements"])
api_router.include_router(roles.router, prefix="/roles", tags=["Rôles"])
api_router.include_router(utilisateurs.router, prefix="/utilisateurs", tags=["Utilisateurs"])
api_router.include_router(annees_scolaires.router, prefix="/annees-scolaires", tags=["Années scolaires"])
api_router.include_router(periodes.router, prefix="/periodes", tags=["Périodes"])
api_router.include_router(classes.router, prefix="/classes", tags=["Classes"])
api_router.include_router(matieres.router, prefix="/matieres", tags=["Matières"])
api_router.include_router(eleves.router, prefix="/eleves", tags=["Élèves"])
api_router.include_router(parents.router, prefix="/parents", tags=["Parents"])
api_router.include_router(inscriptions.router, prefix="/inscriptions", tags=["Inscriptions"])
api_router.include_router(enseignants.router, prefix="/enseignants", tags=["Enseignants"])
api_router.include_router(evaluations.router, prefix="/evaluations", tags=["Évaluations"])
api_router.include_router(notes.router, prefix="/notes", tags=["Notes"])
api_router.include_router(presences_eleves.router, prefix="/presences-eleves", tags=["Présences élèves"])
api_router.include_router(bulletins.router, prefix="/bulletins", tags=["Bulletins"])
api_router.include_router(emploi_temps.router, prefix="/emploi-temps", tags=["Emploi du temps"])
api_router.include_router(presences_enseignants.router, prefix="/presences-enseignants", tags=["Présences enseignants"])
api_router.include_router(cours_effectues.router, prefix="/cours-effectues", tags=["Cours effectués"])
api_router.include_router(honoraires.router, prefix="/honoraires", tags=["Honoraires"])
api_router.include_router(frais_scolaires.router, prefix="/frais-scolaires", tags=["Frais scolaires"])
api_router.include_router(paiements.router, prefix="/paiements", tags=["Paiements"])
api_router.include_router(recus.router, prefix="/recus", tags=["Reçus"])
api_router.include_router(depenses.router, prefix="/depenses", tags=["Dépenses"])
api_router.include_router(cartes_scolaires.router, prefix="/cartes-scolaires", tags=["Cartes scolaires"])
api_router.include_router(communication.router, prefix="/communication", tags=["Communication"])
api_router.include_router(parametres.router, prefix="/parametres", tags=["Paramètres"])
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
api_router.include_router(journal.router, prefix="/journal", tags=["Journal d'activité"])