#!/usr/bin/env bash

source /xy/application/env/bin/activate
cp /xy/application/MutualFundAnalysis/settings.py MutualFundAnalysis/settings.py
python manage.py runserver 0.0.0.0:8000
