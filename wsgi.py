import app as bbs
app = bbs.configured_app()


# gunicorn wsgi:app
# nohup gunicorn -b '0.0.0.0:80' wsgi:app &
