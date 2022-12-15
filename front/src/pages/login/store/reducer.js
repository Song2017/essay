import { fromJS } from "immutable";
import * as constants from "./constants";
import { getLocalToken } from "../../../utils/utils";

const defaultState = fromJS({
  login: getLocalToken() != null,
});

function reducer(state = defaultState, action) {
  switch (action.type) {
    case constants.CHANGE_LOGIN:
      return state.set("login", action.value);
    case constants.LOGOUT:
      return state.set("login", action.value);
    default:
      return state;
  }
}
export default reducer;
