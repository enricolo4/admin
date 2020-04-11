from falcon import API, Response, MEDIA_JS, MEDIA_HTML
from falcon_jinja2 import FalconTemplate

falcon_template = FalconTemplate()


class Index:
    @falcon_template.render('index/index.html')
    def on_get(self, req, resp):
        resp.context = {'framework': 'Falcon'}


class Health:
    @falcon_template.render('register/test.html')
    def on_get(self, req, resp: Response):
        resp.content_type = MEDIA_JS
        resp.content_type = MEDIA_HTML
        resp.context = {'framework': 'Falcon'}


app = API(media_type=MEDIA_HTML)

app.add_route("/", Index())
app.add_route("/health", Health())
