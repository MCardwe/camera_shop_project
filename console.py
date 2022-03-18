import pdb

from models.camera import Camera
from models.make import Make

import repositories.camera_repository as camera_repository
import repositories.make_repository as make_repository

# make_repository.delete_all()

# make1 = Make("Canon")
# make2 = Make("Nikon")

# make_repository.save(make1)
# make_repository.save(make2)

makes = make_repository.select_all()
for make in makes:
    print(make.__dict__)

selected_make = make_repository.select(3)
print(selected_make)

make_sony = Make("Sony", 4)

make_repository.update(make_sony)

makes = make_repository.select_all()
for make in makes:
    print(make.__dict__)

make_repository.delete(4)

makes = make_repository.select_all()
for make in makes:
    print(make.__dict__)

pdb.set_trace()