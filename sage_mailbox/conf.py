from django.conf import settings

from sage_mailbox.exc import IMAPConfigurationError

DEFAULTS = {
    "IMAP_SERVER_DOMAIN": None,
    "IMAP_SERVER_PORT": 993,
    "IMAP_SERVER_USER": None,
    "IMAP_SERVER_PASSWORD": None,
    "IMAP_DEBUG_ENABLED": True,
}


class IMAPSettings:
    def __init__(self):
        self._settings = {}
        for setting, default in DEFAULTS.items():
            value = getattr(settings, setting, default)
            if value is None and setting not in ["MAILCOW_DEBUG_ENABLED"]:
                raise IMAPConfigurationError(
                    f"{setting} must be set in your Django settings."
                )
            self._settings[setting] = value

    def __getattr__(self, item):
        if item in self._settings:
            return self._settings[item]
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{item}'"
        )


imap_settings = IMAPSettings()
