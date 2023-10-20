//AUTHOR:Kalamell
//Language:JS , LIBRARY:ReactJS
//Github link:https://github.com/kalamell



import {useState} from 'react';


function App() {
  const [text, setText] = useState('Coffee');

  function handleClick(){
    if (text === 'Coffee'){
      setText('Code');
    } else{
      setText('Coffee')
    }
    
  }
  return (
    <div className="App">
      <header>
        <h1>REACT JS CHANGING BUTTON</h1>
        <h2>{text}</h2>
        <button onClick={handleClick} className="doublechange">Click to change</button>
      
      </header>
    </div>
  );
}

export default App;
