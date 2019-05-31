echo "Hello,Django-blog starting...."
nohup gunicorn blogProject.wsgi:application -b 127.0.0.1:8000  1>blog.log 2>error.log &

jobs -l

