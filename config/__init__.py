# Python 3.14+ compatibility patch for Django BaseContext/Context copying
import copy
try:
    from django.template import context as _django_context

    def _base_context_copy(self):
        duplicate = self.__class__.__new__(self.__class__)
        duplicate.dicts = self.dicts[:]
        return duplicate

    def _context_copy(self):
        duplicate = self.__class__.__new__(self.__class__)
        duplicate.dicts = self.dicts[:]
        duplicate.use_l10n = getattr(self, 'use_l10n', False)
        duplicate.use_tz = getattr(self, 'use_tz', False)
        duplicate.autoescape = getattr(self, 'autoescape', True)
        if hasattr(self, 'template'):
            duplicate.template = self.template
        if hasattr(self, 'render_context'):
            duplicate.render_context = copy.copy(self.render_context)
        return duplicate

    _django_context.BaseContext.__copy__ = _base_context_copy
    _django_context.Context.__copy__ = _context_copy
except Exception:
    pass
