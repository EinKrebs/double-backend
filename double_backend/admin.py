from django.contrib import admin

from double_backend.models import Category, Level, Theme, Word


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = (
        'icon_preview',
    )


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    pass


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    readonly_fields = (
        'photo_preview',
    )


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    readonly_fields = (
        'sound_player',
    )
