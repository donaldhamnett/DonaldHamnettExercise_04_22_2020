import logging
import traceback

import requests
from flask import flash, render_template, request

logger = logging.getLogger(__name__)

from app.create import create
from app.create.forms import CreateForm


@create.route('/create', methods=['GET', 'POST'], strict_slashes=False)
def create():
    try:
        form = CreateForm()
        if form.validate_on_submit():
            truncate = len('/create')
            if request.base_url[-1] == '/':
                truncate += 1
            url = request.base_url[:-truncate]
            response = requests.post(f'{url}/api/v1/questions/', json={'question': form.question.data})
            flash('You have successfully created a question!')
            return render_template('create/create_result.html', context=response.json())


        return render_template('create/create.html', form=form, title='Create')

    except Exception as e:
        logger.error(f'Create: Error while processing request.\n{str(e)}\n{str(traceback.print_exc())}')
        return render_template('error/error.html')



