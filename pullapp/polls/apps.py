from django.apps import AppConfig

class PollsConfig(AppConfig):
  defoult_auto_field = 'django.db.models.BigAutoField'
  name = 'polls'