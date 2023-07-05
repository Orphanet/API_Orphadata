from flask import Blueprint

from ..controllers.rd_references import query_references_by_multiple_fields


bp = Blueprint('mappor', __name__, url_prefix='/mappor')


@bp.route('/', methods=('GET', 'POST'))
def get_references_by_multiple_fields():
    return query_references_by_multiple_fields()
