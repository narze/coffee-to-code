const coffee2code = (str) => {
    let setUnicode = new Set();
    let char = '';
    let array = [];
    for(let i = 0; i < str.length; i++){
      setUnicode.add(str.codePointAt(i))
    }
    array = [...setUnicode];
    array = array.filter(x => x % 2)
    for(let i = 100; i <= 101; i++){
      array[i%98] = i;
    }
    for(let i = 0; i < array.length; i++){
      char += String.fromCharCode(array[i])
    }
    console.log(char)
  }
  
  coffee2code('Coffee')