import connexion
import six

from swagger_server.models.list_orphacode import ListOrphacode  # noqa: E501
from swagger_server.models.product4 import Product4  # noqa: E501
from swagger_server.models.product4_list import Product4List  # noqa: E501
from swagger_server import util


def phenotype_all_orphacode(language):  # noqa: E501
    """Get all clinical entities with their associated phenotypes in the selected language.

    The result is a collection of clinical entities with their associated HPO phenotypes characterized by frequency (obligate, very frequent, frequent, occasional, very rare or excluded) and whether the annotated HPO term is a major diagnostic criterion or a pathognomonic sign of the rare disease. Source (PMID references), the date and the validation’s status of the association between the rare disease and HPO terms is also available. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product4List
    """
    return 'do some magic!'


def phenotype_by_orphacode(orphacode, language):  # noqa: E501
    """Get informations and associated HPO phenotypes of a clinical entity searching by its ORPHAcode in the selected language.

    The result is a set of data including ORPHAcode, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, preferred term, the group and type, and the associated HPO phenotypes. The annotation is characterized by frequency (obligate, very frequent, frequent, occasional, very rare or excluded) and whether the annotated HPO term is a major diagnostic criterion or a pathognomonic sign of the rare disease. Source (PMID references), the date and the validation’s status of the association between the rare disease and HPO terms is also made available. # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product4
    """
    return 'do some magic!'


def phenotype_list_orphacode(language):  # noqa: E501
    """Get list of ORPHAcodes associated to HPO phenotypes in the selected language.

    The result is a collection of ORPHAcodes in the selected language. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    return 'do some magic!'
