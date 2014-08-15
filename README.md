Digg-like Paginator from Django Snippets
=====================


Originaly posted on Django snippets site by Michael Elsdörfer https://github.com/miracle2k

https://djangosnippets.org/snippets/773/

To setup use:

```
pip install django_digg_paginator
```

Can be used with generic ListView as simple as:

```
from digg_paginator import DiggPaginator

class MyCustomView(ListView):
    paginator_class = DiggPaginator
```

Template may look like this (assuming twitter bootstrap as css framework):

```
<div class="container" align="center">
    <ul class="pagination pagination-sm">
    {% if page_obj.has_previous %}
        <li><a href="./?page={{ page_obj.previous_page_number }}">&larr;</a>
    {% else %}
        <li class="disabled"><a>&larr;</a>
    {% endif %}

    {% for num in page_obj.page_range %}
       <li {% if num = page_obj.number %}class="active"{% endif %}>
       {% if not num %}<li class="disabled"><a>...</a>
       {% else %}
        {% if num = page_obj.number %}
        <a>{{ num }}</a>
        {% else %}
        <a href="./?page={{ num }}">{{ num }}</a>
        {% endif %}
       {% endif %}
       </li>
    {% endfor %}

    {% if page_obj.has_next %}
        <li><a href="./?page={{ page_obj.next_page_number }}">&rarr;</a>
    {% else %}
        <li class="disabled"><a>&rarr;</a>
    {% endif %}
    </ul>
</div>

```
