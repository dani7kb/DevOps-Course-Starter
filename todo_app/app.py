from flask import Flask
from flask import render_template, request, redirect, url_for

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items
from todo_app.data.session_items import add_item


app = Flask(__name__)
app.config.from_object(Config())



@app.route('/')
def index():
    # show all to-do items
    items = get_items()
    return render_template("index.html", items=items)


@app.route('/New_List', methods=["POST"])
def New_List():
    # add new item
    title = request.form.get("title")
    add_item(title)
    #New_List(add_item)

    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run()