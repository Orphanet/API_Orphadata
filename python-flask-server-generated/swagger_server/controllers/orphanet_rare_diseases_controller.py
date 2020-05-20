import connexion
import six

from swagger_server.models.list_hchid import ListHchid  # noqa: E501
from swagger_server.models.list_orphacode import ListOrphacode  # noqa: E501
from swagger_server.models.product1 import Product1  # noqa: E501
from swagger_server.models.product1_list import Product1List  # noqa: E501
from swagger_server.models.product3 import Product3  # noqa: E501
from swagger_server.models.product3_classification_list import Product3ClassificationList  # noqa: E501
from swagger_server.models.product4 import Product4  # noqa: E501
from swagger_server.models.product4_list import Product4List  # noqa: E501
from swagger_server.models.product6 import Product6  # noqa: E501
from swagger_server.models.product6_list import Product6List  # noqa: E501
from swagger_server.models.product9_ages import Product9Ages  # noqa: E501
from swagger_server.models.product9_ages_list import Product9AgesList  # noqa: E501
from swagger_server.models.product9_prev import Product9Prev  # noqa: E501
from swagger_server.models.product9_prev_list import Product9PrevList  # noqa: E501
from swagger_server import util


def associatedgene_all_orphacode():  # noqa: E501
    """Get all rare diseases associated to at least one gene.

    The result is a collection of clinical entities (ORPHAcode, preferred term, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, group and type) and their genes associations. For each gene, symbol, synonyms, name, typology, chromosomal location and cross-mappings with other international genetic databases are also available. # noqa: E501


    :rtype: Product6List
    """
    return 'do some magic!'


def associatedgene_list_orphacode():  # noqa: E501
    """Get the list of ORPHAcodes associated to at least one gene.

    The result is a collection of ORPHAcodes associated to at least one gene. # noqa: E501


    :rtype: ListOrphacode
    """
    return 'do some magic!'


def associatedgene_orphacode(orphacode):  # noqa: E501
    """Get associated genes and genes information of a clinical entity searching by its ORPHAcode.

    The result is a set of data includes ORPhacode, preferred term, expertlink, group and type of the selected clinical entity, relationship between genes and the searched disease and symbol, synonyms, name, typology, chromosomal location and cross-mappings with other international genetic databases of selected genes. # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int

    :rtype: Product6
    """
    return 'do some magic!'


def epidemiology_all_orphacode(language):  # noqa: E501
    """Get all clinical entities with their epidemiological dataset in the selected language.

    The result is a collection of clinical entities (ORPhacode, preferred term, expertlink) and associated epidemiological data characterized as point prevalence, birth prevalence, lifelong prevalence and incidence, or the number of cases/families reported together with their respective intervals per geographical area (country, continent) and translated in the selected language. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product9PrevList
    """
    return 'do some magic!'


def epidemiology_by_orphacode(orphacode, language):  # noqa: E501
    """Get epideliological informations of a clinical entity searching by its ORPHAcode in the selected language.

    The result is a set of data including ORPHAcode, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, preferred term, the group and type, and the associated point prevalence, birth prevalence, lifelong prevalence and incidence, or the number of cases/families reported together with their respective intervals per geographical area (country, continent) when exist. # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product9Prev
    """
    return 'do some magic!'


def epidemiology_list_orphacode(language):  # noqa: E501
    """Get the list of ORPHAcodes associated to at least one epidemiological data.

    The result is a collection of ORPHAcodes in the selected language. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    return 'do some magic!'


def hierarchy_all_orphacode(hchid):  # noqa: E501
    """Get the organisation of all ORPHAcodes available for a selected classification.

    The result is a collection of ORPHAcodes organised as children and parents in the selected classification. # noqa: E501

    :param hchid: The hierarchy ID (hchID) is a specific identifier attributed to an Orphanet classification.
    :type hchid: int

    :rtype: Product3ClassificationList
    """
    return 'do some magic!'


def hierarchy_by_orphacode(orphacode):  # noqa: E501
    """Hierarchical classification of clinical entities by ORPHAcode in all classifications

    Query one clinical entity by its ORPHAcode and gives the list of occurences in Orphanet&#x27;s classifications with parents and childs clinical entity ORPHAcode number, the list of its children and parents. # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int

    :rtype: Product3ClassificationList
    """
    return 'do some magic!'


def hierarchy_id_by_orphacode(orphacode, hchid):  # noqa: E501
    """Hierarchical classification of clinical entities by ORPHAcode in selected classification

    Query one clinical entity by its ORPHAcode and gives the list of parents and childs clinical entity in the selected Orphanet&#x27;s classification # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int
    :param hchid: The hierarchy ID (hchID) is a specific identifier attributed to an Orphanet classification.
    :type hchid: int

    :rtype: Product3
    """
    return 'do some magic!'


def hierarchy_list_hchid():  # noqa: E501
    """Get the list of identifiers of all Orphanet Rare Diseases Classifications available.

    The result is a collection of the unique identifier of each rare diseases classification available. # noqa: E501


    :rtype: ListHchid
    """
    return 'do some magic!'


def hierarchy_list_orphacode(hchid):  # noqa: E501
    """Get the list of ORPHAcodes available for a selected classification.

    The result is a collection of ORPHAcodes present in the selected classification. # noqa: E501

    :param hchid: The hierarchy ID (hchID) is a specific identifier attributed to an Orphanet classification.
    :type hchid: int

    :rtype: ListOrphacode
    """
    return 'do some magic!'


def natural_history_all_orphacode(language):  # noqa: E501
    """Get all clinical entities with their natural history data in the selected language.

    The result is a collection of clinical entities (ORPhacode, preferred term, expertlink) and associated natural history data characterized by informations on inheritance, interval average age of onset and interval average age of death. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product9AgesList
    """
    return 'do some magic!'


def natural_history_by_orphacode(orphacode, language):  # noqa: E501
    """Get natural history informations of a clinical entity searching by its ORPHAcode in the selected language.

    The result is a set of data including ORPHAcode, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, preferred term, the group and type, and the associated inheritance, age of onset and age of death when exist. # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product9Ages
    """
    return 'do some magic!'


def natural_history_list_orphacode(language):  # noqa: E501
    """Get the list of ORPHAcodes associated to at least one natural history data.

    The result is a collection of ORPHAcodes in the selected language. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    return 'do some magic!'


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


def product1_all_orphacode(language):  # noqa: E501
    """Get all clinical entities informations and their cross-referencing in the selected language.

    The result is a collection of rare diseases informations including ORPHAcode, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, preferred term, synonyms, definition, the group and type, and the characterisation of the alignment between the clinical entity and ICD-10, UMLS, MesH, MedDra, and OMIM systems in the selected language # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product1List
    """
    return 'do some magic!'


def product1_by_orphacode(orphacode, language):  # noqa: E501
    """Get informations and cross-referencing of a clinical entity searching by its ORPHAcode in the selected language.

    The result is a set of data including ORPHAcode, the stable URL pointing to the specific page of the clinical entity on the Orphanet website, preferred term, synonyms, definition, the group and type, and the characterisation of the alignment between the clinical entity and ICD-10, UMLS, MesH, MedDra, and OMIM systems in the selected language. # noqa: E501

    :param orphacode: a unique and time-stable numerical identifier attributed randomly by the database upon creation of the entity.
    :type orphacode: int
    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: Product1
    """
    return 'do some magic!'


def product1_list_orphacode(language):  # noqa: E501
    """Get the list of ORPHAcodes available in the selected language.

    The result is a collection of ORPHAcodes in the selected language. # noqa: E501

    :param language: Specify the language in the list supported by Orphanet (CS, DE, EN, ES, FR, IT, NL, PL, PT)
    :type language: str

    :rtype: ListOrphacode
    """
    return 'do some magic!'
