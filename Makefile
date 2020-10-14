all: cleminbox
cleminbox:
	cp src/cleminlang.py bin
	cp src/clemincomp.py bin
	cp src/cleminbox.py bin
	python3 bin/clemincomp.py examples/example1.clmnlng bin/example1.bin
	python3 bin/clemincomp.py examples/example2.clmnlng bin/example2.bin
	rm -r bin/__pycache__
clean:
	rm -r bin
	mkdir bin
