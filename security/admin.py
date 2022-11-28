from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from .models import *
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form  = CustomUserChangeForm
	model = CustomUser 
	list_display = ['username', 'phone_number', 'birth_date']
	fieldsets = UserAdmin.fieldsets + (
		(None, {'fields': ('phone_number', 'birth_date')}),
	)


	
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Contract)
admin.site.register(Location)
admin.site.register(Shift)
admin.site.register(Post)
admin.site.register(Instruction)
admin.site.register(Guard)
admin.site.register(DDO)
admin.site.register(Firearm)
admin.site.register(AgencyInformation)
admin.site.register(Designation)
admin.site.register(FirearmAssignment)