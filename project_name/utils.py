from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.conf import settings


class Email(object):
	def __init__(self, *a, **k):
		self.kwargs = k
		
	def get_context_data(self, *a, **k):
		context = self.kwargs or {}
		
		#add static url in
		context['DOMAIN'] = settings.DOMAIN
		context['STATIC_URL'] = context['DOMAIN'] + settings.STATIC_URL
		
		#
		return context
	
	def send(self, to, cc=None):
		text = get_template(self.get_template_location(suffix='txt'))
		html = get_template(self.get_template_location(suffix='html'))
		
		context = Context(self.get_context_data())
		subject = self.get_subject()

		text_content = text.render(context)
		html_content = html.render(context)
		
		parameters = {
			'subject': subject,
			'body': text_content,
			'from_email': '%s <%s>' % (self.get_from(), settings.EMAIL_NOTIFICATIONS_FROM),
			'to': [to],
			'headers': self.get_headers(),
		}
		
		if cc:
			parameters['cc'] = cc if isinstance(cc, list) else [cc]
		
		msg = EmailMultiAlternatives(**parameters)
		msg.attach_alternative(html_content, 'text/html')
		
		return msg.send()
	
	def get_template_location(self, suffix):
		return '.'.join([self.template_name, suffix])
	
	def get_subject(self):
		return self.subject
	
	def get_from(self):
		return self.from_name
	
	def get_headers(self):
		return {}
	