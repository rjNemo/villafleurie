# Villafleurie : moteur de réservation autonome

<!-- [![Travis](https://travis-ci.com/rjNemo/villafleurie.svg?branch=master)](https://travis-ci.com/rjNemo/villafleurie.svg?branch=master) -->

`V 1.0 Le site est prêt à l'emploi`

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

- `Django 3.0` python based web application
- `PostgreSQL` object-relational database
- `Celery` asynchronous task queue
- `RabbitMQ` messaging broker
- `NginX` reverse-proxy & static files server
- `Docker`
- Google Calendar API

### Hébergement

- VPS on [Vultr](https://my.vultr.com/subs/?SUBID=32140017)

## Pages

1. Page d'accueil

- Landing page
- CTA = "Réserver"

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

- [ ] Ajouter un date picker dans le formulaire de réservation
- [ ] Envoyer devis réservation par mail et notification aux hôtes (personnaliser les htmails : contact, admin et réservation)
- [ ] Ajout page/module de paiement
- [ ] Ajouter les témoignages depuis Booking, AirBnb, ajouter le lien. Créer une page dédiée.
- [ ] Changer l'adresse de l'admin, personnaliser le back-end (design et les infos displayed per model)
- [x] Factoriser le code de réservation
- [x] Formulaire de réservation : les apparts sont hard codés rendre ça dynamique (use choicefields)
- [x] Nettoyer les statics files. Garder que les définitions utiles
- [x] Mixpanel et Google Analytics
- [ ] Récrire les mentions légales
- [ ] Centrer Bouton "Reserver" page location
- [ ] Ajouter un titre "Disponibilités" au dessus du calendrier
- [ ] Page réservation/services : égayer avec des petites photos …
- [ ] Internationalisation
- [x] Push docker to Vultr. Connect to domain name
- [ ] Système de facturation: CRUD Réservations et envoi. Automatisation si possible
- [ ] Réservation page : Ajouter des photos. Renvoyer vers la page Location onClick sur Réserver TX. Proposer Upsells : navette + location voiture.
- [x] Vider le contenu du folder root ?
- [x] Pages confirmation message contact envoyé,
- [ ] reservations réussies ou non (expliquer pourquoi)
- [ ] SSL certificate
- [ ] Cookie bar
- [ ] Booking refs on landing page
- [ ] CD/CI build flow from master to Production
- [x] configure zapier webhooks
- [ ] Fuseau horaire
- [x] Calendar API
- [ ] Blog

## BUGS

- La synchro ne gère pas les heures dans le calendriers
