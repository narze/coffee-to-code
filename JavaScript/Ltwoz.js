const coffeeMachine = {
  coffee: "coffee",
  brew() {
    console.log(`Brewing ${this.coffee}...`);
    setTimeout(() => {
      this.coffee = "code";
      console.log(this.coffee);
    }, 2000);
  },
};

coffeeMachine.brew();
