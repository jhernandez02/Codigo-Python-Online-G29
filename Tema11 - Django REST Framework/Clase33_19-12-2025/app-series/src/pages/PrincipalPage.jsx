import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { listarSerieService } from "../services/SerieService";
import Spinner from 'react-bootstrap/Spinner';
import Card from 'react-bootstrap/Card';

function PrincipalPage(){
    const [lista, setLista] = useState([]);
    const [cargando, setCargando] = useState(true);
    
    const listarSeries = async () => {
        const res = await listarSerieService();
        console.log(res.data);
        setLista(res.data);
        setCargando(false);
    };

    useEffect(()=>{
        listarSeries();
    }, []);

    return (
        <section className="container py-5">
            <h2>Lista Series</h2>
            {cargando ? (
                <p className="text-center">
                    <Spinner animation="border" variant="primary" />
                    <div>Cargando...</div>
                </p>
            ):(
                <div className="mt-4 row">
                {lista.map(serie => (
                    <div key={serie.id} className="col-md-3">
                        <Card className="mb-4 p-0">
                            <Card.Img variant="top" src="https://placehold.co/300x200" />
                            <Card.Body>
                                <Card.Title>{serie.nombre}</Card.Title>
                                <Link to={`/serie/${serie.id}`} className="btn btn-primary w-100">Ver detalle</Link>
                            </Card.Body>
                        </Card>
                    </div>
                ))}
                </div>
            )}
        </section>
    );
}

export default PrincipalPage;