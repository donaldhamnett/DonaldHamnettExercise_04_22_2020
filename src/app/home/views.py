import logging
import traceback
from flask import render_template

from app.home import home

logger = logging.getLogger(__name__)


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    try:
        return render_template('home/index.html', title="Welcome")
    except Exception as e:
        logger.error(f'Create: Error while processing request.\n{str(e)}\n{str(traceback.print_exc())}')
        return 'hello'



