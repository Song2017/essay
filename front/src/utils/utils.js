
import * as constants from "./constants";

export const getLocalToken = () => {
    return localStorage.getItem(constants.TOKEN)
};

export const saveLocalToken = (token) => {
    localStorage.setItem(constants.TOKEN, token);
}

export const removeLocalToken = () => localStorage.removeItem(constants.TOKEN);
