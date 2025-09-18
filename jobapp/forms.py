from ckeditor.widgets import CKEditorWidget
from jobapp.models import *
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django import forms


class JobForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].label = "Job Title :"
        self.fields['location'].label = "Job Location :"
        self.fields['salary'].label = "Salary :"
        self.fields['description'].label = "Job Description :"
        self.fields['tags'].label = "Tags :"
        self.fields['last_date'].label = "Submission Deadline :"
        self.fields['company_name'].label = "Company Name :"
        self.fields['url'].label = "Website :"

        # Make category optional
        self.fields['category'].required = False

        # Placeholders
        self.fields['title'].widget.attrs.update(
            {'placeholder': 'eg : Software Developer'})
        self.fields['location'].widget.attrs.update(
            {'placeholder': 'eg : Lagos, Nigeria'})
        self.fields['salary'].widget.attrs.update(
            {'placeholder': '$800 - $1200'})
        self.fields['tags'].widget.attrs.update(
            {'placeholder': 'Python, JavaScript'})
        self.fields['last_date'].widget.attrs.update(
            {'placeholder': 'YYYY-MM-DD'})
        self.fields['company_name'].widget.attrs.update(
            {'placeholder': 'Company Name'})
        self.fields['url'].widget.attrs.update(
            {'placeholder': 'https://example.com'})

    class Meta:
        model = Job
        fields = [
            "title",
            "location",
            "job_type",
            "category",   # still here but not required
            "salary",
            "description",
            "tags",
            "last_date",
            "company_name",
            "company_description",
            "url"
        ]

    def clean_job_type(self):
        job_type = self.cleaned_data.get('job_type')
        if not job_type:
            raise forms.ValidationError("Job Type is required")
        return job_type


class JobApplyForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['job']


class JobBookmarkForm(forms.ModelForm):
    class Meta:
        model = BookmarkJob
        fields = ['job']


class JobEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].label = "Job Title :"
        self.fields['location'].label = "Job Location :"
        self.fields['salary'].label = "Salary :"
        self.fields['description'].label = "Job Description :"
        self.fields['last_date'].label = "Dead Line :"
        self.fields['company_name'].label = "Company Name :"
        self.fields['url'].label = "Website :"

        # Make category optional
        self.fields['category'].required = False

        # Placeholders
        self.fields['title'].widget.attrs.update(
            {'placeholder': 'eg : Software Developer'})
        self.fields['location'].widget.attrs.update(
            {'placeholder': 'eg : Lagos, Nigeria'})
        self.fields['salary'].widget.attrs.update(
            {'placeholder': '$800 - $1200'})
        self.fields['last_date'].widget.attrs.update(
            {'placeholder': 'YYYY-MM-DD'})
        self.fields['company_name'].widget.attrs.update(
            {'placeholder': 'Company Name'})
        self.fields['url'].widget.attrs.update(
            {'placeholder': 'https://example.com'})

    class Meta:
        model = Job
        fields = [
            "title",
            "location",
            "job_type",
            "category",   # still here but optional
            "salary",
            "description",
            "last_date",
            "company_name",
            "company_description",
            "url"
        ]

    def clean_job_type(self):
        job_type = self.cleaned_data.get('job_type')
        if not job_type:
            raise forms.ValidationError("Job Type is required")
        return job_type
