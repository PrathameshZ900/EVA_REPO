from django.contrib import admin
from .models import Author, Books, Country

# Register User model
admin.site.register(Author)
admin.site.register(Books)
admin.site.register(Country)
