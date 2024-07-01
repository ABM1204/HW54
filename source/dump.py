import os
import sys
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HW54.settings')
django.setup()

with open('source/online_shop/fixtures/data.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata', 'online_shop.Category', 'online_shop.Product', indent=4, stdout=f)
