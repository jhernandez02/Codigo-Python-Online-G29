import axios from "axios";

export const Api = () => {
    const token = localStorage.token;
    const apiAxios = axios.create({
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`
        }
    });
    return apiAxios;
}