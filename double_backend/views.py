from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, FileResponse, HttpResponse
from double_backend.models import (
    Theme,
    Word,
)
from double_backend.settings import API_SECRET


def check_secret(handler):
    def res(request):
        if ('Secret' not in request.headers
                or request.headers['Secret'] != API_SECRET):
            print(request.headers['Secret'])
            return HttpResponse(status=403)
        else:
            return handler(request)

    return res


def get_all(cls):
    @check_secret
    def res(request):
        objects = cls.objects.all()
        jsons = list(map(cls.to_json, objects))
        return JsonResponse(jsons, safe=False)

    return res


@check_secret
def get_theme(request, theme_id=None):
    try:
        theme = Theme.objects.get(pk=theme_id)
    except ObjectDoesNotExist:
        return JsonResponse({})
    words = Word.objects.filter(themes__pk=theme_id)
    res = theme.to_json()
    res['words'] = list(map(Word.to_json_short, words))
    return JsonResponse(res)


@check_secret
def get_word(request, word_id=None):
    try:
        print(Word.objects.get(id=word_id).to_json())
        return JsonResponse(Word.objects.get(id=word_id).to_json())
    except ObjectDoesNotExist:
        return JsonResponse({})


def get_file(request, file_path=None):
    return FileResponse(open('media/' + file_path, 'rb'))
