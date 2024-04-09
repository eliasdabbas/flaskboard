# v02 Using Jinja templates and embedding Dash apps anywhere you want

* We now create routes for our Flask `app` object.
* Each route view function will `return render_template`, which is a pure HTML page, that will be rendered on every URL. The difference is that it takes variables for objects to be inserted wherever we want.
* The relevant Dash app will be given to `render_template` and injeted into our HTML page where we placed it.
* Dash apps have an `index` method which gives the body of the app (`app.index()`). This is what we will use in the dynamic region of every page.
* We also create a `/templates/` folder in which we can add as many page templates as we want.
* A "base.html" template was created to be used.
* We now have a template of content that appear on all pages, fully manged by Flask. In this template the dynamic part gets a Dash app and displays its content and functionality.
* Important: The routes that belong to the Flask app should not have the same path as the `url_base_pathname` in the Dash apps. Otherwise that path would be managed by the Dash app. One approach might be to use the same paths, but prepend the Dash apps' path with a special folder, here I use `/test/`.

To run:

```bash
cd v02/
export FLASK_APP=app.py
flask run
```
