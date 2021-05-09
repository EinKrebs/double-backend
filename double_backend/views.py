from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, FileResponse
from double_backend.models import (
    Category,
    Level,
    Theme,
    Word,
)


def get_all(cls):
    def res(request):
        objects = cls.objects.all()
        jsons = list(map(cls.to_json, objects))
        return JsonResponse(jsons, safe=False)

    return res


def get_id(request):
    path = request.path
    return path[path.find('/')]


def get_theme(request, theme_id=None):
    try:
        theme = Theme.objects.get(pk=theme_id)
    except ObjectDoesNotExist:
        return JsonResponse({})
    words = Word.objects.filter(themes__pk=theme_id)
    res = theme.to_json()
    res['words'] = list(map(Word.to_json_short, words))
    return JsonResponse(res)


def get_word(request, word_id=None):
    try:
        print(Word.objects.get(id=word_id).to_json())
        return JsonResponse(Word.objects.get(id=word_id).to_json())
    except ObjectDoesNotExist:
        return JsonResponse({})


def get_file(request, file_path=None):
    return FileResponse(open('media/' + file_path, 'rb'))
