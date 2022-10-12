//AUTHOR:Manaswini123456
//Language:JS , LIBRARY:ReactJS
//Github link:https://github.com/Manaswini123456

//App.jsx file
import logo from './logo.svg';
import './App.css';
import {useState} from 'react';


function App() {
  const [buttonText,setButtonText] = useState('Coffee');

  function handleClick(){
    if (buttonText==='Coffee'){
      setButtonText('Code');
    } else{
      setButtonText('Coffee')
    }
    console.log(buttonText);
    
  }
  return (
    <div className="App">
      <header className='App-header'>
        <h1>REACT JS CHANGING BUTTON</h1>
        <h2>Try Yourself and Enjoy!</h2>
      <img src={logo} className="App-logo" alt='text'></img>
      <button onClick={handleClick} className="doublechange">{buttonText}</button>
      
      </header>
    </div>
  );
}

export default App;
