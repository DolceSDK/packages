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

project(sdl_mixer LANGUAGES C)

add_compile_options(
  -O3 -Wall
)

add_compile_definitions(
  FLAC_MUSIC
  MOD_MUSIC
  USE_TIMIDITY_MIDI
  MODPLUG_MUSIC
  OGG_MUSIC
  WAV_MUSIC
)

include_directories(
  "${CMAKE_INSTALL_PREFIX}/include/SDL"
  "${CMAKE_INSTALL_PREFIX}/include/libmodplug"
)

add_library(SDL_mixer STATIC
  dynamic_flac.c
  dynamic_fluidsynth.c
  dynamic_mod.c
  dynamic_mp3.c
  dynamic_ogg.c
  effect_position.c
  effect_stereoreverse.c
  effects_internal.c
  fluidsynth.c
  load_aiff.c
  load_flac.c
  load_ogg.c
  load_voc.c
  mixer.c
  music.c
  music_cmd.c
  music_flac.c
  music_mad.c
  music_mod.c
  music_modplug.c
  music_ogg.c
  playmus.c
  playwave.c
  wavestream.c
  timidity/common.c
  timidity/instrum.c
  timidity/mix.c
  timidity/output.c
  timidity/playmidi.c
  timidity/readmidi.c
  timidity/resample.c
  timidity/tables.c
  timidity/timidity.c
)

install(TARGETS SDL_mixer DESTINATION lib)
install(FILES SDL_mixer.h DESTINATION include/SDL)
