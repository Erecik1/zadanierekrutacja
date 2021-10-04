from django import forms

from book.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        widgets = {"title": forms.widgets.TextInput(attrs={"class": "form-control"}),
                   "author": forms.widgets.TextInput(attrs={"class": "form-control"}),
                   "date_of_publication": forms.widgets.DateInput(attrs={"class": "form-control", "type": "date"}),
                   "ISBN_number": forms.widgets.TextInput(attrs={"class": "form-control"}),
                   "number_of_pages": forms.widgets.TextInput(attrs={"class": "form-control"}),
                   "link_to_cover": forms.widgets.TextInput(attrs={"class": "form-control"}),
                   "language": forms.widgets.TextInput(attrs={"class": "form-control"}), }


class BookImportForm(forms.Form):
    form_widget = forms.widgets.TextInput(attrs={"class": "form-control"})
    intitle = forms.CharField(required=False, widget=form_widget)
    inauthor = forms.CharField(required=False, widget=form_widget)
    inpublisher = forms.CharField(required=False, widget=form_widget)
    subject = forms.CharField(required=False, widget=form_widget)
    isbn = forms.CharField(required=False, widget=form_widget)
    lccn = forms.CharField(required=False, widget=form_widget)
    oclc = forms.CharField(required=False, widget=form_widget)
