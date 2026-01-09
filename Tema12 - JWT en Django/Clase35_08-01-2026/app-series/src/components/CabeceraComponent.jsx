import { useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import { AppContext } from "../contexts/AppContext";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

function CabeceraComponent(){
    const navigate = useNavigate();
    const { usuario, logout } = useContext(AppContext);

    const handleLogout = () => {
        logout();
        navigate('/');
    }
    return (
        <Navbar expand="lg" className="bg-body-tertiary">
            <Container>
                <Link to="/principal" className="navbar-brand">SerieApp</Link>
                <Navbar.Toggle />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <li className="nav-item">
                        {usuario && (
                            <Link to="/favoritos" className="nav-link">Favoritos</Link>
                        )}
                        </li>
                    </Nav>
                    <Navbar.Text>  
                    {usuario ? (
                        <div className="me-3">
                            <i className="bi bi-person-circle"></i> {usuario} | <a onClick={handleLogout} href="#" className="text-secondary" >Salir</a>
                        </div>
                    ):(
                        <div className="me-3">
                             <Link to="/" className="nav-link">Login</Link>
                        </div>
                    )}
                    </Navbar.Text>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default CabeceraComponent;