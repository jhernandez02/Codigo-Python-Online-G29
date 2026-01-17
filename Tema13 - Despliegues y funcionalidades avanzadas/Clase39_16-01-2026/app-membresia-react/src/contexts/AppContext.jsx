import React, { useState } from "react";

let AppContext = React.createContext();
let { Provider, Consumer } = AppContext;

function AppProvider({children}){
    let [carrito, setCarrito] = useState([]);
    let [usuario, setUsuario] = useState(null);
    let [token, setToken] = useState(null);

    function login(usuario, token){
        localStorage.setItem('token', token);
        setUsuario(usuario);
        setToken(token);
    }

    function logout(){
        localStorage.removeItem('token');
        setUsuario(null);
        setToken(null);
    }

    return(
        <Provider value={{token, carrito, setCarrito, usuario, login, logout}}>
            {children}
        </Provider>
    );
}

export { AppProvider, AppContext }