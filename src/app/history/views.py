import logging
import traceback

import requests
from flask import flash, render_template, request

logger = logging.getLogger(__name__)

from app.history import history
from app.history.forms import HistoryForm


@history.route('/history', methods=['GET', 'POST'], strict_slashes=False)
def history():
    try:
        form = HistoryForm()
        if form.validate_on_submit():
            truncate = len('/history')
            if request.base_url[-1] == '/':
                truncate += 1
            url = request.base_url[:-truncate]
            response = requests.get(f'{url}/api/v1/questions/', json={'id': form.question.data})
            flash('You have successfully looked up a question!')
            print(response.json())
            return render_template('history/history_result.html', context=response.json())


        return render_template('history/history.html', form=form, title='history')

    except Exception as e:
        logger.error(f'history: Error while processing request.\n{str(e)}\n{str(traceback.print_exc())}')
        return render_template('error/error.html')



