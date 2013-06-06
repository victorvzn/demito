from myapp.models import Amigo
from django.contrib import admin

class AmigoAdmin(admin.ModelAdmin):
    list_display = ('nombres','user',)
    fields = ['nombres']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def queryset(self, request):
        qs = super(AmigoAdmin, self).queryset(request)

        # If super-user, show all comments
        if request.user.is_superuser:
            return qs

        return qs.filter(user=request.user)

admin.site.register(Amigo, AmigoAdmin)