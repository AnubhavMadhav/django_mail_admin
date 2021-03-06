from mailbox import Maildir

from django_mail_admin.transports.generic import GenericFileMailbox


class MaildirTransport(GenericFileMailbox):
    _variant = Maildir

    def get_instance(self):
        return self._variant(self._path, None)
