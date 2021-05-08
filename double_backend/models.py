from django.db import models
from django.contrib import admin


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
            'icon': self.icon if self.icon is not None else '',
        }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


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


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    pass


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
            'photo': self.photo
        }


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    pass


class Word(models.Model):
    name = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    transcription = models.CharField(max_length=255,
                                     blank=True,
                                     null=False)
    example = models.TextField(blank=True,
                               null=False)
    sound = models.URLField(max_length=255,
                            blank=True,
                            null=False)
    themes = models.ManyToManyField(Theme)

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


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    pass
