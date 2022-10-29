pm.test("Convert Coffee to Code", function () {
    var input = "Coffee";
    console.log(input);
    console.log("Drink coffee up ! :D");
    const regex = /Coffee/ig;
    //var output = input.replaceAll('ffe','d');
    var output = input.replaceAll(regex,'Code');
    console.log(output);
    pm.expect(output).to.eql("Code");
});