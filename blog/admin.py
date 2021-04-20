from django.contrib import admin
from .models import *
from .forms import *


@admin.register(Marker)
class MarkerAdmin(admin.ModelAdmin):
    form = MarkerForm  #this field main_section required 

#main section and markers together
class MarkerInline(admin.TabularInline):
# Built-in editor is similar setform
# On the page editing a record primary model
# creating a setform for working with related records of the secondary model.
    model = Marker
    extra = 1 #number forms for create new record
    can_delete = True
    classes = "collapse" #display as spoiler


@admin.register(MainSection)
#decorator registers model in admin site
class MainSectionAdmin(admin.ModelAdmin):
    exclude = ('main_section',)
    inlines = (MarkerInline,)


#attacments and post together
class AttachmentAdmin(admin.TabularInline):
    model = Attachment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content','author','published')
    fields =  (('markers','author'),'title','content','image')
    inlines = (AttachmentAdmin,)


