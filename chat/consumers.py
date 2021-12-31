# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User

from api.models import Categorie, Last_question, Player, Question, Score


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = self.room_name
        last_question, create = Last_question.objects.get_or_create(
            room=self.room_name)
        print(last_question)
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        if last_question.question:
            last_question = Question.objects.filter(
                id=last_question.question.id).values().order_by('?').first()
        self.send(text_data=json.dumps({
            'message': last_question
        }))

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        if message['type'] == 'response':
            print(message['question'])
            question = Question.objects.get(question=message['question'])
            print(question.response)
            print(message['message'])
            if question.response.upper() == message['message']:
                score, created = Score.objects.get_or_create(player=Player.objects.get(
                    user=User.objects.get(username=message['player'])))
                print(score.score)
                score.score = score.score + 1
                print(score.score)
                score.save()
                self.send(text_data=json.dumps({
                    'type': 'score',
                    'player': message['player'],
                    'message': score.score
                }))

        if message['message'] == 'suivant':
            questions = Question.objects.filter(
                activate=True).values().order_by('?').first()
            last_question = Last_question.objects.get(room=self.room_name)
            last_question.question = Question.objects.get(id=questions['id'])
            last_question.save()
            if questions is not None:
                # update = Question.objects.get(id=questions['id'])
                # update.activate = False
                # update.save()
                message = questions
            else:
                message = "Désolé mais nous n'avons pas trouvé de questions"
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )
        if message['message'] == 'start':
            cat = Categorie.objects.get(name=message['categorie'])
            if cat.activate == True:
                cat.activate = False
                cat.save()
                self.send(text_data=json.dumps({
                    'type': 'categories',
                    'message': "ok"
                }))
            questions = Question.objects.filter(
                activate=True, categorie=Categorie.objects.get(name=message['categorie'])).values().order_by('?').first()
            last_question = Last_question.objects.get(room=self.room_name)
            last_question.question = Question.objects.get(id=questions['id'])
            last_question.save()
            if message['response'] == 'ok':
                score, created = Score.objects.get_or_create(player=Player.objects.get(
                user=User.objects.get(username=message['player'])))
                print(score.score)
                score.score = score.score + 1
                print(score.score)
                score.save()
                self.send(text_data=json.dumps({
                    'type': 'score',
                    'player': message['player'],
                    'message': score.score
                }))
            if questions is not None:
                # update = Question.objects.get(id=questions['id'])
                # update.activate = False
                # update.save()
                message = questions
            else:
                message = "Désolé mais nous n'avons pas trouvé de questions"
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )
        # Send message to room group

    # Receive message from room group

    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
