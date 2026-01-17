import { registrarSuscripcionService } from "../services/SuscripcionService";
import PayPalButtonComponent from "../components/PaypalButtonComponent";
import Swal from "sweetalert2";

function MembresiaPage(){
    const membresias = [
        {id:1,nombre:"Clásica",precio:"50"},
        {id:2,nombre:"Platinum",precio:"100"},
        {id:3,nombre:"Golden",precio:"150"},
    ];

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

    return(
        <div className="container mt-3">
            <div class="pricing-header p-3 pb-md-4 mx-auto text-center">
                <h1 class="display-4 fw-normal text-body-emphasis">Membresías</h1>
                <p class="fs-5 text-body-secondary">Quickly build an effective pricing table for your potential customers with this Bootstrap example. It’s built with default Bootstrap components and utilities with little customization.</p> </div>
            <div className="mt-4 row row-cols-1 row-cols-md-3 mb-3 text-center">
            {membresias.map((item)=>(
                <div class="col" key={item.id}>
                    <div class="card mb-4 rounded-3 shadow-sm">
                        <div class="card-header py-3">
                            <h4 class="my-0 fw-normal">{item.nombre}</h4>
                        </div>
                        <div class="card-body">
                            <h1 class="card-title pricing-card-title">${item.precio}<small class="text-body-secondary fw-light">/mo</small></h1>
                            <ul class="list-unstyled mt-3 mb-4">
                                <li>10 users included</li>
                                <li>2 GB of storage</li>
                                <li>Email support</li>
                                <li>Help center access</li>
                            </ul>
                            <PayPalButtonComponent registrar={()=>handleSuscribirse(item)} monto={item.precio} />
                        </div>
                    </div>
                </div>
            ))}
            </div>
        </div>
    );
}

export default MembresiaPage;