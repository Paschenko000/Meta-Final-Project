# Meta-Final-Project
Admin Login Details:
User: admin
Passwrd: Gfhjkm123

You need to be authenticated to add menu items. So before trying to add menu items, go to http://127.0.0.1:8000/admin

How to delete menu items:
http://127.0.0.1:8000/menu-items/{menu-item-id-here}
example:
http://127.0.0.1:8000/menu-items/1

API URLs:
http://127.0.0.1:8000/menu-items/ (Authentication Required)
http://127.0.0.1:8000/menu-items/{menu-item-id-here} (Authentication Required)
http://127.0.0.1:8000/reservations/
http://127.0.0.1:8000/booking/tables/

Default Database: MySql.
If you do not wish to use MySql, please change the database settings with the following:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
