all: build

build:
	mkdir bin
	cp src/cleminlang.py bin
	cp src/clemincomp.py bin
	cp src/cleminbox.py bin
	python3 bin/clemincomp.py examples/example1.clmnlng bin/example1.bin
	python3 bin/clemincomp.py examples/example2.clmnlng bin/example2.bin
	rm -r bin/__pycache__

prepare_dist:
	mkdir dist

prepare_packages: prepare_dist
	mkdir rfs
	mkdir -p rfs/usr/bin
	mkdir -p rfs/usr/share/
	mkdir -p rfs/usr/share/cleminbox/examples

generate_runtime_packages: build prepare_packages
	cp bin/cleminbox.py rfs/usr/share/cleminbox
	cp bin/cleminlang.py rfs/usr/share/cleminbox
	cp bin/example1.bin rfs/usr/share/cleminbox/examples
	cp bin/example2.bin rfs/usr/share/cleminbox/examples
	python3 tools/generate_runtime_wrappers.py rfs/usr/bin /usr/share/cleminbox
	tar -C rfs -c "." | gzip -f > dist/cleminbox-runtime-install.tar.gz

generate_sdk_packages: generate_runtime_packages
	cp bin/clemincomp.py rfs/usr/share/cleminbox
	python3 tools/generate_sdk_wrappers.py rfs/usr/bin /usr/share/cleminbox
	tar -C rfs -c "." | gzip -f > dist/cleminbox-sdk-install.tar.gz

generate_packages: build prepare_packages generate_runtime_packages generate_sdk_packages
	rm -r rfs

generate_source_archive: prepare_dist
	tar -c src examples tools README.md Makefile LICENSE | gzip -f > dist/cleminbox.tar.gz

dist: generate_source_archive generate_packages

cleanbin:
	rm -r bin

cleandist:
	rm -r dist

cleanall: cleanbin cleandist
clean: cleanall
