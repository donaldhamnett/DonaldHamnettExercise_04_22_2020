import logging
import traceback

import requests
from flask import flash, render_template, request

logger = logging.getLogger(__name__)

from app.update import update
from app.update.forms import UpdateForm


@update.route('/update', methods=['GET', 'POST'], strict_slashes=False)
def update():
    try:
        form = UpdateForm()
        if form.validate_on_submit():
            truncate = len('/update')
            if request.base_url[-1] == '/':
                truncate += 1
            url = request.base_url[:-truncate]
            response = requests.patch(f'{url}/api/v1/questions/', json={'question': form.question.data,
                                                                        'id': form.id.data})
            flash('You have successfully Updated a question!')
            context = response.json()
            print(context)
            return render_template('update/update_result.html', context=context, url=request.base_url)


        return render_template('update/update.html', form=form, title='Update')

    except Exception as e:
        logger.error(f'Create: Error while processing request.\n{str(e)}\n{str(traceback.print_exc())}')
        return render_template('error/error.html')



