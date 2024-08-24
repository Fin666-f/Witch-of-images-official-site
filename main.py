import os

from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route("/")
@app.route("/main_page")
def main_page():
    return render_template('main page.html')


@app.route("/guide_page")
def guide_page():
    return render_template('guide page.html')


@app.route('/download_file')
def download_file():
    path = 'static/Witch_of_images_WINDOWS_1.0_SETUP_RU.exe'
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)