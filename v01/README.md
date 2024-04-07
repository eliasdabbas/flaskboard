# v01 The most minimal irreducible integration

* Three dashboards are created using a minimal structure (imports, instantiate an app, create a layout).
* `dashboard1`, `dashboard2`, and `home` are our Dash apps, living separately in separate files.
* The `app.py` file is where the Flask app lives.
* The dash apps are instantiated with `server=False` and  `url_base_pathname='/<dashboard_name>/'`
  * This will create the apps without creating a server
  * It will set the part of the app (the blueprint) that this will manage `/<dashboard_name>/`
* The main Flask app will import those apps, and register them as blueprints with the standard `init_app` method. 

To run:

```bash
cd v01/
export FLASK_APP=app.py
flask run
```
