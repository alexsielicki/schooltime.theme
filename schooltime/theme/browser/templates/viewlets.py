from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.links.viewlets import FaviconViewlet


class ThemedFaviconViewlet(FaviconViewlet):
    """A custom version of the favicon viewlet
    
    This class is needed because the favicon viewlet still uses the render method
    which you can't override in zcml with template attribute.
    So I'm adding this class and using the index method to specify the page template.
    The index method can be overriden in zcml.
    """

    def render(self):
        # defer to index method, because that's what gets overridden by the template ZCML attribute
        return self.index()

    index = ViewPageTemplateFile('favicon.pt')

