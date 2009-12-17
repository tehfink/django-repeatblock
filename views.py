from django import template, http


def repeatblock_example(request):
    html = template.loader.render_to_string('repeatblock_example.html',
                                            {'title': 'example'})
    return http.HttpResponse(html)
