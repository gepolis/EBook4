from django import forms
from django.contrib.auth.forms import UserCreationForm

from Accounts.models import Account

from MainApp.models import Events, ClassRoom, EventCategory

class EditUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, disabled=True)

    class Meta:
        model = Account
        fields = (
        "username", "email", "second_name", "first_name", "middle_name", "date_of_birth", "role","points")
        labels = {
            "username": "Имя пользователя",
            "email": "Почта",
            "second_name": "Фамилия",
            "first_name": "Имя",
            "middle_name": "Отчество",
            "date_of_birth": "Дата рождения",
            "role": "Роль",
            "points": "Баллов"
        }
        widgets = {
            'date_of_birth': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       })
        }
    def save(self, commit=True):
        user = super(EditUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Почта")

    class Meta:
        model = Account
        fields = (
        "username", "email", "second_name", "first_name", "middle_name", "password1", "password2", "date_of_birth", 'role')
        labels = {
            "username": "Имя пользователя",
            "email": "Почта",
            "second_name": "Фамилия",
            "first_name": "Имя",
            "middle_name": "Отчество",
            "date_of_birth": "Дата рождения",
            'role': "Роль"

        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={"type": "date"})
        }

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class EventAddForm(forms.ModelForm):
    class Meta:
        model = Events
        # Описываем поля, которые будем заполнять в форме
        fields = ('name','description','start_date','end_date','organizer', 'category', 'classroom_number','building', 'image')

        widgets = {
            'name': forms.TextInput(),
            'description': forms.Textarea(),
            'start_date': forms.DateTimeInput(format=['%d/%m/%y'], attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(format=['%d/%m/%y'], attrs={'type': 'datetime-local'}),
            'organizer': forms.Select(),
            'classroom_number': forms.Select(),
            'building': forms.Select(),
            'image': forms.FileInput(attrs={"class": "form-control"})
        }
        labels = {
            "name": "Название",
            "description": "Описание",
            "start_date": "Дата начала",
            "end_date": "Дата окончания",
            "organizer": "Организатор",
            "building": "Корпус",
            "classroom_number": "Доступно для",
            "image": "Изображение",
            "category": "Категория"

        }

    def save(self, commit=True):
        user = super(EventAddForm, self).save(commit=False)
        if commit:
            user.save()
        return user



class NewClassRoom(forms.ModelForm):
    class Meta:
        model = ClassRoom
        # Описываем поля, которые будем заполнять в форме
        fields = ('classroom','parallel')

        widgets = {
            'classroom': forms.NumberInput(),
            'parallel': forms.TextInput(attrs={"style": "text-transform:uppercase" }),
        }
        labels = {
            "classroom": "Класс",
            "parallel": "Паралель",
        }
    def unique(self):
        classroom = super(NewClassRoom, self).save(commit=False)
        if ClassRoom.objects.all().filter(classroom=classroom.classroom, parallel__iexact=str(classroom.parallel).upper()).exists():
            return False
        else:
            return True

    def save(self, commit=True):
        classroom = super(NewClassRoom, self).save(commit=False)
        classroom.parallel = str(classroom.parallel).upper()
        if commit:
            classroom.save()
        return classroom



class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = (
        "username", "second_name", "first_name", "middle_name", "date_of_birth")
        labels = {
            "username": "Имя пользователя",
            "second_name": "Фамилия",
            "first_name": "Имя",
            "middle_name": "Отчество",
            "date_of_birth": "Дата рождения"
        }
        widgets = {
            'date_of_birth': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        }
    def save(self, commit=True):
        user = super(EditProfileForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class EventCategoryForm(forms.ModelForm):
    class Meta:
        model = EventCategory
        # Описываем поля, которые будем заполнять в форме
        fields = ('name','methodists')
        labels = {
            "name": "Название",
            "methodists": "Методисты"
        }

    def save(self, commit=True):
        user = super(EventCategoryForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class EventAddFormMethodist(forms.ModelForm):
    class Meta:
        model = Events
        # Описываем поля, которые будем заполнять в форме
        fields = ('name','description','start_date','end_date', 'category', 'classroom_number','building', 'image', "organizer")

        widgets = {
            'name': forms.TextInput(),
            'description': forms.Textarea(),
            'start_date': forms.DateTimeInput(format=['%d/%m/%y'], attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(format=['%d/%m/%y'], attrs={'type': 'datetime-local'}),
            'building': forms.Select(),
            'image': forms.FileInput(attrs={"class": "form-control"})
        }
        labels = {
            "name": "Название",
            "description": "Описание",
            "start_date": "Дата начала",
            "end_date": "Дата окончания",
            "organizer": "Организатор",
            "building": "Корпус",
            "classroom_number": "Доступно для",
            "image": "Изображение",
            "category": "Категория"

        }

    def __init__(self,loggedin_user=None, *args, **kwargs):
        super(EventAddFormMethodist, self).__init__(*args, **kwargs)
        if loggedin_user is not None:
            self.fields['category'].queryset = EventCategory.objects.all().filter(methodists=loggedin_user)
    def save(self, commit=True):
        user = super(EventAddFormMethodist, self).save(commit=False)
        if commit:
            user.save()
        return user

class UploadPhotoReport(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, "class": "form-control"}),label="Изображения")