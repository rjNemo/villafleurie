# Villafleurie : moteur de réservation autonome

`V 0.1 Le site est structuré. Il reste à appliquer le contenu et les visuels`

Auteur : Ruidy Nemausat

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

## Architecture

### Front-end

- `Bootstrap 4`
- `Javascript`
- `JQuery`

### Back-end

- `Django 3.0`
- `PostgreSQL`
- `Docker`
- `NginX`
- Google Calendar API

### Hébergement

- Virtual Private Server

## Pages

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
7. Page services

## Données

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

- Gestion du calendrier
  ..\_ Tester la synchro avec Google calendar
  ..\_ Ajouter un date picker dans le formulaire de réservation (j'ai pas envie de jouer avec JQuery)
- Envoyer devis réservation par mail et notification aux hôtes (put it in a background process, personnaliser les htmails)
- Ajout page/module de paiement
- ajouter les témoignages depuis Booking, AirBnb, ajouter le lien
- changer la couleur des liens hypertextes
- changer l'adresse de l'admin, personnaliser le back-end (design et les infos displayed per model)
- ajouter un diaporama en bas de page de location ?
- deploy on Heroku or somewhere else … don't care
- change placeholders for dates, add a date picker
- factoriser le code de réservation
- formulaire de réservation : les apparts sont hard codés rendre ça dynamique (use choicefields)
  \_ nettoyer les statics files. Garder que les définitions utiles
- Mixpanel et Google Analytics
- Récrire les mentions légales
- configure nginx server to serve media files
- Centrer Bouton "Reserver" page location
- Ajouter un titre "Disponibilités" au dessus du calendrier
- page réservation/services : égayer avec des petites photos …
- Internationalisation

## BUGS

- La synchro ne gère pas les heures dans le calendriers.
