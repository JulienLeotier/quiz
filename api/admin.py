from django.contrib import admin

from api.models import Player, Question, Score

admin.site.register(Player)
admin.site.register(Score)
admin.site.register(Question)