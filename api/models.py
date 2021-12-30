from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext as _
from django.conf import settings


class Player(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(
        "player"), on_delete=models.CASCADE)
    photo = models.ImageField(_("photo"), upload_to="static/player/", height_field=None,
                              width_field=None, max_length=None, blank=True, null=True)

    class Meta:
        db_table = 'Player'
        managed = True
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        return self.user.username


class Score(models.Model):
    player = models.ForeignKey("Player", verbose_name=_(
        "players"), on_delete=models.CASCADE)
    score = models.IntegerField(_("score"), default=0)

    class Meta:
        db_table = 'score'
        managed = True
        verbose_name = 'Score'
        verbose_name_plural = 'Scores'

    def __str__(self):
        return self.player.user.username


class Question(models.Model):
    question = models.CharField(_("question"), max_length=250)
    activate = models.BooleanField(_("activate"), default=True)
    response = models.CharField(_("response"), max_length=250)
    image = models.ImageField(_("image"), upload_to="static/image/", height_field=None,
                              width_field=None, max_length=None, blank=True, null=True)
    audio = models.FileField(
        _("audio"), upload_to="static/audio/", max_length=100, blank=True, null=True)
    video = models.FileField(
        _("video"), upload_to="static/video/", max_length=100, blank=True, null=True)
    propositionOne = models.CharField(
        _("propositionOne"), max_length=250, blank=True, null=True)
    propositionTwo = models.CharField(
        _("propositionTwo"), max_length=250, blank=True, null=True)
    propositionThree = models.CharField(
        _("propositionThree"), max_length=250, blank=True, null=True)
    propositionFour = models.CharField(
        _("propositionFour"), max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'Question'
        managed = True
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question


class Last_question(models.Model):
    question = models.ForeignKey("Question", verbose_name=_(
        "question"), on_delete=models.CASCADE, blank=True, null=True)
    room = models.CharField(_("room"), max_length=50)

    class Meta:
        db_table = 'last_question'
        managed = True
        verbose_name = 'last_question'
        verbose_name_plural = 'last_questions'

    def __str__(self) -> str:
        return self.room
