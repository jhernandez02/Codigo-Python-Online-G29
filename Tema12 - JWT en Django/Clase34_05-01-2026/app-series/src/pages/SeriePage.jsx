import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { mostrarSerieService } from "../services/SerieService";
import Spinner from "react-bootstrap/esm/Spinner";

const initData = {
    id: 0,
    categoria_nombre: "",
    nombre: "",
    fecha_lanzamiento: "",
    puntaje: 0,
    categoria: 0
};

function SeriePage(){
    const { id } = useParams();
    const [serie, setSerie] = useState(initData);
    const [cargando, setCargando] = useState(true);

    const mostrarSerie = async () => {
        const res = await mostrarSerieService(id);
        const datos = res.data;
        setSerie({
            id: datos.id,
            categoria_nombre: datos.categoria_nombre,
            nombre: datos.nombre,
            fecha_lanzamiento: datos.fecha_lanzamiento,
            puntaje: datos.puntaje,
            categoria: datos.categoria
        });
        setCargando(false);
    };

    useEffect(()=>{
        mostrarSerie();
    }, id);

    return (
        <section className="container py-5">
            {cargando ? (
                <p className="text-center">
                    <Spinner animation="border" variant="primary" />
                    <div>Cargando...</div>
                </p>
            ):(
                <div className="row">
                    <div className="col-md-6">
                        <img src="https://placehold.co/600x400" className="w-100" alt="imagen" />
                    </div>
                    <div className="col-md-6">
                        <h2>{serie.nombre}</h2>
                        <p><strong>Fecha Lanzamiento:</strong> {serie.fecha_lanzamiento}</p>
                        <p><strong>Rating:</strong> {serie.puntaje}</p>
                        <p><strong>Categoría:</strong> {serie.categoria_nombre}</p>
                    </div>
                </div>
            )}
        </section>
    );
}

export default SeriePage;