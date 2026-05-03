# Application de gestion d'emplois du temps scolaires

Application pour générer et consulter automatiquement les emplois du temps d'un collège (6e/5e/4e/3e/2e/1e/Te), avec authentification (administrateur,Lecture/écriture, Lecture), génération automatique sous contraintes, et exports CSV/PDF.

## Fonctionnalités

### 1. Authentification administrateur
- Connexion par identifiant + mot de passe 
- Toutes les pages de gestion sont protégées
- Bouton de déconnexion

### 2. Gestion des données de référence
Pages distinctes pour saisir :
- **Niveaux & Classes** : 6e, 5e, 4e, 3e, 2e, 1e, Te avec plusieurs classes par niveau (ex. 6°M1, 6°M2,T°STEG a, T°L2 a)
- **Matières** : nom + code couleur (chaque matière a sa couleur d'affichage)
- **Professeurs** : matricule, nom, prénom, matière(s) enseignée(s) — un prof peut enseigner une matière, une matière peut être enseignée par plusieurs profs
- **Salles** : numéro, capacité (nombre max de classes mutualisées)
- **Volumes horaires** : pour chaque couple (classe, matière), nombre de tranches de 55 min par semaine
- **Indisponibilités professeurs** : grille hebdomadaire cliquable pour marquer les créneaux indisponibles (par défaut tout disponible)

### 3. Structure temporelle 
- 5 jours : lundi → vendredi
- Tranches de 55 min entre 8h00 et 19h00
- Petite pause de 20 min à partir de 10h45
- Grande pause à partir de 12h55 : 55 min (lundi-jeudi), 1h35 (vendredi)
- Calcul des créneaux exacts effectué automatiquement

### 4. Génération automatique de l'emploi du temps
Bouton « Générer » qui lance un solveur respectant toutes les contraintes :
- Respect des volumes horaires par (classe, matière)
- Un prof n'est jamais dans deux salles en même temps
- Une classe n'a jamais deux cours en même temps
- Une salle n'accueille pas deux cours différents en même temps (sauf mutualisation)
- **Mutualisation** : plusieurs classes peuvent partager une salle uniquement si elles ont la même matière au même créneau, avec le même prof
- Indisponibilités professeurs respectées
- **Minimisation des trous** dans la journée pour chaque classe et chaque prof
- Affichage d'un rapport en cas d'impossibilité (contraintes non satisfiables) avec les conflits détectés

### 5. Visualisation des emplois du temps
Deux modes de consultation :
- **Par classe** : sélecteur de classe → grille hebdomadaire (jours en colonnes, créneaux en lignes), cellules colorées par matière, affichant matière + prof + salle
- **Par professeur** : sélecteur de prof → même grille, affichant matière + classe(s) + salle
- Pauses visibles comme bandes grises sur la grille
- Cours mutualisés clairement signalés (liste des classes regroupées)

### 6. Exports
Boutons d'export sur chaque vue d'emploi du temps :
- **CSV** : structure tabulaire (jour, heure, matière, prof, salle, classes)
- **PDF** : grille hebdomadaire mise en page proprement, en-tête avec nom de la classe ou du prof
- Export possible d'un seul EDT ou de tous d'un coup (zip non requis : un PDF multi-pages)

## Design

Style **moderne et coloré** :
- Interface SaaS épurée, navigation latérale
- Chaque matière a sa couleur identifiante, réutilisée dans toute l'app (listes, grilles, exports)
- Grilles d'emploi du temps lisibles avec coins arrondis, ombrages doux
- Mode clair par défaut, palette accessible (contraste suffisant pour le texte sur les couleurs de matière)
- Composants shadcn/ui pour cohérence (tables, dialogs, formulaires, sélecteurs
