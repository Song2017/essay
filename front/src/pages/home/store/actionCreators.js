import * as constants from './constants';
import { api } from '../../../api';
import { fromJS } from 'immutable';

const changHomeData = (result) => ({
	type: constants.CHANGE_HOME_DATA,
	topicList: result.topicList,
	articleList: result.articleList,
	recommendList: result.recommendList
});

const addHomeList = (list, nextPage) => ({
	type: constants.ADD_ARTICLE_LIST,
	list: fromJS(list),
	nextPage
})

export const getHomeInfo = () => {
	return async (dispatch) =>  {
		const res = await api.getHomeInfo()
		dispatch(changHomeData(res.data.data));
	}
}

export const getMoreList = (page) => {
	return async (dispatch) => {
		const res = await api.getMoreList(page)
		dispatch(addHomeList(res.data.data, page + 1));

		// axios.get(process.env.REACT_APP_BACKEND_HOST+'/homeList?page=' + page).then((res) => {
		// 	const result = res.data.data;
		// 	dispatch(addHomeList(result, page + 1));
		// });
	}
}

export const toggleTopShow = (show) => ({
	type: constants.TOGGLE_SCROLL_TOP,
	show
})