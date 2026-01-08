import { API_URL } from "../utils/Config";
import axios from "axios";

const URL = `${API_URL}/series`;

export const listarSerieService = async () => {
    const res = await axios.get(`${URL}/`);
    return res;
}

export const mostrarSerieService = async (id) => {
    const res = await axios.get(`${URL}/${id}/`);
    return res;
}