import pdb

from models.camera import Camera
from models.make import Make

import repositories.camera_repository as camera_repository
import repositories.make_repository as make_repository

# make_repository.delete_all()

make1 = Make("Canon")
make2 = Make("Nikon")
make3 = Make("Sony")

# make_repository.save(make1)
# make_repository.save(make2)
# make_repository.save(make3)

camera1 = Camera("250d", make1, "Compact DSLR", "Lightweight APS-C mid-range camera", 5, 250, 500)
camera2 = Camera("a7", make3, "Mirrorless Camera", "Full frame high end camera", 3, 600, 1200)

# camera_repository.save(camera1)
# camera_repository.save(camera2)

cameras = camera_repository.select_all()
for camera in cameras:
    print(camera.__dict__)

# makes = make_repository.select_all()
# for make in makes:
#     print(make.__dict__)

# selected_make = make_repository.select(3)
# print(selected_make)

# make_sony = Make("test", 4)

# make_repository.update(make_sony)

# makes = make_repository.select_all()
# for make in makes:
#     print(make.__dict__)

# make_repository.delete(4)

pdb.set_trace()