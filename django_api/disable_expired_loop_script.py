import time

from django.utils import timezone

import django
import os

# Setting django evironment to the script
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_api.settings")
django.setup()
from api.models import Token


def main():
    while (True):
        print('tick')
        datetime_now = timezone.now()
        all_tokens = Token.objects.all()
        for token in all_tokens:
            if token.expiration_datetime < datetime_now:
                print("turning off {}".format(token))
                token.status = False
                token.save()
        # run every hour
        interval = 3600
        time.sleep(interval - time.time() % interval)


if __name__ == '__main__':
    main()
