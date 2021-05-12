from django.db import models
from django.utils.safestring import mark_safe


class Category(models.Model):
    name = models.CharField(max_length=255,
                            unique=True,)
    icon = models.ImageField(blank=True,
                             upload_to='images/category_icons',
                             )

    def __str__(self):
        return f'Category {self.name}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'icon': self.icon.url if self.icon else '',
        }

    def icon_preview(self):
        if self.icon:
            return mark_safe(f'<img src="{ self.icon.url}" width="150" height="150" />')
        else:
            return '(No image)'
    icon_preview.short_description = 'Icon preview'


class Level(models.Model):
    name = models.CharField(max_length=255,
                            unique=True)
    code = models.CharField(max_length=2,
                            unique=True)

    def __str__(self):
        return f'Level {self.name}: {self.code}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
        }


class Theme(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)
    level = models.ForeignKey(Level,
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    photo = models.ImageField(blank=True,
                              upload_to='images/theme_photos',
                              )

    def __str__(self):
        return f'Theme {self.name}'

    def to_json(self):
        return {
            'id': self.id,
            'category': self.category.id,
            'level': self.level.id,
            'name': self.name,
            'photo': self.photo.url if self.photo else ''
        }

    def photo_preview(self):
        if self.photo:
            return mark_safe(f'<img src="{ self.photo.url}" width="150" height="150" />')
        else:
            return '(No image)'
    photo_preview.short_description = 'Photo preview'


class Word(models.Model):
    name = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    transcription = models.CharField(max_length=255,
                                     blank=True,
                                     null=False)
    example = models.TextField(blank=True,
                               null=False)
    themes = models.ManyToManyField(Theme)
    sound = models.FileField(upload_to='sounds',
                             blank=True)

    def __str__(self):
        return f'Word {self.name}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'translation': self.translation,
            'transcription': self.transcription,
            'example': self.example,
            'sound': self.sound,
        }

    def to_json_short(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def sound_player(self):
        if self.sound:
            sound_type = self.sound.name[self.sound.name.rfind('.') + 1:]
            if sound_type == 'mp3':
                src_type = 'mpeg'
            else:
                src_type = 'ogg'
            src_type = 'audio/' + src_type
            return mark_safe(
                f'<audio controls> '
                f'<source src="{self.sound.url}" type="{src_type}"> '
                f"Your browser doesn't support the audio element </audio>"
            )
        else:
            return '(No sound)'
    sound_player.short_description = 'Sound preview'
