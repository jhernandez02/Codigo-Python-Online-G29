import { Api } from "../utils/Api";
import { API_URL } from "../utils/Config";

const URL =  `${API_URL}/membresias`;

export const listarMembresiasService = async () => {
    const res = await Api().get(`${URL}/`);
    return res;
}