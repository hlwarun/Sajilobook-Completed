# from django import forms
# from django.contrib.auth.models import User
# from user.models import Profile
#
# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'email']
#
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         field = ['mobile']

# from django import forms
# from django.utils.translation import ugettext, ugettext_lazy as _
# from collections import OrderedDict
# from django.contrib.auth.views import SetPasswordForm
# #
# # class PasswordChange(PasswordChangeForm):
# #     old_password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'myInput'}))
#
# class PasswordChangeForm(SetPasswordForm):
#     error_messages = dict(SetPasswordForm.error_messages, **{
#         'password_incorrect': _("Your old password was entered incorrectly. "
#                                 "Please enter it again."),
#     })
#     old_password = forms.CharField(label=_("Old password"), widget=forms.PasswordInput(attrs={'id':'myInput'}))
#
#     def clean_old_password(self):
#         old_password = self.cleaned_data["old_password"]
#         if not self.user.check_password(old_password):
#             raise forms.ValidationError(
#                 self.error_messages['password_incorrect'],
#                 code='password_incorrect',
#             )
#         return old_password
#
#
# PasswordChangeForm.base_fields = OrderedDict(
#     (k, PasswordChangeForm.base_fields[k])
#     for k in ['old_password', 'new_password1', 'new_password2']
# )
