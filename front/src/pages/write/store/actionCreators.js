import * as constants from "./constants";
import { api } from "../../../api";
// import { fromJS } from 'immutable';

// const changHomeData = (result) => ({
// 	type: constants.CHANGE_HOME_DATA,
// 	topicList: result.topicList,
// 	articleList: result.articleList,
// 	recommendList: result.recommendList
// });
const changeArticle = (content) => ({
  type: constants.CHANGE_ARTICLE_VALUE,
  value: content,
});
const changeArticleTitle = (title) => ({
  type: constants.CHANGE_ARTICLE_Title,
  value: title,
});

export const saveEditor = (content) => {
  return (dispatch) => {
    dispatch(changeArticle(content));
    console.log("保存成功", content);
  };
};

export const save = (title, content) => {
  return async (dispatch) => {
    const res = await api.createArticle(title, content);
    if (res && res.status === 200) {
      dispatch(changeArticle(content));
      dispatch(changeArticleTitle(title));
      console.log("保存成功", content);
    } else {
      alert("保存失败");
    }
  };
};
