import os

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME', None)
if HEROKU_APP_NAME is not None:
    API_TOKEN = os.environ.get('API_TOKEN') # for heroku
    HEROKU = True

    # webhook settings
    WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
    WEBHOOK_PATH = f'/webhook/{API_TOKEN}'
    WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

    # webserver settings
    WEBAPP_HOST = '0.0.0.0'
    WEBAPP_PORT = os.getenv('PORT', default=443)
else:
    print("Aslida dastur Webhook uchun moslashtirilgan edi.")
    API_TOKEN = "12345:aabbcc"