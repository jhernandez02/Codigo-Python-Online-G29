import { useState, useEffect } from "react";
import { listarMembresiasService } from "../services/MembresiaServices";
import { registrarSuscripcionService } from "../services/SuscripcionService";
import PayPalButtonComponent from "../components/PaypalButtonComponent";
import Spinner from "react-bootstrap/Spinner";
import Swal from "sweetalert2";

function MembresiaPage(){
    const [membresias, setMembresias] = useState([]);
    const [cargando, setCargando] = useState(true);

    const listarMembresias = async () => {
        const res = await listarMembresiasService();
        setMembresias(res.data);
        setCargando(false);
    }

    const handleSuscribirse = async (membresia) => {
        const detalle = {
            "membresia": membresia.id,
            "fecha_inicio": "2026-01-12",
            "fecha_fin": "2027-01-11",
            "precio": membresia.precio,
            "activo": 1
        }
        const res = await registrarSuscripcionService(detalle);
        Swal.fire({
            title: "¡Suscripción generada!",
            text: "Su suscripción ha sido registrada satisfactoriamente",
            icon: "success"
        });
    };

     useEffect(()=>{
        listarMembresias();
    }, []);

    return(
        <div className="container mt-3">
            <div className="pricing-header p-3 pb-md-4 mx-auto text-center">
                <h1 className="display-4 fw-normal text-body-emphasis">Membresías</h1>
                <p className="fs-5 text-body-secondary">Quickly build an effective pricing table for your potential customers with this Bootstrap example. It’s built with default Bootstrap components and utilities with little customization.</p>
            </div>
            <div className="mt-4 row mb-3 text-center">
            {cargando ? (
                <div className="text-center">
                    <Spinner animation="border" variant="primary" />
                    <div>Cargando...</div>
                </div>
            ) : (
                membresias.map((item)=>(
                <div className="col" key={item.id}>
                    <div className="card mb-4 rounded-3 shadow-sm">
                        <div className="card-header py-3">
                            <h4 className="my-0 fw-normal">{item.nombre}</h4>
                        </div>
                        <div className="card-body">
                            <h1 className="card-title pricing-card-title">${item.precio}<small className="text-body-secondary fw-light">/mo</small></h1>
                            <ul className="list-unstyled mt-3 mb-4">
                                <li>10 users included</li>
                                <li>2 GB of storage</li>
                                <li>Email support</li>
                                <li>Help center access</li>
                            </ul>
                            <PayPalButtonComponent registrar={()=>handleSuscribirse(item)} monto={item.precio} />
                        </div>
                    </div>
                </div>
                ))
            )}
            </div>
        </div>
    );
}

export default MembresiaPage;