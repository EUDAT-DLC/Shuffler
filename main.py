from flask import Flask, request, render_template
from random import shuffle

app = Flask(__name__)

app.config.update(dict(
    DEBUG=True,
))

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        file = request.files['file']
        content = file.stream.read(1024 * 1024)
        words = content.strip().split(' ')
        shuffle(words)
        return ' '.join(words)
    else:
        return render_template('main.html')

if __name__ == "__main__":
    app.run()
