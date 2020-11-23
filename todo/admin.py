from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'done',)
    list_display_links = ('id', 'title',)
    list_editable = ('done',)
    list_filter = ('done',)
    search_fields = ('id', 'title', 'description',)


admin.site.register(Todo, TodoAdmin)
