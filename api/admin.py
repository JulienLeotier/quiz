from django.contrib import admin

from api.models import Last_question, Player, Question, Score

admin.site.register(Player)
admin.site.register(Score)
admin.site.register(Question)
admin.site.register(Last_question)