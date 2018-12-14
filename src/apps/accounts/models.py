from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group as DjangoGroup, \
    AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class Group(DjangoGroup):
    """..."""
    class Meta:
        proxy = True
        app_label = 'accounts'
        verbose_name = _('group')
        verbose_name_plural = _('Groups')


class User(AbstractBaseUser, PermissionsMixin):
    """..."""
    email = models.EmailField(
        blank=False,
        unique=True,
        verbose_name=_('E-mail')
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_('Staff status'),
        help_text=_('Designates whether the user can log into admin of site.')
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Active'),
        help_text=_(
            'Designates whether this user should be treated as '
            'active. Unselect this instead of deleting accounts.'
        )
    )
    is_confirmed = models.BooleanField(
        default=False,
        verbose_name=_('Confirmed'),
        help_text=_(
            'The user has confirmed the account. If this option is '
            'not selected - the account can be re-registered.'
        )
    )
    token = models.CharField(
        max_length=32,
        verbose_name=_('Confirm token'),
        blank=True,
        null=True
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('Date joined'),
        help_text=_('Date when the user was registered.')
    )
    photo = models.ImageField(
        verbose_name=_('Photo'),
        blank=True,
        null=True
    )
    first_name = models.CharField(
        verbose_name=_('First name'),
        max_length=64,
        blank=False,
        null=True
    )
    middle_name = models.CharField(
        verbose_name=_('Middle name'),
        max_length=64,
        blank=False,
        null=True
    )
    last_name = models.CharField(
        verbose_name=_('Last name'),
        max_length=64,
        blank=False,
        null=True
    )
    phone = models.CharField(
        verbose_name=_('Phone'),
        max_length=64,
        blank=False,
        null=True
    )
    skype = models.CharField(
        verbose_name=_('Skype'),
        max_length=64,
        blank=False,
        null=True
    )
    telegram = models.CharField(
        verbose_name=_('Telegram'),
        max_length=64,
        blank=False,
        null=True
    )
    position = models.CharField(
        verbose_name=_('Position'),
        max_length=64,
        blank=False,
        null=True
    )
    city = models.CharField(
        verbose_name=_('City'),
        max_length=64,
        blank=True,
        null=True
    )
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = tuple()
    
    def image_tag(self):
        if self.photo:
            return u'<img style="width: 100px" src="%s" />' % self.photo.url
        else:
            return '<b>%s</b>'%_('No')
    image_tag.short_description = _('Photo')
    image_tag.allow_tags = True

    def get_short_name(self):
        return self.email

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('Users')

    @property
    def full_name(self):
        return '{0} {1} {2}'.format(
            self.last_name if self.last_name else '',
            self.first_name if self.first_name else '',
            self.middle_name if self.middle_name else ''
        )

    def __str__(self):
        """"Show object as string."""
        return self.full_name if len(self.full_name)>2 else self.email
