import os

os.system("mkdir -p build && cd build && cmake .. -DPLATFORM=Embedded -DGRAPHICS=GRAPHICS_API_OPENGL_11 && make -j")