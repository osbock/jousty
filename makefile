
all:
	dasm  joust.asm -f3
	python3 segmentize.py a.out
