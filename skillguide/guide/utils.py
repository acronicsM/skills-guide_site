class DataMixin:
    title_page = url_name = None
    extra_context = dict()

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if self.url_name:
            self.extra_context['url_name'] = self.url_name

    @staticmethod
    def get_mixin_context(context, **kwargs):
        context.update(kwargs)

        return context
