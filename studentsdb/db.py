#for settings.py in studentsdb Project
DATABASES_for_pr = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        #'USER': 'students_user1',
        #'PASSWORD': '5282',
        'USER': 'root',
        'PASSWORD': '5282',
        'NAME': 'students_db1',
        'TEST': {
        	'CHARSET': 'utf8',
        	'COLLATION': 'utf8_general_ci',
        },
    }
}