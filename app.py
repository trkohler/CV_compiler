from flask import Flask
import yaml
from flask.templating import render_template

app = Flask(__name__)

app.static_folder = 'static/'
app.template_folder = 'static/templates/'

@app.route('/<code>')
def main(code):
    func_name = 'cv_compiler'
    return render_template("main.html", code=code)

@app.route('/cv/<method>')
def render(method):
    with open(r'cv_draft.yaml') as file:
        cv = yaml.full_load(file)
        if int(method) == 0:
            return render_template("plain.html", context=cv)
        
        return render_template('cv.html', context=cv)


if __name__ == '__main__':
    app.run(debug=True)