ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  # Unix
  pwd := $$(pwd)
  translate = $1
else
  # Windows mit MSys2/Cygwin
  pwd := $$(cygpath -m "$$(pwd)")
  translate = $(shell echo '$1' | sed 's/:/;/g')
endif

all: build/main.pdf

# hier Python-Skripte:
build/linregplot.pdf: linregplot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python linregplot.py

build/plotw1.pdf: plotw1.py matplotlibrc b1.txt header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plotw1.py

build/plotw2.pdf: plotw2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plotw2.py

<<<<<<< HEAD
build/plotd_1.pdf: plotd_1.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plotd_1.py

build/plotd_2.pdf: plotd_2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plotd_2.py

build/plote.pdf: plote.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plote.py

build/plotvph.pdf: plotvph.py matplotlibrc c.txt header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plotvph.py

build/main.pdf: build/linregplot.pdf lit.bib content/ main.tex build/plotd_1.pdf build/plotd_2.pdf build/plote.pdf build/plotw1.pdf build/plotvph.pdf build/plotw2.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS="$(call translate,build:)" \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
