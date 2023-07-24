from django.contrib import admin
from blog.models import Post , Category , Comments , Contacts
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["title",'publishing_date',"slug"]
    list_display_links = ["publishing_date"]
    list_filter = ["publishing_date"]
    search_fields =["title","content"]
    list_editable = ["title"]

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        "pk",
        "title",
        "slug",
    )
class CommentAdmin(admin.ModelAdmin):
    class Meta:
        model = Comments

class ContactAdmin(admin.ModelAdmin):
    class Meta:
        model = Contacts
admin.site.register(Post, PostAdmin)
admin.site.register(Category , CategoryAdmin)
admin.site.register(Comments,CommentAdmin)
admin.site.register(Contacts , ContactAdmin)