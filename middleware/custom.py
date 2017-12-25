from django.conf.global_settings import LANGUAGES

from django.utils.deprecation import MiddlewareMixin

class URLMiddleware(MiddlewareMixin):
    def process_request(self,request):
        print ("dddddddddddddd")
        l_path = request.path.split('/')
        request.session['no_lang_path'] = request.path
        codes = []
        for code,name in LANGUAGES:
            codes.append(code)
        if l_path[1] in codes:
            del l_path[1]
            no_lang_path = '/'.join(l_path)
            request.session['no_lang_path'] = no_lang_path