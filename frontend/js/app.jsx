import React, { Component } from "react";

import AdvancedPaginationTable from "./issues";

class App extends Component {
  render() {
    return (
      <div className="app">
        <div className="container">
          <div className="App-header">
            <h2>Welcome to Git Integration</h2>
          </div>
          <AdvancedPaginationTable />
        </div>
      </div>
    );
  }
}

export default App;
