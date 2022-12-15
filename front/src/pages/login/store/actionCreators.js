import { api } from "../../../api";
import * as constants from "./constants";
import * as util_const from "../../../utils/constants";
import { saveLocalToken, removeLocalToken } from "../../../utils/utils";

const changeLogin = () => ({
  type: constants.CHANGE_LOGIN,
  value: true,
});

export const logout = () => {
  return async (dispatch) => {
    removeLocalToken(util_const.TOKEN);

    dispatch({
      type: constants.LOGOUT,
      value: false,
    });
  };
};

export const login = (accout, password) => {
  return async (dispatch) => {
    const res = await api.logInGetToken(accout, password);
    if (res && res.data.access_token) {
      dispatch(changeLogin());
      saveLocalToken("test token");
    } else {
      alert("登陆失败");
      saveLocalToken(res);
    }
  };
};