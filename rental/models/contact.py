from django.db import models
import rental.tasks.apiMailer as mailer  # or gMailer


class Contact(models.Model):

    def __str__(self):
        return f"Message de {self.name}, le {self.date}"

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.EmailField(max_length=50)
    message = models.TextField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def send_confirmation(self):
        mailer.send_confirmation.delay(self.name, self.email)

    def send_notification(self):
        mailer.send_notification.delay(
            self.name,
            self.email,
            self.subject,
            self.message,
            self.date
        )
