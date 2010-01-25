from django import template, http


def repeatblock_example(request):
    html = template.loader.render_to_string('repeatblock_example.html',
                                            {'title': 'example'})
    return http.HttpResponse(html)


def repeatblock_example_2(request):
    html = template.loader.render_to_string('repeatblock_example_2.html',
                                            {'title': 'example'})
    return http.HttpResponse(html)
