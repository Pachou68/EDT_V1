from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

from app.models.base import Base
from app.models.user import User
from app.models.referentiels import Niveau, Professeur, Matiere, ProfesseurMatiere, Classe, Salle, ExigenceHebdo
from app.models.planning import SlotModele, ProfIndisponibilite, CoursPlanifie, CoursPlanifieClasse

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata, compare_type=True)
        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()

5.3 Commandes init
alembic init alembic
alembic revision --autogenerate -m "init schema"
alembic upgrade head

