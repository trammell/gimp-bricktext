usage:
	@echo "usage: make [clean|install]"

clean:
	rm ~/.gimp-2.6/plug-ins/bricktext.py

install:
	ln -sf $(pwd)/bricktext.py ~/.gimp-2.6/plug-ins/

