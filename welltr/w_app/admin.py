from django.contrib import admin

from w_app.models import User, Data


class DataAdmin(admin.TabularInline):
    model = Data

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [DataAdmin]

