import * as React from 'react';
import ReactDOM from 'react-dom';
import { StyledEngineProvider } from '@mui/material/styles';
import App from './App';
import './App.css'


ReactDOM.render(
  
  <App>  
    <StyledEngineProvider injectFirst>
    </StyledEngineProvider>,
  </App>
  ,
  document.querySelector("#root")
);

