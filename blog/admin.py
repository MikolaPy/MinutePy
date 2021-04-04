from django.contrib import admin

from .models import Post,Teg,AdvUser

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content','published',)
    list_display_links = ('title','content',)
    search_fields = ('title','content',)
admin.site.register(Post,PostAdmin)       # admin.site = instance class AdmineSite
admin.site.register(Teg)
admin.site.register(AdvUser)

