from django.apps import AppConfig

class ArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'articles'
    verbose_name = 'Articles'

    def ready(self):
        from django.contrib import admin
        from django.contrib.auth.models import Group
        try:
            admin.site.unregister(Group)
        except Exception:
            pass
