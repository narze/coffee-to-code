const coffeeToCode = (input)=>{
  if (!input || input.toLowerCase() !== 'coffee') throw new Error('invalid coffee string');
  const reducer = input.split('').reduce((a,b) => {
      const i = b.toLowerCase()
      if (!a.dup[i]) { 
        a.dup[i]=1
        a.res+=`${b}`
      } else a.dup[i]++  
      return a 
    } ,{ dup: {}, res: ''})
  return reducer.res.replace('f','d').replace('F','D')
}
console.log(coffeeToCode('CoFfeE'))
