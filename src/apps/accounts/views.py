import random, string

from django.views.generic import FormView, UpdateView, CreateView, TemplateView
from django.views import View
from django.contrib.auth import get_user_model, forms as auth_forms,\
    views as auth_views
from django.contrib import messages
from django.core.mail import EmailMessage
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext as _

from .forms import UserModelForm, UserSignupForm
from .permissions import LoginRequiredMixin

User = get_user_model()

class PasswordResetView(auth_views.PasswordResetView):
    """..."""
    template_name='accounts/reset_password.jinja'
    email_template_name = 'emails/password_reset_email.jinja'
    subject_template_name = 'emails/password_reset_subject.jinja'
    success_url = reverse_lazy('accounts:reset-done')


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    """..."""
    template_name='accounts/reset_confirm.jinja'
    success_url = reverse_lazy('accounts:reset-complete')


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    """..."""
    template_name='accounts/reset_done.jinja'


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/reset_complete.jinja'


class LoginView(FormView):
    """..."""
    def dispatch(self, *args, **kwargs):
        print(args)
        print('*******')
        print(kwargs)
        return super().dispatch(*args, **kwargs)


class ConfirmView(TemplateView):
    """..."""
    template_name = 'accounts/confirm.jinja'

    def get_context_data(self, token, *args, **kwargs):
        """..."""
        context = super().get_context_data(*args, **kwargs)
        try:
            user = User.objects.get(token=token)
            user.token = ''
            user.is_confirmed = 1
            user.is_active = 1
            user.save()
            messages.add_message(
                self.request,
                messages.SUCCESS,
                _('Account confirm sucessfull')
            )
        except:
            messages.add_message(
                self.request,
                messages.WARNING,
                _('Some errors occured, when trying activate account.')
            )

        return context


class SignUpView(CreateView):
    """..."""
    template_name='accounts/signup.jinja'
    form_class=UserSignupForm
    success_url='/'

    def form_valid(self, form, *args, **kwargs):
        """..."""

        token = ''.join(
            random.choice(string.ascii_uppercase) for _ in range(32)
        )

        form.instance.email = form.instance.email.lower()
        form.instance.token = token
        form.instance.is_active = 0
        
        messages.add_message(
            self.request,
            messages.INFO,
            'Вы успешно зарегистрировались. Для использования сайта необходимо подтвердить учетную запись. Ссылка для подтверждения отправлена на email.'
        )
        
        message_list = ['Здравствуйте! Благодарим Вас за открытие личного кабинета для регистрации площадок на “Центавр-2017/18”!',
            '','Для завершения реистрации перейдите по ссылке: ',
            'http://lk.moskvasirius.ru/accounts/confirm/{0}/'.format(token),
            '','Адрес сайта: http://lk.moskvasirius.ru','',
            'Регистрационные данные:',
            '----------------------------------------',
            'Email: {0}'.format(form.instance.email),
            'Пароль: {0}'.format(self.request.POST.get('password1','***')),
            '----------------------------------------',
            '', 'Если у Вас остаются вопросы, Вы можете обратиться:',
            'на e-mail: 89167271327@yandex.ru ', 'или позвонить по телефону: +7(916)727-13-27']
        try:
            email = EmailMessage(
                'Регистрация на сайте!',
                "\n".join(message_list),
                to=[form.instance.email]
            )
            email.send()
        except:
            pass

        return super().form_valid(form, *args, **kwargs)


class UpdateUser(UpdateView):
    """..."""
    form_class = UserModelForm
    template_name='accounts/update_user.jinja'
    success_url = '/'

    def get_object(self, queryset=None):
        """..."""
        return self.request.user


def handle_uploaded_file(f, chunk, filename):
    """Here you can do whatever you like with your files, like resize them if
    they are images

    :param f: the file
    :param chunk: number of chunk to save

    """

    if int(chunk) > 0:
        # opens for append
        _file = open(filename, 'a+b')
    else:
        # erases content
        _file = open(filename, 'w+b')

    if f.multiple_chunks:
        for chunk in f.chunks():
            _file.write(chunk)
    else:
        _file.write(f.read())
    _file.flush()
    return _file


class FilePlupload(LoginRequiredMixin, View):
    """..."""

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """..."""
        if request.method == 'POST' and request.FILES:
            save_to_root = settings.MEDIA_ROOT
            if not os.path.exists(save_to_root):
                os.makedirs(save_to_root)
            dir_fd = os.open(
                save_to_root,
                os.O_RDONLY
            )
            os.fchdir(dir_fd)
            for _file in request.FILES:

                file = request.FILES.get(_file)

                if file.size>1024*1024*5:
                    return JsonResponse({
                        'status': 'error',
                        'message': _('Max file size is %(size).2f mb')%{
                            'size': 5
                        }
                    })

                name = request.POST['name'].split('.')
                filename = '{name}_{hash}.{ext}'.format(
                    name='.'.join(name[:-1]),
                    hash=request.user.id,
                    ext=name[-1]
                )
                file = handle_uploaded_file(
                    request.FILES[_file],
                    request.POST.get('chunk', 0),
                    filename
                )

            #response to notify plUpload that the upload was successful
            os.close(dir_fd)
            content_file = ContentFile(file.read())

            request.user.photo.save(file.name, content_file, save=True)

            response = {
                'status': 'success',
                'storage': storage_data,
            }
        else:
            #response to notify plUpload that the upload was failed
            response = {
                'status': 'error'
            }
        return JsonResponse(response)
