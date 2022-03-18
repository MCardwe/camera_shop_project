import pdb

from models.camera import Camera
from models.make import Make

import repositories.camera_repository as camera_repository
import repositories.make_repository as make_repository


camera = camera_repository.select(14)
print(camera)

# camera_repository.delete_all()
# make_repository.delete_all()

# make_canon = Make("Canon")
# make_nikon = Make("Nikon")
# make_sony = Make("Sony")
# make_fuji = Make("Fuji")
# make_panasonic = Make("Panasonic")
# make_olympus = Make("Olympus")

# make_repository.save(make_canon)
# make_repository.save(make_nikon)
# make_repository.save(make_sony)
# make_repository.save(make_fuji)
# make_repository.save(make_panasonic)
# make_repository.save(make_olympus)

# camera_compact_dslr = Camera("250d", make_canon, "Compact DSLR", "Lightweight APS-C DSLR mid-range camera", 5, 250, 500)
# camera_mirroless = Camera("a7", make_sony, "Mirrorless Camera", "Full frame mirrorless high end camera", 3, 600, 1200)
# camera_compact_mirroless = Camera("M50", make_canon, "Compact Mirroless", "Lightweight APS-C mirrorless mid-range camera", 4, 300, 600)
# camera_dslr = Camera("5D MKIV", make_canon, "DSLR", "Full frame DSLR high end camera", 2, 1000, 2000)

# camera_repository.save(camera_dslr)
# camera_repository.save(camera_compact_dslr)
# camera_repository.save(camera_mirroless)
# camera_repository.save(camera_compact_mirroless)

# camera = camera_repository.select(2)
# print(camera)

# camera_repository.update(camera3)

# camera_repository.delete(10)

# cameras = camera_repository.select_all()
# for camera in cameras:
#     print(camera.__dict__)


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

# make_repository.delete(11)

pdb.set_trace()