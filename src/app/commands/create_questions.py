from flask_script import Command

from app import db


class CreateQuestionsCommand(Command):

    def run(self):
        create_all_tables()
        print('Question tables created.')


def create_all_tables():
    """ Create users """

    # Create all tables if not exists
    db.create_all()
