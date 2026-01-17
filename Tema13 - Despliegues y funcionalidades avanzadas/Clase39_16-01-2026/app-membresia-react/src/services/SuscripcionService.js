import { Api } from "../utils/Api";
import { API_URL } from "../utils/Config";

const URL =  `${API_URL}/suscripciones`;

export const listarSuscripcionesService = async () => {
    const res = await Api().get(`${API_URL}/usuario/suscripciones/`);
    return res;
}

export const registrarSuscripcionService = async (data) => {
    const res = await Api().post(`${URL}/`, data);
    return res;
}