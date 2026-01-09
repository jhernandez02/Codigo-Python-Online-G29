import { useState, useEffect, useContext } from "react";
import { useParams } from "react-router-dom";
import { AppContext } from "../contexts/AppContext";
import { mostrarSerieService } from "../services/SerieService";
import { guardarFavoritoService } from "../services/FavoritoService";
import Spinner from "react-bootstrap/esm/Spinner";
import Swal from "sweetalert2";

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
    const { usuario } = useContext(AppContext);
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

    const agregarSerie = async (serieId) => {
        try {
            const postData = {serie: serieId};
            if(usuario){
                await guardarFavoritoService(postData);
                Swal.fire({
                    icon: "success",
                    title: "¡Serie agregada!",
                    text: "La serie se agregó a tus favoritos",
                    confirmButtonColor: "#3085d6",
                    confirmButtonText: "Aceptar"
                });
            }else{
                Swal.fire({
                    icon: "error",
                    title: "¡Debes iniciar sesión!",
                    text: "Para guardar como favorito, debes iniciar sesión primero",
                    confirmButtonColor: "#3085d6",
                    confirmButtonText: "Aceptar"
                });
            } 
        } catch (error) {
            console.log(error);
            const mensaje = error.response.data.non_field_errors[0] || "¡Ocurrió un error!";
            Swal.fire({
                icon: "error",
                title: 'Oops...',
                text: mensaje,
                confirmButtonColor: "#3085d6",
                confirmButtonText: "Aceptar"
            });
        }
    };

    useEffect(()=>{
        mostrarSerie();
    }, id);

    const formatearFecha = (fechaISO) => {
        const meses = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
        const [anio, mes, dia] = fechaISO.split('-');
        return `${dia} de ${meses[mes-1]} de ${anio}`;
    }

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
                        <p><strong>Fecha Lanzamiento:</strong> {formatearFecha(serie.fecha_lanzamiento)}</p>
                        <p><strong>Rating:</strong> {serie.puntaje}</p>
                        <p><strong>Categoría:</strong> {serie.categoria_nombre}</p>
                        <button onClick={()=>agregarSerie(serie.id)} className="btn btn-success mt-2 fs-4 w-100">
                            <i className="bi bi-plus-circle"></i> Agregar a favoritos
                        </button>
                    </div>
                </div>
            )}
        </section>
    );
}

export default SeriePage;