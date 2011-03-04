from pyramid.httpexceptions import HTTPFound
from pyramid.url import route_url

import uuid

from sqlalchemy.orm.exc import NoResultFound

from testqr.models import DBSession
from testqr.models import BusinessCard

def home(request):
    dbsession = DBSession()
    return {'title':'The Title', 'project':'testqr', 'uuid': uuid.uuid1()}

def create_card(request, id, session):
    session = DBSession()
    card = BusinessCard( 
        id = id,
        name = request.params['name'], 
        company = request.params['company'], 
        phone_work = request.params['phone.work'], 
        phone_mobile = request.params['phone.mobile'], 
        phone_home = request.params['phone.home'], 
        email = request.params['email'] 
        )
    session.add(card)
    return card

def view_card(request):
    id = request.matchdict['id']
    session = DBSession()

    try :
        card = session.query(BusinessCard).filter_by(id=id).one()
    except NoResultFound:  
        card = create_card(request, id, session)

    return {'card':card, 'title':'Business Card', 'url': route_url('view_card', request, id=card.id)}