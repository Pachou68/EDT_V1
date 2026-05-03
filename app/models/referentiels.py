app/models/referentiels.py
from sqlalchemy import String, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

class Niveau(Base):
    __tablename__ = "niveau"
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    libelle: Mapped[str | None] = mapped_column(String(50), nullable=True)

class Professeur(Base):
    __tablename__ = "professeur"
    id: Mapped[int] = mapped_column(primary_key=True)
    matricule: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    nom: Mapped[str] = mapped_column(String(100), nullable=False)
    prenom: Mapped[str] = mapped_column(String(100), nullable=False)

class Matiere(Base):
    __tablename__ = "matiere"
    id: Mapped[int] = mapped_column(primary_key=True)
    libelle: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

class ProfesseurMatiere(Base):
    __tablename__ = "professeur_matiere"
    professeur_id: Mapped[int] = mapped_column(ForeignKey("professeur.id", ondelete="CASCADE"), primary_key=True)
    matiere_id: Mapped[int] = mapped_column(ForeignKey("matiere.id", ondelete="CASCADE"), primary_key=True)

class Classe(Base):
    __tablename__ = "classe"
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    niveau_id: Mapped[int] = mapped_column(ForeignKey("niveau.id"), nullable=False)
    effectif: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

class Salle(Base):
    __tablename__ = "salle"
    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    capacite: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

class ExigenceHebdo(Base):
    __tablename__ = "exigence_hebdo"
    __table_args__ = (UniqueConstraint("classe_id", "matiere_id", name="uq_exigence_classe_matiere"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    classe_id: Mapped[int] = mapped_column(ForeignKey("classe.id", ondelete="CASCADE"), nullable=False)
    matiere_id: Mapped[int] = mapped_column(ForeignKey("matiere.id", ondelete="CASCADE"), nullable=False)
    nb_tranches_semaine: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

app/models/planning.py
from sqlalchemy import Integer, String, ForeignKey, Time, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class SlotModele(Base):
    __tablename__ = "slot_modele"
    jour: Mapped[int] = mapped_column(SmallInteger, primary_key=True)         # 1..5
    slot_index: Mapped[int] = mapped_column(SmallInteger, primary_key=True)   # 1..10 ou 1..9
    heure_debut: Mapped[str] = mapped_column(Time, nullable=False)
    heure_fin: Mapped[str] = mapped_column(Time, nullable=False)

class ProfIndisponibilite(Base):
    __tablename__ = "prof_indisponibilite"
    professeur_id: Mapped[int] = mapped_column(ForeignKey("professeur.id", ondelete="CASCADE"), primary_key=True)
    jour: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    slot_index: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    motif: Mapped[str | None] = mapped_column(String(200), nullable=True)

class CoursPlanifie(Base):
    __tablename__ = "cours_planifie"
    id: Mapped[int] = mapped_column(primary_key=True)
    matiere_id: Mapped[int] = mapped_column(ForeignKey("matiere.id"), nullable=False)
    professeur_id: Mapped[int] = mapped_column(ForeignKey("professeur.id"), nullable=False)
    salle_id: Mapped[int] = mapped_column(ForeignKey("salle.id"), nullable=False)
    niveau_id: Mapped[int] = mapped_column(ForeignKey("niveau.id"), nullable=False)
    jour: Mapped[int] = mapped_column(SmallInteger, nullable=False)       # 1..5
    slot_index: Mapped[int] = mapped_column(SmallInteger, nullable=False)

class CoursPlanifieClasse(Base):
    __tablename__ = "cours_planifie_classe"
    cours_id: Mapped[int] = mapped_column(ForeignKey("cours_planifie.id", ondelete="CASCADE"), primary_key=True)
    classe_id: Mapped[int] = mapped_column(ForeignKey("classe.id", ondelete="CASCADE"), primary_key=True)
