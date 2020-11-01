from app.models.sets import *

Set.query.delete()

set = Set(set_num='9943-1', name='Axles and Extenders', year=1998, theme_id=1, num_parts=54, image_url='')
db.session.add(set)
db.session.commit()

sets = Set.query.all()
print(sets)

# ['9943-1', 'Axles and Extenders', '1998', '1', '54']