from django.contrib import admin

from .models import *


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    fields = ('subscriber', 'subscribed_to')
    list_display = ('id', 'subscriber', 'subscribed_to')
    list_display_links = ('subscriber', )
    search_fields = ('subscriber', 'subscribed_to')
