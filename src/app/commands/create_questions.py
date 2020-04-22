from flask_script import Command

from src.app import db


class CreateQuestionsCommand(Command):

    def run(self):
        create_reports()
        print('Reports created.')


def create_reports():
    """ Create users """

    # Create all tables if not exists
    db.create_all()
