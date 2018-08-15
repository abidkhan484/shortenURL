import functools
import validators

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from shortenURL.db import get_db
import shortenURL.myFunction as fn

bp = Blueprint('application', __name__)



"""All the routes are given below"""


@bp.route("/", methods=["GET", "POST"])
def index():
    db = get_db()
    if request.method=="POST":
        givenURL = request.form.get("givenURL")
        if not validators.url(givenURL):
            # make here flash message
            message = "url not valid"
            flash(message)
            return redirect(url_for('application.index'))
        givenURL = givenURL.strip('/')
        index = fn.find_shorten_url_index(givenURL)
        url = request.base_url + fn.encode_url(index)

        return render_template('index.html', returnURL=url)

    return render_template('index.html')


@bp.route('/<string:url>')
def get_original_url(url):
    url_index = fn.decode_url(url)

    if url_index == -1:
        # make here flash message
        message = "404, url not found or expired"
        flash(message)
        return redirect(url_for('application.index'))

    original_url = fn.find_original_url(url_index)
    return redirect(original_url)


@bp.route('/all')
def show_entries():
	db = get_db()
	cur = db.execute('select id, url, created_at from entries order by id desc')
	entries = cur.fetchall()
	return render_template('show_entries.html', entries=entries)

'''
# please complete with proper logic

@bp.route('/delete')
def delete_database():
    db = get_db()
    db.execute('DELETE FROM entries')
    db.commit()
    mess = "You have deleted all the records"
    return render_template('delete_entries.html', message=mess)
'''
