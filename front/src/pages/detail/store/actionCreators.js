import { api } from '../../../api';
import * as constants from './constants';

const changeDetail = (title, content) => ({
	type: constants.CHANGE_DETAIL,
	title,
	content
});

export const getDetail = (id) => {
	return async (dispatch) => {
		const res = await api.getDetail(id)
		const result = res.data[0];
		dispatch(changeDetail(result.title, result.content));
	}
};