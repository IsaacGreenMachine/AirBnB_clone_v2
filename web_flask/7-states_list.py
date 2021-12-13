#!/usr/bin/python3
'''Starts a Flask Web app'''
if __name__ == '__main__':
    from flask import Flask, render_template
    from models import storage
    from models.state import State

    app = Flask(__name__)

    @app.teardown_appcontext
    def teardown(context):
        """Flask Teardown"""
        storage.close()

    @app.route('/states_list', strict_slashes=False)
    def statesList():
        state_list = storage.all(State)
        return render_template("7-states_list.html", state_list=state_list)

    app.run(debug=True, host='0.0.0.0')
