import morepath
from more.static import StaticApp
import bowerstatic
import os


class app(StaticApp):
    pass


@app.path(path='/')
class Root(object):
    pass


@app.html(model=Root)
def root_default(self, request):
    request.include('jquery')
    return ("<!DOCTYPE html><html><head></head><body>"
            "jquery is inserted in the HTML source</body></html>")


bower = bowerstatic.Bower()


components = bower.components(
    'app', os.path.join(os.path.dirname(__file__), 'bower_components'))


@app.static_components()
def get_static_components():
    return components


def main():
    morepath.autosetup()
    wsgi = bower.wrap(app())
    morepath.run(wsgi)
