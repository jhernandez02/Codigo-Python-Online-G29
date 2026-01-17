import { PayPalScriptProvider, PayPalButtons } from "@paypal/react-paypal-js";

const initialOptions = { 
    'client-id': import.meta.env.VITE_PAYPAL_CLIENT_ID, 
    components: "buttons", 
    currency: "USD" 
}

const styleOptions = {
    shape: "rect",
    layout: "horizontal",
    color: "silver", //gold, blue, sivler, white, black
    label: "pay"
}

function PayPalButtonComponent(props){
    return (
        <PayPalScriptProvider options={initialOptions}>
            <PayPalButtons
                style={styleOptions}
                fundingSource="paypal"
                createOrder = {(data, actions)=>{
                    return actions.order.create({
                        purchase_units: [
                            {
                                amount: {
                                    value: props.monto
                                }
                            }
                        ]
                    }).then((orderId)=>{
                        console.log('orderId: ', orderId);
                        return orderId;
                    });
                }}
                onApprove = {(data, actions)=>{
                    return actions.order.capture().then(async (details)=>{
                        console.log('details: ', details);
                        console.log('Aprobado por ', details.payer.name.given_name);
                        // llamanos a nuestra funcion para generar la compra en nuestro sistema
                        await props.registrar();
                    });
                }}
                onError = {(error)=>{
                    console.log('Error en el pago:', error);
                }}
            />
        </PayPalScriptProvider>
    );
}

export default PayPalButtonComponent;