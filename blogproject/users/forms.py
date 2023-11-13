import uuid
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class RegisteForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "nickname")

    def save(self, *args, **kwargs):
        self.instance.username = uuid.uuid1()
        super(RegisteForm, self).save(*args, **kwargs)


class AuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = '用户名或邮箱'
        self.fields['password'].help_text = '<a href="/password/reset/">忘记密码?点击找回!</a>'
