#!/usr/bin/env python3

print('''\
language: cpp
os: linux
dist: bionic
addons:
  apt:
    sources:
      - sourceline: 'deb https://apt.kitware.com/ubuntu/ bionic main'
        key_url: 'https://apt.kitware.com/keys/kitware-archive-latest.asc'
    packages:
      - autoconf
      - automake
      - bsdtar
      - cmake
      - fakeroot
      - file
      - libtool-bin
      - pkg-config
      - texinfo
      - xutils-dev
env:
  - DOLCESDK="$TRAVIS_BUILD_DIR/dolcesdk"
    PATH="$DOLCESDK/bin:$PATH"
before_script:
  - sudo rm -rf /usr/local/cmake-* # workaround to remove default cmake that has priority in PATH''')

# since we don't have dep tracking, we need to build in a specific order
manifest=(
	'zlib',
	'bzip2',
	'libzip',
	'libpng',
	'libexif',
	'libjpeg-turbo',
	'jansson',
	'yaml-cpp',
	'freetype',
	'harfbuzz',
	'fftw',
	'libvita2d',
	'libvita2d_sys',
	'libmad',
	'libogg',
	'libvorbis',
	'flac',
	'mpg123',
	'libtremor',
	'libmikmod',
	'libftpvita',
	'henkaku',
	'taihen',
	'onigmo',
	'sdl',
	# 'sdl_image',
	'sdl_mixer',
	# 'sdl_net',
	# 'sdl_ttf',
	# 'sdl_gfx',
	'sdl2',
	'sdl2_image',
	'sdl2_mixer',
	# 'sdl2_net',
	'sdl2_ttf',
	# 'sdl2_gfx',
	'openssl',
	'curl',
	'curlpp',
	'expat',
	'opus',
	'unrar',
	'glm',
	'libxml2',
	'speexdsp',
	'pixman',
	'taipool',
	'libmpeg2',
	'soloud',
	'quirc',
	'libsndfile',
	'xz',
	'libarchive',
	'libmodplug',
	'libconfig',
	'libsodium',
	'libmathneon',
	'vitaGL',
	'imgui',
	'libbaremetal',
	'minizip',
	'jsoncpp',
	'lame',
	'ffmpeg',
	'fnblit',
	'libtheora',
	'libvitaSAS',
	'libShellAudio',
	'psp2dbg',
	'box2d',
	'libpib',
)

print('''\
stages:
  - prepare''')

build_stage_size = 8

for i in range(0, len(manifest), build_stage_size):
	print(f'''\
  - build-stage-{i // build_stage_size}''')

print('''\
jobs:
  include:
    - stage: prepare
      workspaces:
        create:
          name: prepare
          paths: "$TRAVIS_BUILD_DIR"
      script:
        - .travis.d/prepare.sh''')

for i in range(0, len(manifest), build_stage_size):
	prev = 'prepare' if i == 0 else f'build-stage-{i // build_stage_size - 1}'
	cur = f'build-stage-{i // build_stage_size}'
	print(f'''\
    - stage: {cur}
      workspaces:
        use: {prev}
        create:
          name: {cur}
          paths: "$TRAVIS_BUILD_DIR"
      script:
        - set -e''')
	build_stage_items = manifest[i : i + build_stage_size]
	for p in build_stage_items:
		print(f'''\
        - .travis.d/build.sh "{p}"''')

print('''\
      deploy:
        provider: releases
        api_key:
          secure: Iq9pGKXRKBlW45VdSNPmHq/atWPebPmj5J6jo1aIrf/TE2mQSyp/b2qMO7Q1s0gEMi4AQRKUO5/iugWtEjK4puA/3uKtlwA6D4jlZr0VdD3i8jD8a0npLRT3ESGoSVul1N5hWov+2AfJYbIq7BgfrqpVPTTMaYx3vA9FyJkzBTieVXvblIe0qoViisjQNLQftSwDyLLgoEAZ8AIbX+WQI7jmpDumP/uIVJb7IVwMbXol2vIWXCtaivmy9F4/btYJLb5EeH6gXlpnYeGai8aRqwBnHLKMR0sGsQKAJfajOCxuqfFjtrUSypFlVNAUqsN0L16dsRN49/fI+SofHnpyKxcd/tH9MrRcoGS6hzzE5sP/dRPCONdRVRyeTi3YkJ6P8+iqoZzecOSlqAaeqfP3GO1NaZZSTt22BZzRJw3LM0HZ78e4MRvh+7+VCHX4rQnwFA2QrjfSDjV9+xErDjo/f+zgVvu5dbCknFG/taeAPy1poIQ7G3xN/emkV0HHyDchyup6Qtmlz21RpRDytRtN3ACsBGLqxYznc7o/9bMfS9swxB7jbfeOg1LQ2jym2JvKv8rai7H3F+SkNV6LOCrFq3XYr1AnEPFvbcRZDbdIj3NjilPAf45R1tYzGIxGSqbCgCwan8tFJ2jI78KevqV0CweD0wTtDmrSNFRPuCj3Eeo=
        file_glob: true
        file: deploy/*
        skip_cleanup: true
        on:
          tags: true
          repo: DolceSDK/packages''')
