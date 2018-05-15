#!/bin/bash

source /edx/app/edxapp/edxapp_env && python manage.py lms runserver 0.0.0.0:8001 --settings hedu
