[![Build Status](https://travis-ci.org/fhinkel/create-download-link.svg?branch=master)](https://travis-ci.org/fhinkel/create-download-link)

# Villafleurie : moteur de réservation autonome

`V 0.1 Le site est structuré. Il reste à appliquer le contenu et les visuels`

## Projet

Créer un site vitrine présentant l'activité de Villafleurie :

- location de logements : T2 et T3
- navette entre l'aéroport, la gare maritime et la résidence
- découverte de l'archipel

Le visiteur doit pouvoir :

- connaitre les disponibilité de chaque logement,
- leur tarif,
- pouvoir contacter les propriétaires,
- et pouvoir réserver

## Structure

### Pages

1. Page d'accueil

- Landing page
- CTA = "Réserver maintenant"

2. Page logement

- photos,
- disponibilités,
- tarif pour la période sélectionnée,

3. Page réservation

- Entrer ses coordonnées
- La réservation n'est validée que si la période spécifiée est libre
- Prépayer la réservation ou la caution,

4. Page remerciements

- Expliquer les prochaines étapes

5. Page contact
6. Page légale

### Données

1. Logement :

- nom,
- photos,
- description,
- calendrier,
- tarif

2. Client :

- nom,
- mail,
- téléphone,
- _réservation_

3. Réservation :

- _client_,
- _logement_,
- dates de calendrier,

4. Témoignages :

- _client_,
- _reservation_,
- témoignage

## TO DO

- Page service : navette + location
- Gestion du calendrier
  ..\_ Synchroniser avec Google calendar
  ..\_ Afficher les disponibilités
- Envoyer devis réservation par mail et notification aux hôtes
- Ajout page/module de paiement
- ajouter les témoignages depuis Booking, AirBnb, ajouter le lien
- changer la couleur des liens hypertextes
- changer l'adresse de l'admin
- ajouter un diaporama en bas de page de location ?
- deploy on Heroku or somewhere else … don't care
- change placeholders for dates, add a date picker
- factoriser le code de réservation
- formulaire de réservation : les apparts sont hard codés rendre ça dynamique

## BUGS
