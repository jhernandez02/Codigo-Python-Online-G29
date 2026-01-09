import { useState, useEffect } from "react";
import { listarFavoritoService, eliminarFavoritoService } from "../services/FavoritoService";
import Spinner from "react-bootstrap/esm/Spinner";
import Card from 'react-bootstrap/Card';
import Swal from "sweetalert2";

function FavoritoPage(){
    const [lista, setLista] = useState([]);
    const [cargando, setCargando] = useState(true);

    const listarFavoritos = async () => {
        const res = await listarFavoritoService();
        setLista(res.data);
        setCargando(false);
    };

    const eliminarFavorito = async (id) => {
        setCargando(true)
        await eliminarFavoritoService(id);
        listarFavoritos();
        Swal.fire({
            icon: "success",
            title: "¡Eliminado!",
            text: "La serie ha sido elminada de tus favoritos",
            confirmButtonColor: "#3085d6",
            confirmButtonText: "Aceptar"
        });
    };

    const confirmarEliminarFavorito = (favorito) => {
        Swal.fire({
            title:  `¿Está seguro de eliminar "${favorito.serie_nombre}"?`,
            text: "¡No podrás revertir esta acción!",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: "¡Sí, eliminar!",
            cancelButtonText: "Cancelar"
        }).then((result) => {
            if (result.isConfirmed) {
                eliminarFavorito(favorito.id);
            }
        });
    };

    useEffect(()=>{
        listarFavoritos();
    }, []);

    return (
        <section className="container py-5">
            <h2>Favoritos</h2>
            {cargando ? (
                <p className="text-center">
                    <Spinner animation="border" variant="primary" />
                    <div>Cargando...</div>
                </p>
            ):(
                <div className="mt-4 row">
                {lista.map(favorito => (
                    <div key={favorito.id} className="col-md-3">
                        <Card className="mb-4 p-0">
                            <Card.Img variant="top" src="https://placehold.co/300x200" />
                            <Card.Body>
                                <Card.Title>{favorito.serie_nombre}</Card.Title>
                                <p>{favorito.categoria_nombre}</p>
                                <button onClick={()=>confirmarEliminarFavorito(favorito)} className="btn btn-danger w-100">
                                    <i className="bi bi-trash"></i> Eliminar
                                </button>
                            </Card.Body>
                        </Card>
                    </div>
                ))}
                </div>
            )}
        </section>
    );
}

export default FavoritoPage;