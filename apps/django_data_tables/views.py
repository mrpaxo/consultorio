from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class DataTablesPagination(LimitOffsetPagination):
    """
    Paginador compatible con datatables v1.10
    ver documentacion: https://www.datatables.net/manual/server-side
    """
    limit_query_param = 'length'
    offset_query_param = 'start'

    def get_paginated_response(self, data, recordsTotal=None):
        print(data)
        dic = dict([
            ('draw', self.request.query_params.get('draw', 0)),
            ('recordsTotal', recordsTotal or self.count),
            ('recordsFiltered', self.count),
            ('data', data)
        ])
        return Response(dic)


class DataTablesMixin(object):
    """
    Agrega funcionalidad para compatibilidad con data tables.
    """
    total_records = -1

    def get_total_records(self):
        if not self.total_records >= 0:
            raise Exception('Debe proporcionar el total de registros antes de filtrar, requerido por DataTables.')
        return self.total_records

    def get_paginated_response(self, data):
        """
        Return a paginated style `Response` object for the given output data.
        Agregamos el total de registros para poder pasarle al DataTables.
        """
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data, self.get_total_records())
