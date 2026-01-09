import { API_URL } from "../utils/Config";
import { Api } from "../utils/Api";

const URL = `${API_URL}/favoritos/usuario`;

export const listarFavoritoService = async () => {
    const res = await Api().get(`${URL}/`);
    return res;
}

export const guardarFavoritoService = async (data) => {
    const res = await Api().post(`${URL}/crear/`, data);
    return res;
}

export const eliminarFavoritoService = async (id) => {
    const res = await Api().delete(`${URL}/eliminar/${id}/`);
    return res;
}
