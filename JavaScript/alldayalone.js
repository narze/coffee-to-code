class Programmer {
    isReady = false;
    
    drink(input) {
        if (input === "Coffee") {
            this.isReady = true;
        }
    }

    writeCode() {
        if (this.isReady) {
            console.log("Code");
        }
    }
     
    
}

const pavel = new Programmer();

pavel.drink("Coffee");
pavel.writeCode();
