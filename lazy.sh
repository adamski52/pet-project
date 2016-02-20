source ~/Projects/env/bin/activate
python ~/Projects/storybook/manage.py makemigrations api
python ~/Projects/storybook/manage.py migrate
python ~/Projects/storybook/manage.py runserver
