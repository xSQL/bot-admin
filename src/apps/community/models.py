from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Extension(models.Model):
    """..."""
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name')
    )
    description = models.TextField(
        verbose_name=_('Description')
    )

    def __str__(self):
        """..."""
        return self.name


class Community(models.Model):
    """..."""
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name')
    )
    community_id = models.PositiveIntegerField(
        verbose_name=_('Community id')
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='communities'
    )
    extensions = models.ManyToManyField(Extension)
    def __str__(self):
        """..."""
        return self.name


class Synonym(models.Model):
    """..."""
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name')
    )
    text = models.TextField(
        verbose_name=_('Description')
    )
    community = models.ForeignKey(
        Community,
        on_delete=models.CASCADE,
        related_name='synonyms'
    )
    
    def __str__(self):
        """..."""
        return self.name


