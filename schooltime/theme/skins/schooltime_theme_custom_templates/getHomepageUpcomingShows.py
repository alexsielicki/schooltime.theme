limit = 2
parentIds = []
upcomingShows = []
performances = context.queryCatalog({'portal_type':'Performance', 'sort_on':'start', 'start': {'query': DateTime(), 'range': 'min'}})
for performance in performances:
    performanceObject = performance.getObject()
    performanceParentUID = performanceObject.aq_inner.aq_parent.UID()
    if performanceParentUID not in parentIds:
        parentIds.append(performanceParentUID)
        upcomingShows.append(performanceObject)
    if len(upcomingShows) >= limit:
        break
return upcomingShows
