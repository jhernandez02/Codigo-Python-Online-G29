import React, { useState } from "react";

const AppContext = React.createContext();
const { Provider } = AppContext;

function AppProvider({children}){
    let [usuario, setUsuario] = useState(localStorage.usuario || null);
    let [token, setToken] = useState(localStorage.token || null);

    function login(usuario, token){
        localStorage.setItem('usuario', usuario);
        localStorage.setItem('token', token);
        setUsuario(usuario);
        setToken(token);
    }

    function logout(){
        localStorage.removeItem('usuario');
        localStorage.removeItem('token');
        setUsuario(null);
        setToken(null);
    }

    return(
        <Provider value={{token, usuario, login, logout}}>
            {children}
        </Provider>
    );

}

export { AppProvider, AppContext}