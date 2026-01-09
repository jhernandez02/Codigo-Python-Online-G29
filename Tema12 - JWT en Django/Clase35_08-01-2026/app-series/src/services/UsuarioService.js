import { API_URL } from "../utils/Config";
import axios from "axios";

const URL = `${API_URL}/token/`;

export const loginUsuarioService = async (data) => {
    const res = await axios.post(URL, data);
    return res;
}
