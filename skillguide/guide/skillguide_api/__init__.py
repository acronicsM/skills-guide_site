from .index_api import index, EXCEPT_RESPONSE as INDEX_RESPONSE
from .vacancies_api import vacancies, vacancy, VACANCIES_RESPONSE, VACANCY_RESPONSE
from .skills_api import skills, SKILLS_RESPONSE
from .querys_api import querys, querysPOST, querysDELETE, QUERYS_RESPONSE

INDEX_MODEL = {'func': index,
               'response': INDEX_RESPONSE,
               }

VACANCIES_MODEL = {'func': vacancies,
                   'response': VACANCIES_RESPONSE,
                   }

VACANCY_MODEL = {'func': vacancy,
                 'response': VACANCY_RESPONSE,
                 }

SKILLS_MODEL = {'func': skills,
                'response': SKILLS_RESPONSE,
                }

QUERYS_MODEL = {'func': querysPOST,
                'response': QUERYS_RESPONSE,
                }

QUERYS_POST_MODEL = {'func': querysPOST,
                     'response': QUERYS_RESPONSE,
                     }

QUERYS_DELETE_MODEL = {'func': querysDELETE,
                       'response': QUERYS_RESPONSE,
                       }
