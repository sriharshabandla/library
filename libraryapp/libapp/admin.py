from django.contrib import admin
from django import forms
from .models import Book, Author, Member, Record

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'price', 'available', 'isbn','stock','available1')
    list_filter = ('available',)
    search_fields = ['book_name', 'price', 'isbn', ]
    ordering = ('isbn', 'price', 'book_name', 'available',)

# admin.site.register(Book, BookAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('member_id', 'member_name', 'member_address',)
    list_filter = ('member_id',)
    search_fields = ['member_id', 'member_name', ]
    ordering = ('member_name', 'member_id', 'member_address',)

admin.site.register(Member, MemberAdmin)

class RecordAdmin(admin.ModelAdmin):
    list_display = ('book_issue_date', 'book_return_date',)
    list_filter = ('book_issue_date',)
    search_fields = ['book_name', 'author_name', ]
    ordering = ('book_name', 'book_issue_date', 'book_return_date',)

admin.site.register(Record, RecordAdmin)

class AuthorAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(AuthorAdminForm,self).__init__(*args,**kwargs)

    def clean(self):
        author_name = self.cleaned_data.get('author_name')
        if len(author_name) < 4:
            raise forms.ValidationError('enter a valid,cannot be less than 4 characters',code='invalid',)
        return self.cleaned_data

    def save(self,commit=True):
        return super(AuthorAdminForm,self).save(commit=commit)

class AuthorAdmin(admin.ModelAdmin):
    form = AuthorAdminForm

admin.site.register(Author,AuthorAdmin)

class BookAdminForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(BookAdminForm,self).__init__(*args,**kwargs)

    def clean(self):
        book_name=self.cleaned_data.get('book_name')
        if len(book_name) < 3:
            raise forms.ValidationError('enter a valid,cannot be less than 2 characters',code='invalid')

        return self.cleaned_data


    def save(self,commit=True):
        return super(BookAdminForm,self).save(commit=commit)

    # def __init__(self,*args,**kwargs):
    #     super(BookAdminForm,self).__init__(*args,**kwargs)
    # def clean(self):
    #     price =self.cleaned_data.get('price')
    #
    #     if len(price)< 4:
    #         raise forms.ValidationError('enter a valid,cannot be less than 2 characters',code='invalid')
    #     return self.cleaned_data

    # def save(self,commit=True):
    #     return super(BookAdminForm,self).save(commit=commit)


class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm

admin.site.register(Book,BookAdmin)





