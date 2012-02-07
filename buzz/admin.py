from django.contrib import admin

from buzz.models import AuthorExpertise, Country, File, Mention, Product, \
    Report, ReportType, Source, MentionType, UserProfile, FollowUp, \
    FollowUpStatus


class BuzzAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'creation_user', None) is None:
            obj.creation_user = request.user
        obj.last_update_user = request.user
        obj.save()


class JustNameAdmin(BuzzAdmin):
    fields = ('name',)


class FileAdmin(BuzzAdmin):
    fields = ('name', 'location')


class MentionAdmin(BuzzAdmin):
    fields = ('type','origin', 'feedback', 'link', 'text', 'author_expertise',
              'previous_product_comments', 'estimated_audience', 'country',
              'product', 'relevant_audience', 'update_rate', 'remarks', 'source_name')


class FollowUpAdmin(BuzzAdmin):
    fields = ('status', 'mention', 'remarks')


admin.site.register(AuthorExpertise, JustNameAdmin)
admin.site.register(Country, JustNameAdmin)
#admin.site.register(File, FileAdmin)
admin.site.register(MentionType, JustNameAdmin)
admin.site.register(Mention, MentionAdmin)
admin.site.register(Product, JustNameAdmin)
#admin.site.register(Report, BuzzAdmin)
#admin.site.register(ReportType, BuzzAdmin)
admin.site.register(Source, JustNameAdmin)
#admin.site.register(UserProfile, BuzzAdmin)
admin.site.register(FollowUp, FollowUpAdmin)
admin.site.register(FollowUpStatus, JustNameAdmin)
