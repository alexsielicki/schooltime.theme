## Script (Python) "getLatestCalendarX"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=return the latest published Season as a brain
##

from DateTime.DateTime import DateTime
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.browser.navtree import getNavigationRoot

catalog = getToolByName(context, 'portal_catalog')
limit = 1
state = 'published'
path = getNavigationRoot(context)
brain = None
brains = catalog(portal_type='CalendarXFolder',
               review_state=state,
               effective={'query': DateTime(), 'range': 'max'},
               path=path,
               sort_on='effective',
               sort_order='descending',
               sort_limit=limit)[:limit]
if brains:
    brain = brains[0]
    
return brain