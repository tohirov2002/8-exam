from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from app_articles.models import ArticlesModel
from app_journal.models import JournalModel


@api_view(['GET'])
def all_search(request):
    keyword = request.GET.get('keyword', None)
    if keyword:
        articles = ArticlesModel.objects.filter(title_uz__icontains=keyword).values_list('id')
        journal = JournalModel.objects.filter(description_uz__icontains=keyword).values_list('id')
        response = Response(status=status.HTTP_200_OK)
        result = list(articles) + list(journal)

        a = [0] * len(result)

        for i in range(len(result)):
            a[i] = (result[i][0])

        res = ArticlesModel.objects.filter(id__in=set(a)).values()
        response.data = {
            'docs': list(res)
        }
        return response
    return Response(
        data={'message': 'Insert keyword please!'},
        status=status.HTTP_400_BAD_REQUEST
    )