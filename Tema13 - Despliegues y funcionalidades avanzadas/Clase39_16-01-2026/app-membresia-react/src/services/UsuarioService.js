import axios from "axios";
import { API_URL } from "../utils/Config";

const URL =  `${API_URL}/token/`;

export const loginClienteService = async (data) => {
    const res = await axios.post(URL, data);
    return res;
}