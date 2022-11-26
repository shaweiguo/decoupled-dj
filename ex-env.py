import os
import pathlib
import environ


BASE_DIR = environ.Path(__file__) - 1
print(BASE_DIR)
print(BASE_DIR('.env'))

# for i, v in enumerate(os.environ.items(), 1):
#     print(i, v)

# print(os.environ.get('HOMEPATH'))

# env = environ.Env()
# print(env.str('TEST_FOO'))
# env.prefix = "TEST_"
#
# print(env.str('FOO'))
# env = environ.Env(
#     TEST_FOO=(str, ''),
#     MAIL_ENABLED=(bool, False),
#     SMTP_LOGIN=(str, 'DEFAULT')
# )
env = environ.Env()

environ.Env.read_env(BASE_DIR('.env'))
print(env('MAIL_ENABLED'))
print(env('SMTP_LOGIN'))
print(env('TEST_FOO'))
print(env('DEBUG'))
print(env('DATABASE_URL'))
print(env('STATIC_URL'))
