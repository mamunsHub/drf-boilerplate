from django.contrib.auth.tokens import default_token_generator

from djoser import utils
from djoser.conf import settings

from utils.email import BaseEmailMessage


class ActivationEmail(BaseEmailMessage):
    template_name = 'email/activation.html'

    def get_context_data(self):
        context = super(ActivationEmail, self).get_context_data()

        user = context.get('user')
        context['alert'] = True
        context['uid'] = utils.encode_uid(user.pk)
        context['token'] = default_token_generator.make_token(user)
        context['url'] = settings.ACTIVATION_URL.format(**context)
        return context