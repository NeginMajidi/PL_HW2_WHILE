# while function
current_dir := ${CURDIR}

default: while

arith: HW2.py
	echo 'python $(current_dir)/HW2.py' > while
	chmod u+x while

clean:
	rm -f while

install: while