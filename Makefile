BIN=bin
NAME=curwthr
FILE=src/main.py
CLEAN=build/ curwthr.spec src/__pycache__ bin/

compile:
	mkdir -p $(BIN)
	pyinstaller $(FILE) --onefile --distpath $(BIN) --name $(NAME)
clean:
	rm -rf $(CLEAN)
install: $(BIN)/$(NAME)
	sudo cp $(BIN)/$(NAME) /bin
uninstall: /bin/$(NAME)
	sudo rm -f /bin/$(NAME)