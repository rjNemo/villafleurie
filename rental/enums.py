from django.db import models
from django.utils.translation import gettext_lazy as _


class PlaceNames(models.TextChoices):
    """ PlaceNames enums serve to list places and prepare
        for internationalisation
    """
    T2 = "T2", _("T2")
    T3 = "T3", _("T3")
