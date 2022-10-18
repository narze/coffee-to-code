import React, { useState } from "react";

export default function App() {
  let [changeImg, setChangeImg] = useState(true);
  const [buttonText, setButtonText] = useState('Code');

  const handleClick = () => {
    setButtonText(!buttonText)
  } 

  const handleChange = () => {
    return setChangeImg(!changeImg);
  };

  return (
    <div>
      <div className="container" style={{margin: 'auto', top:'125px', left: '450px', position:'absolute', alignItems:'center', border: '#FFF00'}}>
      {changeImg ? <img src='https://images.unsplash.com/photo-1541167760496-1628856ab772?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1037&q=80' alt="coffee" width={450} height={250} /> : <img src='https://images.unsplash.com/photo-1516259762381-22954d7d3ad2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=889&q=80' alt="code" width={450} height={250} />}
      </div>
      <div className="button" style={{textAlign: 'center'}}>
      <button style={{backgroundColor: '#98A8F8', color: 'white', border: 'none', borderRadius: '5px', padding: '10px', position: 'absolute', left: '650px', top: '380px', cursor: 'pointer'}} onClick={() => {handleChange(); handleClick()}}>{buttonText ? 'Code' : 'Coffee'}</button>
      </div>
    </div>
  );
}