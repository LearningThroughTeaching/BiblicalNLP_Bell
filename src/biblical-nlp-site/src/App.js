import React from 'react';
import johnData from '/src/data/niv_text/1_john_niv.json';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          {johnData.text}
        </p>
      </header>
    </div>
  );
}

export default App;
