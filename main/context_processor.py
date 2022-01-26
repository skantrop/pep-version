from .models import Company


def get_categories(request):
    companies = Company.objects.filter(parent__isnull=True)
    return {'companies': companies}
