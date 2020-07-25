# Copyright 2020 The `Kumar Nityan Suman` (https://github.com/nityansuman/). All Rights Reserved.
#
#                     GNU GENERAL PUBLIC LICENSE
#                        Version 3, 29 June 2007
#  Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
#  Everyone is permitted to copy and distribute verbatim copies
#  of this license document, but changing it is not allowed.
# ==============================================================================


# Import packages
import os
import pandas as pd
import numpy as np
from datetime import datetime
from fbprophet import Prophet
from itertools import zip_longest
from flask import request, redirect
from flask import render_template, request, session
from werkzeug.utils import secure_filename
from src import app


@app.route('/')
@app.route('/home')
def home():
    ''' Renders the home page '''
    session["date"] = datetime.now()
    return render_template(
        "index.html"
    )
