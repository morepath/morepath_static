import bowerstatic
import os

from .model import Root
from .app import App


@App.html(model=Root)
def root_default(self, request):
    request.include('my_component')
    return ("<!DOCTYPE html><html><head></head><body>"
            "components are inserted in the HTML source</body></html>")


bower = bowerstatic.Bower()


components = bower.components(
    'app', os.path.join(os.path.dirname(__file__), 'bower_components'))


local = bower.local_components('local', components)


local.component(os.path.join(os.path.dirname(__file__), 'my_component'),
                version=None)


@App.static_components()
def get_static_components():
    return local
