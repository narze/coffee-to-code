coffee: coffee.o
	ld -macosx_version_min 11.0.0 -o coffee coffee.o -lSystem -syslibroot `xcrun -sdk macosx --show-sdk-path` -e _start -arch arm64

coffee.o: coffee.s
	as -o coffee.o coffee.s

clean:
	rm coffee.o