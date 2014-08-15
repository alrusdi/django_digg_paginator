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

and addig a template like in origial django snippet info
