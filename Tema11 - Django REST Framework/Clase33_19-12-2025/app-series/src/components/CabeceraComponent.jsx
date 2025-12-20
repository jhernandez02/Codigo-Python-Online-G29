import { Link } from "react-router-dom";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

function CabeceraComponent(){
    return (
        <Navbar expand="lg" className="bg-body-tertiary">
            <Container>
                <Link to="/" className="navbar-brand">SerieApp</Link>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <li className="nav-item">
                            <Link to="/principal" className="nav-link">Principal</Link>
                        </li>
                        <li className="nav-item">
                            <Link to="/favoritos" className="nav-link">Favoritos</Link>
                        </li>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default CabeceraComponent;