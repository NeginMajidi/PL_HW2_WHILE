# while function
current_dir := ${CURDIR}

default: while

while: HW2.py
	echo 'python3 $(current_dir)/HW2.py' > while
	chmod u+x while

clean:
	rm -f while

install: while