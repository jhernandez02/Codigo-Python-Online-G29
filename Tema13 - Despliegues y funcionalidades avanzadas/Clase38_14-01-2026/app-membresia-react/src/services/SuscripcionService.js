import { Api } from "../utils/Api";
import { API_URL } from "../utils/Config";

const URL =  `${API_URL}/suscripciones`;

export const listarSuscripcionesService = async () => {
    const res = await Api().get(`${URL}/usuario`)
}

export const registrarSuscripcionService = async (data) => {
    const res = await Api().post(`${URL}/`, data)
}