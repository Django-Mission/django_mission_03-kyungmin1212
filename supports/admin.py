from django.contrib import admin

from .models import Faq,Inquiry,Answer

class AnswerInline(admin.TabularInline):
    model = Answer

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('id','question','category','update_at')
    search_fields = ('question',)
    list_filter = ('category',)

@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('id','question','category','created_at','writer')
    search_fields = ('question',)
    list_filter = ('category',)
    inlines = [AnswerInline]

