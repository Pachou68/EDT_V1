# EDT_V1
application en français pour la gestion des emplois du temps d’une seule école.
Avec comme hypothèse :
Une couleur par matiére
Un professeur a un matricule, nom prénom et enseigne une matière.
Un professeur dispense un cours dans une salle.
Une salle peut regrouper plusieurs classes.
Les cours sont dispensés sur une amplitude de 11h entre 8h et 19h par tranche de 0h55
Un cours est dispensé du lundi au vendredi dans une salle par un professeur à un horaire donné.
Il y a une petite pause de 20 minutes à partir de 10h45 et une grande pause de 0h55 à partir de 12h55
Le vendredi la grande pause a une durée de 1h35
Un professeur ne peut être dans deux salles en même temps, le même jour.
Pour chaque matière et pour chaque classe il y a un nombre de tranches de 0h55 à effectuer par semaine.
Un enseignant est supposé disponible par défaut et fournit ses heures d’indisponibilités
Eviter les trous, dans la journée 
Une matière est- enseignée par plusieurs profs 
Les classes ne sont pas séparées en groupes
Les salles n’ont pas de spécificité pour certaines matières 
Cours mutualisés (salle regroupant plusieurs classes) autorisés pour toutes
C’est bien un niveau pédagogique type 6e/5e/4e/3e/2° /1°/T°
Mutualisation seulement si les classes ont la même matière 
Un profil administrateur, un profil utilisateur pour entrer les informations des professeurs et consulter , un profil utilisateur pour consultation uniquement
Génération automatique des emplois du temps avec possibilité de modification des placements d’un professeur 
Sorties au format csv ou pdf
Afficher un emploi du temps par classe ou par professeur
