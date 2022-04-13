from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

PERSONAL_INFO_FIELDS = (
    'Account Info', {
        'fields': (
            'first_name',
            'last_name',
            'contact_no',
            'birthday',
            'sex',
            'pronouns',
            # 'seed_phrase',
        )
    }
)

PROVIDER_INFO_FIELDS = (
    'Provider Info', {
	'fields': (
	   'provider_type',
	   'prc_num',
	   'prc_pic'
       )
    }
)

PERMISSIONS_FIELDS = (
    'Permissions', {
        'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )
    }
)

class AccountAdmin(UserAdmin):
    model = Account
    list_filter = (
	'is_active',
    )
    list_display = ('full_name', 'email', 'username', )
    search_fields = ('full_name', 'email', 'username', )
    readonly_fields = ('id', 'seed_phrase', )
    
    fieldsets = (
        (None, {
            'fields': (
		'id',
                'email',
                'password'
            )
        }),
        PERSONAL_INFO_FIELDS,
        PROVIDER_INFO_FIELDS,
        PERMISSIONS_FIELDS,
        ('Important dates', {
            'fields': (
                'last_login',
                'date_joined'
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': (
                'email',
                'password1',
                'password2',
            )
        }),
        PERSONAL_INFO_FIELDS,
        PROVIDER_INFO_FIELDS,
        PERMISSIONS_FIELDS,
    )

admin.site.register(Account, AccountAdmin)
