from django.contrib import admin

from buzz.models import AuthorExpertise, Country, File, Mention, Product, \
    Report, ReportType, Source, MentionType, UserProfile

admin.site.register(AuthorExpertise, admin.ModelAdmin)
admin.site.register(Country, admin.ModelAdmin)
admin.site.register(File, admin.ModelAdmin)
admin.site.register(Mention, admin.ModelAdmin)
admin.site.register(Product, admin.ModelAdmin)
admin.site.register(Report, admin.ModelAdmin)
admin.site.register(ReportType, admin.ModelAdmin)
admin.site.register(Source, admin.ModelAdmin)
admin.site.register(MentionType, admin.ModelAdmin)
admin.site.register(UserProfile, admin.ModelAdmin)