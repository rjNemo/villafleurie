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

- [Bootstrap4](https://getbootstrap.com/) - The most popular HTML, CSS, and JS library in the world.
- [JQuery](https://jquery.com/)

### Back-end

- [Django](https://www.djangoproject.com/) - The Web framework for perfectionists with deadlines
- [PostgreSQL](https://www.postgresql.org/) - The world's most advanced open source database
- [Celery](http://www.celeryproject.org/) - Distributed Task Queue
- [RabbitMQ](https://www.rabbitmq.com/) - Messaging that just works
- [NginX](https://www.nginx.com/) - High Performance Load Balancer, Web Server & Reverse Proxy
- [Docker](https://www.docker.com/) - Empowering App Development for Developers

### Hébergement

- VPS on Vultr at [this address](http://villafleuriegp.com)

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

## BUGS

- La synchro ne gère pas les heures dans le calendriers
