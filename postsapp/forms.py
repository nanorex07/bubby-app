from django import forms

from .models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('caption', 'media')

        widgets = {
            "caption": forms.Textarea(attrs={
                "class": "w-full py-2 px-4 rounded-xl mb-2 border"
            }),
            "media": forms.FileInput(attrs={
                "class": '''block w-full border border-gray-200 shadow-sm rounded-md text-sm focus:z-10 focus:border-blue-100 focus:ring-blue-200 dark:bg-slate-200 dark:border-gray-500 dark:text-gray-400
                file:bg-transparent file:border-0
                file:bg-gray-100 file:mr-4
                file:py-3 file:px-4
                dark:file:bg-gray-500 dark:file:text-gray-100'''
            }),
        }

    def clean(self):
        file = self.cleaned_data.get("media")
        file_exts = ("video/mp4", "video/webm", "image/jgp",
                     "image/png", "image/jpeg", "image/webp")
        if file is None:
            raise forms.ValidationError('Please select file first ')

        if file.content_type not in file_exts:
            raise forms.ValidationError("file type not supported.")

        return self.cleaned_data


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('caption',)

        widgets = {
            "caption": forms.Textarea(attrs={
                "class": "w-full py-2 px-4 rounded-xl mb-2 border"
            }),
        }
