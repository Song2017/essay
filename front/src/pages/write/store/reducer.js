import { fromJS } from "immutable";
import * as constants from "./constants";

const defaultState = fromJS({
  articleData: "default",
  title: "title",
});

function redu(state = defaultState, action) {
  switch (action.type) {
    case constants.CHANGE_ARTICLE_VALUE:
      return state.set("articleData", action.value);
    case constants.CHANGE_ARTICLE_Title:
      return state.set("title", action.value);
    default:
      return state;
  }
}
export default redu;
