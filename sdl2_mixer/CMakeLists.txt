#
# Copyright © 2020 DolceSDK contributors
#
# This file is part of DolceSDK
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

cmake_minimum_required(VERSION 3.0)

set(CMAKE_TOOLCHAIN_FILE "$ENV{DOLCESDK}/share/dolce.toolchain.cmake" CACHE PATH "DolceSDK toolchain file")

project(sdl2_mixer LANGUAGES C)

add_compile_options(
  -O3 -Wall
)

add_compile_definitions(
  MUSIC_FLAC
  MUSIC_MOD_MIKMOD
  MUSIC_MP3_MPG123
  MUSIC_OGG
  MUSIC_WAV
)

include_directories("${CMAKE_INSTALL_PREFIX}/include/SDL2")

add_library(SDL2_mixer STATIC
  effect_position.c
  effect_stereoreverse.c
  effects_internal.c
  load_aiff.c
  load_voc.c
  mixer.c
  music.c
  music_cmd.c
  music_flac.c
  music_fluidsynth.c
  music_mad.c
  music_mikmod.c
  music_modplug.c
  music_mpg123.c
  music_nativemidi.c
  music_ogg.c
  music_opus.c
  music_timidity.c
  music_wav.c
)

install(TARGETS SDL2_mixer DESTINATION lib)
install(FILES SDL_mixer.h DESTINATION include/SDL2)
