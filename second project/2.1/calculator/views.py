from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}


def home_view(request):
    template_name = 'calculator/home.html'
    context = {
        'dishes': DATA.keys(),
    }
    return render(request, template_name, context)


def index_view(request, dish):
    template_name = 'calculator/index.html'
    servings = int(request.GET.get('servings', 1))
    result = dict()
    for item, count in DATA[dish].items():
        result[item] = count * servings
    context = {
        'recipe': result,
    }
    return render(request, template_name, context)
