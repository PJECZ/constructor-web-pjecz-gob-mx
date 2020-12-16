"""
Articles Lists JSON
===================

Create lists in JSON from articles and pages.

"""
import json
from pathlib import Path

from bs4 import BeautifulSoup
from pelican import signals


class Articles_Lists_JSON_Generator(object):
    """ Description """

    def __init__(self, context, settings, path, theme, output_path, *null):
        self.context = context
        self.siteurl = settings.get('SITEURL')
        self.relative_urls = settings.get('RELATIVE_URLS')
        self.output_path = output_path
        self.json_output_path = 'json'
        if settings.get('ARTICLES_LISTS_JSON_OUTPUT_PATH'):
            self.json_output_path = settings.get('ARTICLES_LISTS_JSON_OUTPUT_PATH')
        self.output_all = 'all.json'
        if settings.get('ARTICLES_LISTS_JSON_OUTPUT_ALL'):
            self.json_output_all_file = settings.get('ARTICLES_LISTS_JSON_OUTPUT_ALL')
        self.categories_filters = []
        if settings.get('ARTICLES_LISTS_JSON_CATEGORIES_FILTERS'):
            self.categories_filters = settings.get('ARTICLES_LISTS_JSON_CATEGORIES_FILTERS')
        self.limit = 48
        if settings.get('ARTICLES_LISTS_JSON_LIMIT'):
            self.limit = int(settings.get('ARTICLES_LISTS_JSON_LIMIT'))

    def agregar_nodo(self, item):
        """ Add node """
        # Descartar si no está publicado
        if getattr(item, 'status', 'published') != 'published':
            return
        # Obtener título
        soup_title = BeautifulSoup(item.title.replace('&nbsp;', ' '), 'html.parser')
        page_title = soup_title.get_text(' ', strip=True).replace('“', '"').replace('”', '"').replace('’', "'").replace('^', '&#94;')
        # Determinar resumen
        page_summary = ''
        if getattr(item, 'summary', 'None') != 'None':
            soup_summary = BeautifulSoup(item.summary, 'html.parser')
            page_summary = soup_summary.get_text()
        # Obtener categoría
        page_category = item.category.name if getattr(item, 'category', 'None') != 'None' else ''
        # Determinar URL
        page_url = '.'
        if item.url:
            page_url = item.url if self.relative_urls else (self.siteurl + '/' + item.url)
        # Obtener imagen previa
        page_preview = ''
        if getattr(item, 'preview', 'None') != 'None':
            page_preview = page_url + '/' + getattr(item, 'preview', 'None')
        # Diccionario con el nodo
        node = {
            'title': page_title,
            'summary': page_summary,
            'category': page_category,
            'url': page_url,
            'preview': page_preview,
        }
        # Entregar
        return node

    def generate_output(self, writer):
        """ Generate output """
        # Acumular
        all_nodes = []
        categories_nodes = {}
        for page in self.context['articles']:
            node = self.agregar_nodo(page)
            all_nodes.append(node)
            for category_file_name, categories in self.categories_filters:
                # if node['category'] in categories:
                categories_nodes[category_file_name].append(node)
        # Directorio
        output_dir = Path(self.output_path, self.json_output_path)
        output_dir.mkdir(parents=True, exist_ok=True)
        # Guardar cada categoría en su JSON
        # for category_file_name, nodes in categories_nodes.items():
        #     category_output_file = Path(output_dir, category_file_name)
        #     raiz_nodo = { 'data': nodes }
        #     with open(category_output_file, 'w', encoding='utf-8') as pointer:
        #         pointer.write(json.dumps(raiz_nodo, separators=(',', ':'), ensure_ascii=False))
        # Guardar todos los nodos en su JSON
        all_output_file = Path(output_dir, self.output_all)
        raiz_nodo = { 'data': all_nodes }
        with open(all_output_file, 'w', encoding='utf-8') as pointer:
            pointer.write(json.dumps(raiz_nodo, separators=(',', ':'), ensure_ascii=False))


def get_generators(generators):
    """ Get generators """
    return Articles_Lists_JSON_Generator


def register():
    """ Register """
    signals.get_generators.connect(get_generators)
