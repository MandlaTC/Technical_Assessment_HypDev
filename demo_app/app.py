import io
from chess import pgn, svg
import datetime
import os
from flask import Flask, request, flash, render_template, url_for, redirect, Markup, render_template_string
import dropbox
from dotenv import load_dotenv
load_dotenv()


SECRET_KEY = os.environ.get("DROPBOX_KEY")
UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER")
DELETE_FOLDER = os.environ.get("DELETE_FOLDER")

app = Flask(__name__)

dbx = dropbox.Dropbox(SECRET_KEY)


@app.route('/')
def hello():
    return redirect(url_for('dbx_list_games'))


@app.route('/list-games', methods=['POST', 'GET'])
def dbx_list_games():

    if request.method == 'POST':
        form_res = list(request.form.values())[0]
        return dbx_get_game(form_res)
    elif request.method == 'GET':
        try:
            entry_list = [
                entry.name for entry in dbx.files_list_folder('').entries]
            return render_template('list_games.html', your_list=entry_list)
        except dropbox.exceptions.HttpError as err:
            print('*** HTTP error', err)
            return ('500: Internal Server Error')


def download(name):
    """Download a file.

    Return the bytes of the file, or None if it doesn't exist.
    """
    path = str('/'+name).rstrip()
    try:
        md, res = dbx.files_download(path)
    except dropbox.exceptions.HttpError as err:
        print('*** HTTP error', err)
        return None
    data = res.content

    return data


def get_game_svg(game):
    board = game.board()
    svgs = []
    for move in game.mainline_moves():
        board.push(move)
        svgs.append(Markup(svg.board(board, size=350)))
    return svgs


@app.route('/game/<game_name>')
def dbx_get_game(game_name):
    pgn_file = io.StringIO(download(game_name).decode(encoding='utf-8'))

    games = []

    while True:
        game = pgn.read_game(pgn_file)
        if game is None:
            break  # end of file

        games.append(game)

    # games = games[len(games)-10: len(games)-1]
    # svgs = []
    # for game in games:
    #     svgs.append(get_game_svg(game))

    return render_template("show_game.html", svgs=get_game_svg(games[len(games)-1]), game=games[len(games)-1])


def allowed_file(filename):
    return filename.rsplit('.', 1)[1].lower() == 'pgn'


@app.route('/upload', methods=['POST', 'GET'])
def dbx_put_game():
    # dbx.files_upload("")
    # return 'post ' + game_name
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        f = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if f.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if f and allowed_file(f.filename):
            # f.save(os.path.join(UPLOAD_FOLDER, f.filename))
            try:
                dbx.files_upload(f.read(), "/"+f.filename.rsplit('.', 1)[0]+str(datetime.datetime.now())
                                 + "." + f.filename.rsplit('.', 1)[1])
            except dropbox.exceptions.HttpError as err:
                print('*** HTTP error', err)
        return redirect(url_for('dbx_list_games'))
    else:
        return render_template("upload_game.html")
