from django.contrib import admin
from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'role', 'bio')
