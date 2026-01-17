import { useState, useEffect } from "react";
import { listarSuscripcionesService } from "../services/SuscripcionService";
import Spinner from "react-bootstrap/Spinner";

function HistorialPage(){
    const [historial, setHistorial] = useState([]);
    const [cargando, setCargando] = useState(true);

    const listarHistorial = async () => {
        const res = await listarSuscripcionesService();
        setHistorial(res.data);
        setCargando(false);
    }

    useEffect(()=>{
        listarHistorial();
    }, []);

    return(
        <div className="container mt-3">
            <h1>Historial</h1>
            {cargando ? (
                <p className="text-center">
                    <Spinner animation="border" variant="primary" />
                    <div>Cargando...</div>
                </p>
            ) : (
                <div className="mt-4">
                    <table className="table">
                        <thead>
                            <th>Membresía</th>
                            <th>Inicio</th>
                            <th>Fin</th>
                            <th>Precio</th>
                            <th>Boleta</th>
                            <th>Estado</th>
                        </thead>
                        <tbody>
                        {historial.map((suscripcion)=>(
                            <tr key={suscripcion.id}>
                                <td>{suscripcion.membresia_nombre}</td>
                                <td>{suscripcion.fecha_inicio}</td>
                                <td>{suscripcion.fecha_fin}</td>
                                <td>{suscripcion.precio}</td>
                                <td><a href={suscripcion.enlace_boleta} target="_blank">Descargar</a></td>
                                <td>{suscripcion.activo ? 'Activo' : 'Inactivo'}</td>
                            </tr>
                        ))}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
}

export default HistorialPage;